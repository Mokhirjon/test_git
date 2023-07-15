class pirson:
    def __init__(self,number:int):
        self.number=number
    def pink(self):
        count=1

        for i in range(1, self.number+1):
         count =count*i

obj = pirson(number=12)
print (obj.number)
