#Tarini Srikanth
#Instructor: Clark Turner
#Project: Lab 7- Tests
import unittest
from strspn import *

class TestStrSpn(unittest.TestCase):
   def test_1(self):
       self.assertEqual(my_strspn("calpoly","california"),3)
   def test_2(self):
       self.assertEqual(my_strspn("calpoly","place"),4)
   def test_3(self):
       self.assertEqual(my_strspn("cccca","office"),4)
   def test_4(self):
       self.assertEqual(my_strspn("minute","simulation"),5)
       
if __name__ == '__main__':
   unittest.main()
  