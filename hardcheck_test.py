import unittest
from hardcheck import cpuOverUsage
from hardcheck import diskOverUsage

class TestHardCheck(unittest.TestCase):

    def test_cpu(self):
        isOver,message=cpuOverUsage()
        self.assertIsInstance(isOver,bool)
        self.assertIsInstance(message,str)


    def test_disk(self):
        isOver,message=diskOverUsage('./')
        self.assertIsInstance(isOver,bool)
        self.assertIsInstance(message,str)


    def test_invalid_path(self):
        self.assertRaises(ValueError,diskOverUsage,'')

        
unittest.main()