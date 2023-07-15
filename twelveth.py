class Car():
    def __init__(self,name ,colour,year,brend):
        self.name=name
        self.colour=colour
        self.year=year
        self.brend=brend
    def __str__(self):
        super().__str__(name='Supra',colour="orange",year=1998)
l=['qwerty',324,'qadw']
i=0

for x,y in enumerate(l):
    print(x,y)