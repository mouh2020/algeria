class CCP : 
    def __init__(self,ccp : str) : 
        self.ccp = ccp
    def get_cle(self) :
        # Return the cle of the account
        x = self.ccp.zfill(10)
        values = list(x)
        cc = 0
        z = 9
        for i in range(4, 14):
            cc += int(values[z]) * i
            z -= 1
        ccc = str(cc % 100).zfill(2)
        return ccc
    def get_rip(self,only_cle=None) : 
        # Return the rip of the account including the first 8 digits 00799999
        self.ccp = int(self.ccp)
        if ((self.ccp * 100) % 97) + 85 > 97:
            x = 97 - (((self.ccp * 100) % 97) + 85 - 97)
            if x < 10:
                return "00799999"+ str(self.ccp).zfill(10) + str(x) if not(only_cle) else str(x)
            else:
                return "00799999"+ str(self.ccp).zfill(10) + str(x) if not(only_cle) else str(x)
        else:
            y = 97 - (((self.ccp * 100) % 97) + 85)
            if y < 10:
                return "00799999"+ str(self.ccp).zfill(10) + str(y) if not(only_cle) else str(y)
            else:
                return "00799999"+ str(self.ccp).zfill(10) + str(y)if not(only_cle) else str(y)
    def get_rip_cle(self) : 
        # Return only the cle of the rip 
        return self.get_rip(only_cle=True)