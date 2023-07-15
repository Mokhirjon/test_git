class kompyuter:
    def __init__(self,name,price,rame,processor):
        self.name=name
        self.price=price
        self.rame=rame
        self.processor=processor
class HP(kompyuter):
    def __init__(self, name='HP', price="1k$", rame='Rame', processor='Processor'):
        self.name = name
        self.price = price
        self.rame = rame
        self.processor = processor
class apple(kompyuter):
    def __init__(self, name='ACer', price="2k$", rame='Rame', processor="processor"):
        self.name = name
        self.price = price
        self.rame = rame
        self.processor = processor
class zet(kompyuter):
    def __init__(self, name='Zet', price="900$", rame='Rame', processor="processor"):
        self.name = name
        self.price = price
        self.rame = rame
        self.processor = processor
if kompyuter.__name__=='A':
    print(kompyuter.name)
else:
    print('Nothing')