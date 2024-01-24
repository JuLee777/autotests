from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    browser = page.chromium.launch(headless=False)
    page = browser.new_context()

    page.goto("https://www.google.com/")
    page.get_by_label("Пошук", exact=True).fill("yashaka/selene")
    page.wait_for_selector('h3').click()
    asser 'selene' in page.text_content().lower()