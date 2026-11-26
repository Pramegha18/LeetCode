class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num1 = num//10
            num2 = num % 10
            total = num1 + num2
            num = total

        return num    


        