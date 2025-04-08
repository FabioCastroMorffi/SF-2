from segment import Segment
from __future__ import annotations
from functools import total_ordering

@total_ordering
class Account:
    def __init__(self, gold):
        '''Create account with gold'''
        self.gold = gold
    def addGold(self, amount: int) -> None:
        self.gold += amount
    def zeroGold(self) -> None:
        self.gold = 0
    def doubleGold(self) -> None:
        self.gold *= 2
    def __lt__(self, other_account: Account) -> bool:
        '''
        return True if Account and other are of the same type and gold of Account is less than gold of other.
        '''
        return isinstance(other_account, Account) and self.gold < other_account.gold
    def __eq__(self, other_account: Account) -> bool:
        return isinstance(other_account, Account) and self.gold == other_account.gold
    def __repr__(self):
         return f'Gold -> {self.gold}'
    
a1 = Account(1000)
a2 = Account(2000)
value = 400
print(a1)
print('a4')
print(a1 != a2)
