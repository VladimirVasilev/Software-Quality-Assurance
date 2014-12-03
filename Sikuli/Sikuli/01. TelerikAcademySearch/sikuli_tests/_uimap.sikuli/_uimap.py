########################################################
# UI map for XYZ
########################################################
from sikuli import *
########################################################

class BS:
    inputTextWithButtons = "1414932773994.png"
    inputTextSearch = Pattern("1414932773994.png").targetOffset(-115,-21)
    expectedResultVisited = "1414934026361.png"
    expectedResultUnvisited = "1414934422883.png"