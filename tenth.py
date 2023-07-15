import enum
class Colour(enum.Enum):

    RED={'UZ':'QIZIL','RU':'КРАСНЫЙ','ENG':'RED'}
    ORANGE={'UZ':'OLOV RANG',"RU":"ОРАНЖЕВЫЙ",'ENG':'ORANGE'}
    YELLOW={'UZ':'SARIQ','RU':'ЖОЛТЫЙ','ENG':'YELLOW'}


    c1=input("which colour")
    l1=input('which language')
for el in (Colour):
     print(el.name,el.value)