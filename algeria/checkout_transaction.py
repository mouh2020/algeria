import math
from base_transaction import BaseTransaction

class CheckoutTransaction(BaseTransaction):

    def __init__(self, amount: float):
        self.amount = amount

    def calculate_fees(self) -> float:
        return (math.ceil(self.amount/5000)) * 12 + 18

        
