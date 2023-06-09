class CCP:
    def __init__(self, ccp: str):
        self.ccp = ccp

    def get_cle(self):
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

    def __calculate_rip(self, x):
        # Calculate the rip based on the given value x
        if x < 10:
            return "00799999" + str(self.ccp).zfill(10) + str(x)
        else:
            return "00799999" + str(self.ccp).zfill(10) + str(x)

    def get_rip(self, only_cle=None):
        # Calculate and return the rip of the account
        self.ccp = int(self.ccp)
        remainder = (self.ccp * 100) % 97
        if remainder + 85 > 97:
            x = 97 - (remainder + 85 - 97)
        else:
            x = 97 - (remainder + 85)

        return self.__calculate_rip(x) if not only_cle else str(x)

    def get_rip_cle(self):
        # Return only the cle of the rip
        return self.get_rip(only_cle=True).zfill(2)
