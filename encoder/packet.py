class Packet():
    codes = {
        "mycode": "11",
        "basic": "00"
    }
    def __init__(self):
        self.HEADER = "1010"
    def pack(self, mess: str, code: str) -> str:
        result = ""
        result += self.HEADER
        result += self.codes[code]
        result += mess
        return result
        
