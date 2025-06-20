def isNumber(self, s: str) -> bool:
    Error=["inf","+inf","-inf","infinity","+infinity","-infinity","nan","+nan","-nan"]
    try:
        x=float(s)
        if s.lower() in Error:
            return False
        return True
    except ValueError:
        return False