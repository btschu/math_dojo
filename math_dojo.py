class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self
    def subtract(self, num, *nums):
        self.result -= num 
        for n in nums:
            self.result -= n
        return self
# create an instance:
md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

x = md.add(2,3,5,4,2).add(1,3,1).subtract(2,2,3,2,4,5).result
print(x)

x = md.add(3,4,2,5,2).add(5,4,2,5,1).subtract(5,4,6,2,3).result
print(x)

x = md.add(4,3,5,62).add(24,35,21).subtract(23,25,32).result
print(x)
