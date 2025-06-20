def reverse(self, x: int) -> int:
    X=int(str(abs(x))[::-1])
    if x<0:
        X=X*-1
    if (-2**31)<=X<=((2**31)-1):
        return X
    return 0