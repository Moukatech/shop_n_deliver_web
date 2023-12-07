from Pages.BasePage import BasePage
from time import sleep


class BetPlacementPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def place_bet(self):

        self.click_element("first_bet_XPATH")
        self.click_element("second_bet_XPATH")
        self.click_element("third_bet_XPATH")
        sleep(3)
    
    def share_slip(self):
        
        self.click_element("share_slip_XPATH")
        sleep(3)
        element = len(self.CountElementsOnPage("copy_slip_link_XPATH"))
        assert element > 0  #assert that element is on the page
        
    def capture_screen_shot(self,file_name):
        
        self.take_screenshot(file_name)