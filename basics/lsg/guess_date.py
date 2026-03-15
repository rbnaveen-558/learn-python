
import pytest


MONTH_DAYS = {
    "01" : "31",
    "02" : "28" ,
    "03" : "31",
    "04" : "30",  
    "05" : "31",
    "06" : "30",   
    "07" : "31",
    "08" : "31",
    "09" : "30",
    "10" : "31",
    "11" : "30",
    "12" : "31" 
}


# def valid_date(date):
#     month, days = date.split('-')
#     validate_month = False
#     validate_days = False
#     if(month.find("?") != -1):
#         pass
#     else:
#         validate_month = month in MONTH_DAYS

#     if(days.find("?") != -1):
#         pass
#     else:
#         validate_days = days == MONTH_DAYS.get(month)
#     return validate_month and validate_days


def solution(date):
    
    # Replace ':' with '-' for uniformity
    date = date.replace(':', '-')
    month, day = date.split('-')
    # Try to fix month
    if '?' in month:
        for m in range(1, 13):
            m_str = f"{m:02d}"
            if all(a == b or a == '?' for a, b in zip(month, m_str)):
                month = m_str
                break
        else:
            return "xx-xx"
    # Try to fix day
    if '?' in day:
        for d in range(1, 32):
            d_str = f"{d:02d}"
            if all(a == b or a == '?' for a, b in zip(day, d_str)):
                day = d_str
                break
        else:
            return "xx-xx"
    # Validate month and day
    if month not in MONTH_DAYS:
        return "xx-xx"
    max_day = int(MONTH_DAYS[month])
    if not (1 <= int(day) <= max_day):
        return "xx-xx"
    return f"{month}-{day}"

# Examples
examples = ["01-31", "02-30", "?1:31", "01:4?", "??:28", "1?:??", "??-??", "1?-30", "0?-??", "??-3?"]
for ex in examples:
    print(f"{ex} -> {solution(ex)}")