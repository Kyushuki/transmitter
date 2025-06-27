class DePacket():
    codes = {
        "11": "mycode",
        "00": "basic"
    }

    def __init__(self):
        self.HEADER = "1010"

    def depacket(self, mess: str) -> tuple:
        res = ""
        code = ""
        if mess[0:4] == self.HEADER:
            res = mess[4:]
            code = res[0:2]
            res = res[2:]
            return res, self.codes[code]
        # return mess[6:], "basic"
        pass
