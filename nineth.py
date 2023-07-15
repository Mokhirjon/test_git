import enum
class day_of_week(enum.Enum):
    mon="monday"
    tus="thusdaay"
    wen="wendsday"
    thirs="thirsday"
    fri="Friday"
    sat="saturday"
    sun="sunday"
print(day_of_week.mon.value)