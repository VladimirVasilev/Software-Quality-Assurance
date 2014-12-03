import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
    
    def test_001_NavigateToCapitalsDemo(self):
        RunBrowserToUrl("chrome","http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html ")
        wait(BS.label_CapitalsDemo,10)

    def test_002_DragAndDropCapitals(self):
        capitalsCount = len(BS.capitals)
        for i in xrange(capitalsCount):
            dragDrop(BS.capitals[i], BS.countries[i])
            wait(1)
            pass
        for x in xrange(len(BS.assertCapitalsCorrectImages)):
            assert(BS.assertCapitalsCorrectImages[i])
            pass    
                
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()

