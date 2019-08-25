'''
Created on Jun 27, 2019

@author: kalvis
'''
import unittest
import re
from analysis import sync_tasks

class Test(unittest.TestCase):


    def test_escape1(self):
        arg = 'aaa a<c ccc'
        res = sync_tasks.escape_math(arg)
        self.assertEqual(res, 
                         'aaa a&lt;c ccc', 
                         'Inequality not replaced')

    def test_escape2(self):
        arg = 'Atvērt iekavas izteiksmēs (a+b)^n un (a-b)^n'
        res = sync_tasks.escape_math(arg)
        self.assertEqual(res, 
                         'Atvērt iekavas izteiksmēs $(a+b)^n$ un $(a-b)^n$', 
                         'Power not replaced')

#    def test_escape3(self):
#        arg = '(a+b)^n un (a-b)^n'
#        self.assertEqual(
#            re.sub('\(a\+b\)\^n','XXX', arg), 
#            '(a+b)^n un (a-b)^n', 'Message')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_escape1']
    unittest.main()