class Solution:
    def intToRoman(self, num: int) -> str:
        list_R=[]
        Roman={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M",4:"IV",9:"IX",40:"XL",90:"XC",400:"CD",900:"CM"}
        k=num//1000
        num=num%1000
        h=num//100
        num=num%100
        t=num//10
        num=num%10
        for i in range(k):
            list_R.append("M")
            if h==400:
                list_R.append("M")

        