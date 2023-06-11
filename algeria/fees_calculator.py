import math
from transfer_transaction import TransferTransaction
from checkout_transaction import CheckoutTransaction

class FeesCalculator: 

    def __init__(self,amount : float): 
        self.amount = amount
            
    def calculate_deposit_fees(self) -> float: 
        # Return the fees of a a deposit
        transfer_transaction = TransferTransaction(self.amount)
        return transfer_transaction.calculate_fees()
    
    def calculate_checkout_fees(self) -> float: 
        # Return the fees of a cheeckout by che
        checkout_transaction = CheckoutTransaction(self.amount)
        return checkout_transaction.calculate_fees()