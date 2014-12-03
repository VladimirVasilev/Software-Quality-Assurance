########################################################
# UI map for XYZ
########################################################
from sikuli import *
########################################################

class BS:
    searchInputText = "1414952167486.png"
    standardCalculatorKeys = "1414953142793.png"
    arithmeticSigns = [Pattern("1414954457688.png").exact(), "1414954663563.png","1414954898954.png", Pattern("1414955135234.png").exact(), "1414955484395.png", "1414955523246.png"]
    allDigits = ["1414955165325.png", "1414955182361.png", "1414955195079.png", "1414955208111.png", "1414955231309.png", "1414955403569.png", "1414955417610.png", "1414955427140.png", "1414955438472.png", "1414955460344.png"]
    clearAllButton = "1414957217732.png"
    resultTwelve = "1414956729334.png"
    resultThree = "1414957308668.png"
    buttonClose = Pattern("1414958356768.png").targetOffset(34,-29)
    