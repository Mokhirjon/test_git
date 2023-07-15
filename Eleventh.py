import enum
class Villages(enum.Enum):
    TASHKENT="T"
    BUXORO="B"
    ANDIJON="A"
    SAMARQAND="S"
    XORAZM="X"
    SURXANDARYO="S2"
    QASHQADARYO="Q"
    SIRDARYO="S3"
    JIZZAH="J"
    NAVOIY="N"
    NAMANGAN='N2'
    FARGONA='F'
print(Villages.TASHKENT.value)