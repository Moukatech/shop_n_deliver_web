from Pages.BasePage import BasePage
from time import sleep
class RegistrationPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def register(self, phone_number, password, confirm_password):
        self.click_element("register_link_XPATH")
        sleep(3)
        self.send_values("phone_number_field_XPATH",phone_number)
        self.send_values("passwords_field_XPATH", password)
        self.send_values("confirm_password_field_XPATH",confirm_password)
        self.click_element("TERMS_checkbox_XPATH")
        self.click_element("register_button_XPATH")
        sleep(3)
    
    def assert_correct_error_message(self, expected_error_message):
        element_text=self.get_element_Text("invalid_phone_num_error_message_XPATH")
        assert element_text==expected_error_message
    
    def capture_screen_shot(self,file_name):
        self.take_screenshot(file_name)