from components.authentication.registration_form_component import RegistrationFormComponent
from fixtures.browsers import initialize_browser_state
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)







