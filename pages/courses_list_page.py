from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
# Импортируем компонент
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent

from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from components.views.empty_view_component import EmptyViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        # Локаторы были заменены компонентом
        self.toolbar_view = CoursesListToolbarViewComponent(page)

        # Локаторы заменены компонентом
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        # Заменили локаторы на компонент
        self.course_view = CourseViewComponent(page)

        # Заголовок и кнопка создания курса
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

     # Методы были удалены, т.к. в автотестах будут использоваться методы компонента




