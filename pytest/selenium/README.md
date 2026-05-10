# Pytest Selenium Examples

This folder contains two example suites that demonstrate how to combine `pytest` and `selenium` to write browser automation tests in Python.

## Files

- `conftest.py`
  - Provides a reusable `browser` fixture for Chrome and Firefox.
  - Uses an implicit wait for convenience and configures headless mode by default.
- `test_basic_selenium.py`
  - Shows how to locate elements using `By.ID`, `By.CSS_SELECTOR`, `By.CLASS_NAME`, and `By.TAG_NAME`.
  - Demonstrates explicit waits with `WebDriverWait` and `expected_conditions`.
  - Includes basic assertions for text content, attributes, and element state.
  - Adds form control coverage for radio buttons, checkboxes, and select dropdowns.
- `test_advanced_selenium.py`
  - Implements a lightweight page object model to encapsulate page interactions.
  - Uses parameterized tests via `pytest.mark.parametrize`.
  - Adds custom assertion helpers and explicit timeout handling.
  - Demonstrates form interaction with radio buttons, checkboxes, and dropdown selection.

## Features Covered

- Locators
  - `find_element` and `find_elements`
  - `By.ID`, `By.CLASS_NAME`, `By.CSS_SELECTOR`, `By.TAG_NAME`, `By.NAME`
- Waiting strategies
  - implicit wait configured in `conftest.py`
  - explicit wait with `WebDriverWait`
  - common conditions like `visibility_of_element_located`, `element_to_be_clickable`, and `text_to_be_present_in_element`
- Assertions
  - `assert` for element text and attributes
  - explicit assertion messages for easier failure diagnosis
  - `pytest.raises` for expected timeout exceptions

## Prerequisites

Install the required packages with:

```bash
pip install pytest selenium
```

Also make sure the browser driver is available on your PATH:

- Chrome: `chromedriver`
- Firefox: `geckodriver`

## Run the examples

Execute the examples from the repository root:

```bash
pytest pytest/selenium
```

To switch browsers:

```bash
pytest pytest/selenium --browser firefox
```

## Notes

- The tests use simple locally generated HTML files under `tmp_path`, so they are self-contained and do not depend on an external website.
- The `browser` fixture closes the driver session after the test session completes.
