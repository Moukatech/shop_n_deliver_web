import pytest

from Pages.bet_placement_page import BetPlacementPage

from time import sleep

@pytest.mark.usefixtures("init_driver")
# @pytest.mark.usefixtures("login")
class TestBetting:

    
    def test_verify_user_can_place_bets(self,login):
        login
        betting = BetPlacementPage(self.driver)
        betting.select_odds()
        betting.place_bet(10)
        betting.assert_correct_notification_message("Your bet is being processed. Kindly check your notifications shortly")
        betting.capture_screen_shot("success_bet.png")
    
    def test_verify_user_can_share_betslip(self,login):
        login
        betting = BetPlacementPage(self.driver)
        sleep(3)
        betting.select_odds()
        betting.share_slip()
        betting.capture_screen_shot("share_betslip.png")
        betting.place_bet("10")