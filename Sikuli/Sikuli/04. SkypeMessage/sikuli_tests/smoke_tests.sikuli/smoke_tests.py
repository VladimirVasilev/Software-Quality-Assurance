import unittest
bdLibPath=os.path.abspath(sys.argv[0]+"..")
if not bdLibPath in sys.path: sys.path.append(bdLibPath)
from _lib import *

    
class SmokeTests(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass    
    
    def test_001_LaunchSkype(self):
       type(Key.WIN)
       click(BS.searchInputText)
       type("Skype" + Key.ENTER)

    def test_002_SendMessageToPesho(self):
        wait(BS.searchSkypeSubscriberInputText, 10)
        click(BS.searchSkypeSubscriberInputText)
        type("Pesho")
        if exists(BS.peshoSubscriber):
            type(Key.ENTER)
            rightClick(BS.peshoSubscriber)
            pass
        wait(BS.peshoHimself)
        rightClick(BS.peshoHimself)
        wait(BS.sendMessageButton, 10)
        click(BS.sendMessageButton)
        wait(BS.chatInputTextField, 10)
        click(BS.chatInputTextField)
        type("Zdravei, Peshka :)" + Key.ENTER)
        assert(exists(BS.assertImage))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SmokeTests)
    
    
    outfile = open("report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='SmokeTests Report' )
    runner.run(suite)
    outfile.close()
