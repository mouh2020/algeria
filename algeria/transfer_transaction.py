import math
from base_transaction import BaseTransaction

class TransferTransaction(BaseTransaction):
    
    def __init__(self, amount: float):
        self.amount = amount

    def calculate_fees(self) -> float:
        
        z = math.ceil(self.amount / 1000)
        
        if self.amount <= 18000:
            return z*2+18
        elif   18000 < self.amount <= 1000000 : 
            return z * 3 + 18
        elif self.amount > 1000000 :
            z = math.ceil((self.amount - 1000000) / 1000)
            return z * 6 + 3018