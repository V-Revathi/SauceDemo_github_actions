import pytest

@pytest.fixture
def trace_specific_api_call():
    traced_responses = []

    def enable_tracing(page, url_substring: str):
        def handle_response(response):
            if url_substring in response.url:
                traced_responses.append(response)
        page.on("response", handle_response)

    return traced_responses, enable_tracing
