from math import comb
def countGoodArrays(self, n: int, m: int, k: int) -> int:
    nums_chuck=n-k
    nums_connect=comb(n-1,k)
    one_connect_how_many_times=m*((m-1)**(nums_chuck-1))
    allGoodArrays=nums_connect*one_connect_how_many_times
    MOD=10**9+7
    return allGoodArrays%MOD