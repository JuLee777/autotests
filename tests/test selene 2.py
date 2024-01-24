from playwright.sync_api import Page, expec


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_label("Пошук", exact=True).fill("yashaka/selene")
    #page.wait_for_selector('.ekjLze [class="g"]')
    page.locator('.ekjLze' [class="g"]').click()
    qa = 'selene'
    assert qa in page.text_content('html').lower()
    print(page.inner_text("html).lower().count(qa))