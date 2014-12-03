import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
    
    def test_001_NavigateToTap(self):
        RunBrowserToUrl("chrome","http://www.google.com")
        wait(BS.inputTextWithButtons,30)
        type(BS.inputTextSearch, "Telerik academy")
        type(Key.ENTER)
        wait((BS.expectedResultVisited or BS.expectedResultUnvisited),10)
             
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()

