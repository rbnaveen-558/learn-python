import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_demo_page(tmp_path):
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
                document.getElementById('result').textContent = 'Search complete for ' + query;
            }
        </script>
    </head>
    <body>
        <h1 id="main-title">Selenium Pytest Demo</h1>
        <p id="main-paragraph">This page is a minimal test target for locator and wait examples.</p>
        <a class="nav-item" href="/login" id="login-link">Login</a>

        <form id="search-form" onsubmit="handleSearch(event)">
            <label for="query">Search query</label>
            <input type="text" id="query" name="query" value="pytest" />
            <button type="submit" id="search-button">Search</button>

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
                <label><input type="checkbox" id="feature-c" value="feature-c" /> Feature C</label>
            </fieldset>

            <label for="category">Category</label>
            <select id="category" name="category">
                <option value="all">All</option>
                <option value="books" selected>Books</option>
                <option value="electronics">Electronics</option>
            </select>
        </form>

        <div id="result" style="margin-top: 16px; color: green;"></div>
    </body>
    </html>
    """
    path = tmp_path / "demo_page.html"
    path.write_text(html, encoding="utf-8")
    return path


def test_basic_locators_and_assertions(browser, tmp_path):
    page = create_demo_page(tmp_path)
    browser.get(page.as_uri())

    assert browser.title == "Selenium Pytest Demo"

    heading = browser.find_element(By.ID, "main-title")
    assert heading.text == "Selenium Pytest Demo"

    paragraph = browser.find_element(By.CSS_SELECTOR, "#main-paragraph")
    assert "minimal test target" in paragraph.text

    login_link = browser.find_element(By.CLASS_NAME, "nav-item")
    assert login_link.get_attribute("href").endswith("/login")
    assert login_link.text == "Login"

    form = browser.find_element(By.TAG_NAME, "form")
    assert form.get_attribute("id") == "search-form"


def test_form_controls_radio_checkboxes_and_select(browser, tmp_path):
    page = create_demo_page(tmp_path)
    browser.get(page.as_uri())

    selected_color = browser.find_element(By.CSS_SELECTOR, "input[name='color']:checked")
    assert selected_color.get_attribute("value") == "green"

    all_colors = browser.find_elements(By.NAME, "color")
    assert len(all_colors) == 3
    all_colors[2].click()
    assert all_colors[2].is_selected()

    feature_a = browser.find_element(By.ID, "feature-a")
    feature_b = browser.find_element(By.ID, "feature-b")
    assert feature_a.is_selected()
    assert not feature_b.is_selected()

    feature_b.click()
    assert feature_b.is_selected()

    category_select = Select(browser.find_element(By.ID, "category"))
    assert category_select.first_selected_option.get_attribute("value") == "books"
    category_select.select_by_value("electronics")
    assert category_select.first_selected_option.get_attribute("value") == "electronics"


def test_wait_strategy_and_dynamic_content(browser, tmp_path):
    page = create_demo_page(tmp_path)
    browser.get(page.as_uri())

    query_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "query"))
    )
    assert query_input.get_attribute("value") == "pytest"

    query_input.clear()
    query_input.send_keys("selenium")

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert submit_button.is_enabled()
    submit_button.click()

    result = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "result"), "Search complete for selenium")
    )
    assert result is True

    result_text = browser.find_element(By.ID, "result").text
    assert "Search complete" in result_text
    assert result_text.endswith("selenium")
