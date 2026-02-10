import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from physical_bypass.core import AccessControlAnalyzer,LockAnalyzer

class TestAccess(unittest.TestCase):
    def test_card(self):
        a=AccessControlAnalyzer()
        r=a.assess_card_system("HID_prox")
        self.assertEqual(r["clone_difficulty"],"Easy")
    def test_facility(self):
        a=AccessControlAnalyzer()
        r=a.assess_facility({"perimeter_fence":True,"security_cameras":True,"access_control":True})
        self.assertGreater(r["score"],0)

class TestLock(unittest.TestCase):
    def test_analyze(self):
        l=LockAnalyzer()
        r=l.analyze_lock("pin_tumbler","2")
        self.assertIn("raking",r["bypass_techniques"])

if __name__=="__main__": unittest.main()
