
from demoga_tests.data import users_simpl
from demoga_tests.model.application import app

def test_simple_forms_filling_and_submit(open_page_demoqa):
    student = users_simpl.student_simpl
    app.left_panel.open_simple_registration_form()
    app.registration_simple_page.register(student)
    app.registration_simple_page.should_have_registered(student)
