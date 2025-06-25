from demoga_tests.data import users
from demoga_tests.model.pages.registration_page import RegistrationPage


def test_forms_filling_and_submit(open_page_demoqa):
    registration_page = RegistrationPage()
    student = users.student
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)