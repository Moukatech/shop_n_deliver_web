import pytest

from Pages.mybets_page import MyBetsPage
from Pages.bet_placement_page import BetPlacementPage
from time import sleep

@pytest.mark.usefixtures("init_driver")
class TestMyBets:
    def test_user_is_able_to_rebet(self,login):
        login
        place_bet = BetPlacementPage(self.driver)
        sleep(3)
        place_bet.select_odds()
        place_bet.place_bet("10")
        
        bets = MyBetsPage(self.driver)
        bets.Rebet(10)
    
    
    def test_user_is_able_to_cancel_bet(self,login):
        login
        bets = MyBetsPage(self.driver)
        bets.Cancel_bet()
    
    def test_user_is_able_to_cashout(self,login):
        login
        bets = MyBetsPage(self.driver)
        bets.cashout_bet()