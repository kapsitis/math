'''
Created on Jun 14, 2019

@author: kalvis
'''
import unittest
from . import imo_shl_2015_n2


class Test(unittest.TestCase):


    def test_fact(self):
        a = 6
        res = imo_shl_2015_n2.fact(a)
        self.assertEqual(720,res)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_fact']
    unittest.main()