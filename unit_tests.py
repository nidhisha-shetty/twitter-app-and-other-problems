from problem_1_chats_solution  import most_active_users
from problem_3_strings_solution import can_create
import unittest

class TestProblems(unittest.TestCase):

    def test_can_create(self):
        self.assertEqual(can_create(['back','end','front','tree'],'backend'), True)
        self.assertEqual(can_create(['back','end','front','tree'],'frontyard'), False)
        self.assertEqual(can_create(['back','end','front','tree'],'frontend'), True)

    def test_most_active_users(self):
    	self.assertEqual(most_active_users(), ['John', 'Ram', 'Adam'])

if __name__ == '__main__':
    unittest.main()