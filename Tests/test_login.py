import pytest

from Pages.login_page import LoginPage
from time import sleep
import pandas as pd
import os
from Utilities.data import get_login_data


file_path = os.path.join(os.path.dirname(__file__),'..' ,'users.xlsx')

df = pd.read_excel(file_path)
mobile_num,password = get_login_data()

@pytest.mark.usefixtures("init_driver")
class Testlogin:
    
    def test_correct_login(self):
        
        login = LoginPage(self.driver)
        login.do_login(mobile_num,password)
    
    def test_multiple_accounts_login(self):
        login = LoginPage(self.driver)
        for i in df.itertuples():

            User = i.phone_number
            Pass = i.Password
            login.do_login(User, Pass)
    
    def test_invalid_login(self):
        login = LoginPage(self.driver)
        login.do_login("0729208685","Testssfd2")
        login.assert_correct_error("The mobile and password provided do not match")
        login.capture_screen_shot("loginError.png")