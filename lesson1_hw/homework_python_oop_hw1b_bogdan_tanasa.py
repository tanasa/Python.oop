#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Account class
#   This is not an account.
#   Instead, this is a blueprint (for a bank account)
#   The thing that shows what an account would look like.
#   What data does it have (instance variables) and what functions does it have (called methods)


class Account:
    
    def __init__(self, name, balance, password):
        """
        Initialize a new account with the owner's name, initial balance, and password.
        """
        self.name = name
        self.balance = float(balance)
        self._password = password  
        self.interest_applied = False   # a boolean attribute to monitor whether the interest has been applied
                                        # when we deposit or withdraw, we keep the boolean attribute on False
                                        # when we add Interest to our account, we change it on True, 
                                        # to mark that the interest was applied 

    def show(self):
        """
        Display account details.
        """
        print('Account Details:')
        print(f'       Name: {self.name}')
        print(f'       Balance: ${self.balance:.2f}')

    def getBalance(self, password):
        """
        Return the balance if the password is correct.
        """
        if password != self._password:
            print('Sorry, incorrect password.')
            return -1
        return self.balance

    def deposit(self, amount, password):
        """
        Deposit money into the account if the password is correct and the amount is positive.
        """
        if amount < 0:
            raise ValueError("You cannot deposit a negative amount.")
        
        if password != self._password:
            print('Sorry, incorrect password.')
            return -1
        
        self.balance += amount
        
        self.interest_applied = False                   # it resets interest application status
                                                        # signaling that the account is eligible for interest again.
        
        return self.balance

    def withdraw(self, amount, password):
        """
        Withdraw money from the account if the password is correct and there are sufficient funds.
        """
        if amount < 0:
            raise ValueError("You cannot withdraw a negative amount.")
        
        if amount > self.balance:
            print('You cannot withdraw more than your current balance.')
            return -1

        if password != self._password:
            print('Incorrect password for this account.')
            return -1
        
        self.balance -= amount
        
        self.interest_applied = False                     # it resets interest application status 
                                                          # signaling that the account is eligible for interest again.
      
        return self.balance

    def addInterest(self):
        """
        Add interest to the balance based on the current balance.
        Interest can only be applied once unless the balance changes.
        """
        
        if self.interest_applied:
            print('Interest has already been applied. Cannot add interest again without balance change.')
            return self.balance
        
        # The method first checks if interest_applied is True.
        # If it is, it means interest has already been added since the last balance change, 
        # and the method exits without applying interest again.
        
        # Set interest rate based on current balance
        if 0 <= self.balance < 1000:
            interest_rate = 0.010
        elif 1000 <= self.balance < 5000:
            interest_rate = 0.015
        else:
            interest_rate = 0.020
        
        # Add interest to the balance
        interest = self.balance * interest_rate
        self.balance += interest
        
        self.interest_applied = True                # It marks that interest has been applied
        
        # After successfully adding interest, interest_applied is set to True to prevent interest 
        # from being applied again without a subsequent deposit or withdrawal.
        
        return self.balance


# In[2]:


# First, create an account
oAccount = Account('Joe Schmoe', 1200.00, 'myPassword')
print(oAccount.getBalance('myPassword')) # should show starting balance
oAccount.addInterest()
print(oAccount.getBalance('myPassword')) # should show balance with interest
oAccount.addInterest()
print(oAccount.getBalance('myPassword'))    # output should *not* change
oAccount.addInterest()
print(oAccount.getBalance('myPassword'))    # output should *not* change




