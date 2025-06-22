def intToRoman(self, num: int) -> str:
    Roman=[
    (1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),
    (100,"C"),(90,"XC"),(50,"L"),(40,"XL"),
    (10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")
    ]
    int_str=""
    for v,s in Roman:
        while(num>=v):
            num-=v
            int_str+=s
    return int_str