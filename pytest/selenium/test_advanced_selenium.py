import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(EC.title_contains("Selenium Pytest Demo"))

    def choose_color(self, value):
        option = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[name='color'][value='{value}']"))
        )
        option.click()

    def toggle_feature(self, feature_id):
        checkbox = self.wait.until(
            EC.element_to_be_clickable((By.ID, feature_id))
        )
        checkbox.click()

    def choose_category(self, category_value):
        select = self.wait.until(
            EC.element_to_be_clickable((By.ID, "category"))
        )
        from selenium.webdriver.support.ui import Select
        Select(select).select_by_value(category_value)

    def search(self, text):
        search_input = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "query"))
        )
        search_input.clear()
        search_input.send_keys(text)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "search-button"))
        ).click()

    def get_result_text(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.ID, "result"))
        ).text

    def assert_result_contains(self, expected):
        actual = self.get_result_text()
        assert expected in actual, f"Expected '{expected}' in result text, got '{actual}'"


def create_advanced_demo_page(tmp_path):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>Selenium Pytest Demo</title>
        <script>
            function handleSearch(event) {
                event.preventDefault();
                const query = document.querySelector('[name=query]').value;
                const result = document.getElementById('result');
                result.textContent = 'Search complete for ' + query;
                result.style.fontWeight = 'bold';
            }
        </script>
    </head>
    <body>
        <header>
            <h1>Advanced Selenium Pytest Example</h1>
        </header>

        <section>
            <form id="search-form" onsubmit="handleSearch(event)">
                <label for="query">Search query</label>
                <input id="query" name="query" value="advanced" />

                <fieldset id="color-options">
                    <legend>Choose a color</legend>
                    <label><input type="radio" name="color" value="red" /> Red</label>
                    <label><input type="radio" name="color" value="green" checked /> Green</label>
                    <label><input type="radio" name="color" value="blue" /> Blue</label>
                </fieldset>

                <fieldset id="feature-options">
                    <legend>Feature toggles</legend>
                    <label><input type="checkbox" id="feature-a" value="feature-a" checked /> Feature A</label>
                    <label><input type="checkbox" id="feature-b" value="feature-b" /> Feature B</label>
                </fieldset>

                <label for="category">Category</label>
                <select id="category" name="category">
                    <option value="all">All</option>
                    <option value="books" selected>Books</option>
                    <option value="electronics">Electronics</option>
                </select>

                <button id="search-button" type="submit">Run search</button>
            </form>
            <div id="result" aria-live="polite"></div>
        </section>
    </body>
    </html>
    """
    path = tmp_path / "advanced_demo_page.html"
    path.write_text(html, encoding="utf-8")
    return path


@pytest.mark.parametrize("search_term", ["pytest", "selenium", "page object"])
def test_page_object_search_and_assertions(browser, tmp_path, search_term):
    page = DemoPage(browser)
    demo_page = create_advanced_demo_page(tmp_path)

    page.open(demo_page.as_uri())
    page.search(search_term)

    page.assert_result_contains(search_term)
    assert "Search complete" in page.get_result_text()


def test_form_controls_in_page_object(browser, tmp_path):
    page = DemoPage(browser)
    demo_page = create_advanced_demo_page(tmp_path)

    page.open(demo_page.as_uri())
    page.choose_color("blue")
    page.toggle_feature("feature-b")
    page.choose_category("electronics")
    page.search("page object")

    assert "Search complete" in page.get_result_text()
    assert "page object" in page.get_result_text()


def test_timeout_exception_for_missing_element(browser, tmp_path):
    demo_page = create_advanced_demo_page(tmp_path)
    browser.get(demo_page.as_uri())

    with pytest.raises(TimeoutException):
        WebDriverWait(browser, 2).until(
            EC.visibility_of_element_located((By.ID, "missing-element"))
        )
