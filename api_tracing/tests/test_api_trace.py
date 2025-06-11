from playwright.sync_api import sync_playwright,expect
from workflows.login_workflow import login


def test_trace_specific_api(trace_specific_api_call):
    traced_responses, enable_tracing = trace_specific_api_call
    api_url = "https://events.backtrace.io/api/summed-events/submit?universe=UNIVERSE&token=TOKEN"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        enable_tracing(page, api_url)

        page.goto("https://www.saucedemo.com/")
        if traced_responses:
            print("Target API called before login (unexpected)!")
        else:
            print("Target API not called before login (as expected).")

        login(page)

        expect(page.locator('[data-test="inventory-list"]')).to_be_visible()

        page.wait_for_timeout(3000)
        browser.close()
    assert traced_responses, f"No requests found for: {api_url}"


    for resp in traced_responses:
        print(f"Traced API URL: {resp.url}")
        print(f"Status: {resp.status}")
