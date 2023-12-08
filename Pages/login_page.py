from Pages.BasePage import BasePage
from time import sleep

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_login_button(self):
        self.click_element("login_link_XPATH")
    
    def do_login(self, username, password):
        self.click_login_button()
        sleep(3)
        self.send_values("phone_number_field_XPATH",username)
        self.send_values("passwords_field_XPATH", password)
        self.click_element("login_button_XPATH")
        sleep(3)
        
    def assert_correct_notification_message(self, expected_message):
        element_text=self.get_element_Text("notification_message_XPATH")
        assert element_text==expected_message
    
    def capture_screen_shot(self,file_name):
        self.take_screenshot(file_name)
        
    def logout(self):
        self.click_element("side_humbager_XPATH")
        self.scroll_to_the_bottom()
        sleep(3)
        self.click_element("logout_button_XPATH")