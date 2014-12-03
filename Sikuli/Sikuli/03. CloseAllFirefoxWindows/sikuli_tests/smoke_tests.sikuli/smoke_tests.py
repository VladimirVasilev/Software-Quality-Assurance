import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
    
    def test_001_OpenFirefoxThreeTimes(self):
        for x in xrange(3):
            RunBrowserToUrl("firefox","http://google.com")
            wait(BS.mainButtonsFirefox, 10)
            pass

    def test_002_CloseAllFirefoxWindows(self):
        while exists(BS.mainButtonsFirefox):
            click(BS.closeButtonsFirefox)
            if exists(BS.firefoxIcon):
                click(BS.firefoxIcon)
                if exists(BS.minimizedFirefoxWindow):
                    click(BS.minimizedFirefoxWindow)
                    pass                
                pass
            pass            

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()
