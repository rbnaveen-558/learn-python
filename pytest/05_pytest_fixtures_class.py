import pytest

@pytest.fixture(scope="module")
def browser():
    # setup (runs once per class)
    print("\n[SETUP CLASS] Launching browser...")
    driver = {"session": "ChromeDriver"}   # imagine this is a Selenium driver
    yield driver
    # teardown (runs once after all tests in class)
    print("\n[TEARDOWN CLASS] Closing browser...")
    driver.clear()

@pytest.fixture(scope="function")
def fresh_page(browser):
    # setup (runs before each test)
    print("[SETUP METHOD] Opening fresh page...")
    page = {"url": "http://localhost:8000", "driver": browser}
    yield page
    # teardown (runs after each test)
    print("\n[TEARDOWN METHOD] Clearing page state...")
    page.clear()


class TestWebApp:
    def test_homepage_loads(self, fresh_page):
        pass
        # assert fresh_page["url"] == "http://localhost:8000"

    @pytest.mark.parametrize("username,password", [
        ("user1", "pass1"), 
        ("user2", "pass2")
    ])
    def test_add_item(self, fresh_page, username, password):
        print(username, password)
        # fresh_page["item"] = "Book"
        # assert "item" in fresh_page