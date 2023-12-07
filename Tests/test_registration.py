import pytest

from Pages.registration_page import RegistrationPage
from time import sleep
from Utilities.data import generate_phone_number_and_password as data_generator

@pytest.mark.usefixtures("init_driver")
class TestRegistration:
    def test_user_can_register_successfully(self):
        ## mobile_num, password=data_generator()  
        ## The function above is commented out because random 
        ## customers will receive messages and this could be spamming.
        register = RegistrationPage(self.driver)
        register.register("0113035065", "Test123", "Test123")
        register.capture_screen_shot("registation_form.png")
        
    def test_invalid_phone_number_on_registration(self):
        
        register = RegistrationPage(self.driver)
        register.register("084344455", "Test123", "Test123")
        register.assert_correct_error_message("Invalid mobile number")
        register.capture_screen_shot("registation_form.png")