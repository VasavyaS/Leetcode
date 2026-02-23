#
# Problem: 2043. Simple Bank System
# Difficulty: Medium
# Link: https://leetcode.com/problems/simple-bank-system/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Language: python3
# Date: 2026-02-23


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) or account2 > len(self.balance):
            return False
        if self.balance[account1-1] < money:
            return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        if money > self.balance[account -1]:
            return False
        self.balance[account -1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
