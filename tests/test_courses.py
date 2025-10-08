import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state, chromium_page: Page):
        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # data-testid="courses-list-toolbar-title-text"
        courses_list_toolbar = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_list_toolbar).to_be_visible()

        # data-testid="courses-list-empty-view-icon"
        view_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(view_icon).to_be_visible()

        # data-testid="courses-list-empty-view-title-text"
        title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(title_text).to_be_visible()

        # data-testid="courses-list-empty-view-description-text"
        description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_text).to_be_visible()

        chromium_page_with_state.wait_for_timeout(3000)