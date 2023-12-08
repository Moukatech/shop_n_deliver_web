from Pages.BasePage import BasePage
from time import sleep


class BetPlacementPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def select_odds(self):

        self.click_element("first_bet_XPATH")
        self.click_element("second_bet_XPATH")
        self.click_element("third_bet_XPATH")
        sleep(3)
    
    def share_slip(self):
        
        self.click_element("share_slip_XPATH")
        sleep(3)
        element = len(self.CountElementsOnPage("copy_slip_link_XPATH"))
        assert element > 0  #assert that element is on the page
        sleep(1)
        
        
        
    def capture_screen_shot(self,file_name):
        self.take_screenshot(file_name)
        sleep(1)    
    
    def close_popup(self):
        self.click_element("close_share_popup_XPATH")
        
    def place_bet(self,amount,file_name):
        self.clear_textbox("input_bet_amount_XPATH")
        self.send_values("input_bet_amount_XPATH",amount)
        self.click_element("place_bet_button_XPATH")
        element= len(self.CountElementsOnPage("notification_popup_XPATH"))
        assert element>0
        sleep(2)
        
        
    def assert_correct_notification_message(self, expected_message):
        element_text=self.get_element_Text("notification_message_XPATH")
        assert element_text==expected_message