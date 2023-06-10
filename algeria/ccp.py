import math
class CCP:
    def __init__(self, ccp: str):
        self.ccp = ccp

    def get_cle(self) -> str:
        # Calculate and return the cle of the account
        x = self.ccp.zfill(10)
        values = list(x)
        cc = 0
        z = 9
        for i in range(4, 14):
            cc += int(values[z]) * i
            z -= 1
        ccc = str(cc % 100).zfill(2)
        return ccc

    def __calculate_rip(self) :
        # Calculate the rip based on the given value x
        self.ccp = int(self.ccp)
        remainder = (self.ccp * 100) % 97
        if remainder + 85 > 97:
            x = 97 - (remainder + 85 - 97)
        else:
            x = 97 - (remainder + 85)
        return "00799999" + str(self.ccp).zfill(10) + str(x)

    def get_rip(self, only_cle=None) -> str :
        # Calculate and return the rip of the account
        rip = self.__calculate_rip()
        return rip if not only_cle else rip[-2:]
  
    def get_rip_cle(self)-> str : 
        # Return only the cle of the rip 
        return self.get_rip(only_cle=True).zfill(2)

class Transaction : 
    def __init__(self,amount : float) : 
        self.amount = amount

    def __calculate_fees(self,mode) : 
        if mode == "transfer" : 
            return (math.ceil(self.amount/5000)) * 12 + 18
        elif mode == "checkout" : 
            z = math.ceil(self.amount / 1000)
            if self.amount <= 18000:
                return z*2+18
            elif   18000 < self.amount <= 1000000 : 
                return z * 3 + 18
            elif self.amount > 1000000 :
                z = math.ceil((self.amount - 1000000) / 1000)
                return z * 6 + 3018
            
    def get_deposit_fees(self) -> float: 
        # Return the fees of a a deposit
        return self.__calculate_fees(mode="transfer")
    
    def get_checkout_fees(self) -> float: 
        # Return the fees of a cheeckout by che
        return self.__calculate_fees(mode="checkout")


    



