'''
Created on 22/11/2012

@author: Andreas M
'''
import unittest

import Plusandminus

class Test(unittest.TestCase):


    def testplus(self):
        Plusandminus.plus(2, 1)
        self.assertEqual(3, Plusandminus.plus(2,1), "error")
        pass
    
    def testminus(self):
        Plusandminus.minus(2,1)
        self.assertEqual(1, Plusandminus.minus(2,1), "error")
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()