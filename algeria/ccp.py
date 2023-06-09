class CCP : 
    def __init__(self,ccp) : 
        self.ccp = ccp
    def get_cle(self) :
        x = self.ccp.zfill(10)
        values = list(x)
        cc = 0
        z = 9
        for i in range(4, 14):
            cc += int(values[z]) * i
            z -= 1
        ccc = str(cc % 100).zfill(2)
        return ccc