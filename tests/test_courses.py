import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.course
def test_create_course(courses_list_page: CoursesListPage, create_courses_page: CreateCoursePage):

    create_courses_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_courses_page.check_visible_create_course_title()
    create_courses_page.check_disabled_create_course_button()
    create_courses_page.check_visible_image_preview_empty_view()
    # create_courses_page.check_visible_image_upload_view()

    create_courses_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_courses_page.check_visible_create_course_form(
        title= "",
        estimated_time= "",
        description= "",
        max_score= "0",
        min_score= "0"
    )
    create_courses_page.check_visible_exercises_title()
    create_courses_page.check_visible_create_exercise_button()
    create_courses_page.check_visible_exercises_empty_view()
    create_courses_page.check_visible_image_upload_view()
    create_courses_page.upload_preview_image()
    create_courses_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright1",
        max_score="100",
        min_score="10"
    )

    create_courses_page.click_create_course_button()

    #courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage, create_courses_page: CreateCoursePage,
                            dashboard_page_with_state):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    dashboard_page_with_state.navbar.check_visible('username')  # используем атрибут navbar со страницы dashboard_page
    dashboard_page_with_state.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()

