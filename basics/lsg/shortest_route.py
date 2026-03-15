import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# ---------- CREATE TABLES ----------
cur.executescript("""
CREATE TABLE airports (
    port TEXT PRIMARY KEY,
    city TEXT
);

CREATE TABLE flights (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    source_port TEXT,
    end_port    TEXT,
    start_time  TEXT,
    end_time    TEXT
);
""")

# ---------- DUMMY DATA ----------
airports = [
    ("JFK", "NewYork"),
    ("LAX", "LosAngeles"),
    ("ORD", "Chicago"),
    ("LHR", "London"),
    ("DXB", "Dubai"),
    ("SIN", "Singapore"),
    ("NRT", "Tokyo"),
    ("HKG", "HongKong"),
]
cur.executemany("INSERT INTO airports VALUES (?, ?)", airports)

flights = [
    # Direct routes
    ("JFK", "LHR",  "08:00", "20:00"),  # NewYork -> London
    ("JFK", "ORD",  "06:00", "08:30"),  # NewYork -> Chicago
    # Via London
    ("LHR", "DXB",  "10:00", "18:00"),  # London  -> Dubai
    ("DXB", "NRT",  "20:00", "08:00"),  # Dubai   -> Tokyo
    # Via Los Angeles (shorter hop count)
    ("JFK", "LAX",  "07:00", "10:30"),  # NewYork -> LosAngeles
    ("LAX", "NRT",  "12:00", "16:00"),  # LosAngeles -> Tokyo (direct)
    # Via Chicago -> HongKong -> Tokyo
    ("ORD", "HKG",  "09:00", "14:00"),  # Chicago -> HongKong
    ("HKG", "NRT",  "15:00", "19:00"),  # HongKong -> Tokyo
    # Via Singapore
    ("DXB", "SIN",  "21:00", "07:00"),  # Dubai -> Singapore
    ("SIN", "NRT",  "09:00", "17:00"),  # Singapore -> Tokyo
]
cur.executemany(
    "INSERT INTO flights (source_port, end_port, start_time, end_time) VALUES (?,?,?,?)",
    flights
)

# ---------- QUERY: SHORTEST ROUTE (fewest stops) ----------
# Uses a recursive CTE to find all paths from JFK to NRT.
# Stops at depth 5 to avoid infinite loops (no real cycles in dummy data).

query = """
WITH RECURSIVE route(path, current_port, hops) AS (
    -- Start: all flights leaving from NewYork (JFK)
    SELECT
        a_src.city || ' -> ' || a_dst.city AS path,
        f.end_port,
        1 AS hops
    FROM flights f
    JOIN airports a_src ON f.source_port = a_src.port
    JOIN airports a_dst ON f.end_port    = a_dst.port
    WHERE a_src.city = 'NewYork'

    UNION ALL

    -- Extend the path one hop at a time (avoid revisiting ports)
    SELECT
        r.path || ' -> ' || a_dst.city,
        f.end_port,
        r.hops + 1
    FROM route r
    JOIN flights f      ON r.current_port = f.source_port
    JOIN airports a_dst ON f.end_port = a_dst.port
    WHERE r.hops < 5
      AND r.path NOT LIKE '%' || a_dst.city || '%'  -- no cycles
)
SELECT path, hops
FROM route
JOIN airports a ON route.current_port = a.port
WHERE a.city = 'Tokyo'
ORDER BY hops
LIMIT 5;
"""

print("=" * 55)
print("  Shortest routes from NewYork to Tokyo (fewest hops)")
print("=" * 55)
cur.execute(query)
rows = cur.fetchall()
for rank, (path, hops) in enumerate(rows, 1):
    print(f"  #{rank} [{hops} hop(s)]  {path}")

conn.close()
