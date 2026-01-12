from components.courses.course_view_component import CourseViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent

from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from components.views.empty_view_component import EmptyViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Локаторы заменены компонентом
        self.empty_view = EmptyViewComponent(page, 'courses-list')
        # Заменили локаторы на компонент
        self.course_view = CourseViewComponent(page)

        # Заголовок и кнопка создания курса
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_courses_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # Карточка курса теперь на странице EmptyViewComponent
        # self.course_title = page.get_by_test_id('course-widget-title-text')
        # self.course_image = page.get_by_test_id('course-preview-image')
        # self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        # self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        # self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        # # Меню курса теперь на странице EmptyViewComponent
        # self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        # self.course_edit_menu_item = page.get_by_test_id('course-view-edit-menu-item')
        # self.course_delete_menu_item = page.get_by_test_id('course-view-delete-menu-item')

        # Пустой блок при отсутствии курсов/ теперь это в строке self.empty_view = EmptyViewComponent(page, identifier='courses-list')
        # self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        # self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        # self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')


    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

        # expect(self.empty_view_icon).to_be_visible()
        #
        # expect(self.empty_view_title).to_be_visible()
        # expect(self.empty_view_title).to_have_text('There is no results')
        #
        # expect(self.empty_view_description).to_be_visible()
        # expect(self.empty_view_description).to_have_text(
        #     'Results from the load test pipeline will be displayed here'
        # )

    def check_visible_create_courses_button(self):
        expect(self.create_courses_button).to_be_visible()

    def click_create_courses_button(self):
        self.create_courses_button.click()

# теперь на отдельной странице EmptyViewComponent
    # def check_visible_course_card(
    #         self,
    #         index: int = 0,
    #         title: str = "Playwright2",
    #         max_score: str = "100",
    #         min_score: str = "10",
    #         estimated_time: str = "2 weeks"
    # ):
    #     # индекс дает возможность работать с конкретным курсом, если он на стр не один
    #     expect(self.course_image.nth(index)).to_be_visible()
    #
    #     expect(self.course_title.nth(index)).to_be_visible()
    #     expect(self.course_title.nth(index)).to_have_text(title)
    #
    #     expect(self.course_max_score_text.nth(index)).to_be_visible()
    #     expect(self.course_max_score_text.nth(index)).to_have_text(f'Max score: {max_score}')
    #
    #     expect(self.course_min_score_text.nth(index)).to_be_visible()
    #     expect(self.course_min_score_text.nth(index)).to_have_text(f'Min score: {min_score}')
    #
    #     expect(self.course_estimated_time_text.nth(index)).to_be_visible()
    #     expect(self.course_estimated_time_text.nth(index)).to_have_text(f'Estimated time: {estimated_time}')


# теперь на странице EmptyViewComponent
    # def click_edit_course(self, index: int):
    #     self.course_menu_button.nth(index).click()
    #
    #     expect(self.course_menu_button.nth(index)).to_be_visible()
    #     expect(self.course_menu_button.nth(index)).click()
    #
    # def click_delete_course(self, index: int):
    #     self.course_delete_menu_item.nth(index).click()
    #
    #     expect(self.course_delete_menu_item.nth(index)).to_be_visible()
    #     expect(self.course_delete_menu_item.nth(index)).click()