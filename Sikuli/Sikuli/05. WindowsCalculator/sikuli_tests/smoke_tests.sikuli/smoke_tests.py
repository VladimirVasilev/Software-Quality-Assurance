import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
    
    def test_001_LaunchWindowsCalculator(self):
       type("d",KEY_WIN)
       type(Key.WIN)
       click(BS.searchInputText)
       type("Calculator" + Key.ENTER)

    def test_002_ToggleCalculatorToStandardMode(self):
       #type(N, KeyModifier.ALT)
       wait(BS.standardCalculatorKeys, 10)

    def test_003_VerifyAddition(self):
        click(BS.allDigits[5])
        wait(0.5)
        click(BS.arithmeticSigns[0])
        wait(0.5)
        click(BS.allDigits[7])
        wait(0.5)
        click(BS.arithmeticSigns[5])
        assert(exists(BS.resultTwelve))

    def test_004_VerifySubtraction(self):
        click(BS.clearAllButton)
        click(BS.allDigits[5])
        wait(0.5)
        click(BS.arithmeticSigns[1])
        wait(0.5)
        click(BS.allDigits[2])
        wait(0.5)
        click(BS.arithmeticSigns[5])
        assert(exists(BS.resultThree))

    def test_005_VerifyMultiplication(self):
        click(BS.clearAllButton)
        click(BS.allDigits[3])
        wait(0.5)
        click(BS.arithmeticSigns[2])
        wait(0.5)
        click(BS.allDigits[4])
        wait(0.5)
        click(BS.arithmeticSigns[5])
        assert(exists(BS.resultTwelve))

    def test_006_VerifyDivision(self):
        click(BS.clearAllButton)
        click(BS.allDigits[1])
        wait(0.5)
        click(BS.allDigits[2])
        wait(0.5)
        click(BS.arithmeticSigns[3])
        wait(0.5)
        click(BS.allDigits[4])
        wait(0.5)
        click(BS.arithmeticSigns[5])
        assert(exists(BS.resultThree))
   
    def test_007_CloseWindowsCalculator(self):
        click(BS.buttonClose)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()
