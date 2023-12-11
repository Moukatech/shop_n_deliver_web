from Pages.BasePage import BasePage
from time import sleep


class MyBetsPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def capture_screen_shot(self,file_name):
        self.take_screenshot(file_name)
    
    def select_bet_slip(self):
        self.click_element("mybest_button_XPATH")
        self.click_element("open_bet_slip_XPATH")
    
    def Rebet(self,amount):
        self.select_bet_slip()
        self.click_element("rebet_button_XPATH")
        self.click_element("continue_button_XPATH")
        self.clear_textbox("input_bet_amount_XPATH")
        self.send_values("input_bet_amount_XPATH",amount)
        self.click_element("place_bet_button_XPATH")
        element= len(self.CountElementsOnPage("notification_popup_XPATH"))
        assert element>0
        sleep(1)
    
    def Cancel_bet(self):
        self.select_bet_slip()
        self.click_element("cancel_bet_XPATH")
        self.click_element("continue_button_XPATH")
        
        
    def cashout_bet(self):
        self.select_bet_slip()
        self.click_element("request_cashout_XPATH")
        sleep(2)
        self.click_element("approve_cashout_XPATH")
        sleep(2)
        self.click_element("continue_button_XPATH")
        element= len(self.CountElementsOnPage("notification_popup_XPATH"))
        assert element>0
        sleep(2)
        
    
    def assert_correct_notification_message(self, expected_message):
        element_text=self.get_element_Text("notification_message_XPATH")
        assert element_text==expected_message
    
    