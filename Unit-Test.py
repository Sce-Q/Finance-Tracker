import unittest
import os
import json
from FinanceTracker import FinanceTracker

class TestFinanceTracker(unittest.TestCase):

    def setUp(self):
        self.filepath = "test_expenses.json"
        self.tracker = FinanceTracker(self.filepath)

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def test_load_expense_history(self):
        self.assertEqual(self.tracker.users, {})

        with open(self.filepath, 'w') as file:
            json.dump({'users': {'user1': {'expenses': []}}}, file)
        self.tracker = FinanceTracker(self.filepath)
        self.assertEqual(self.tracker.users, {'user1': {'expenses': []}})

        with open(self.filepath, 'w') as file:
            file.write("Invalid JSON")
        self.tracker = FinanceTracker(self.filepath)
        self.assertEqual(self.tracker.users, {})

    def test_add_user(self):
        self.tracker.add_user('user1')
        self.assertIn('user1', self.tracker.users)
        self.tracker.add_user('user1')
        self.assertIn('user1', self.tracker.users)

    def test_add_expense(self):
        self.tracker.add_user('user1')
        self.tracker.add_expense(10.0, 'Test expense', 'user1')
        self.assertEqual(len(self.tracker.users['user1']['expenses']), 1)

    def test_remove_expense(self):
        self.tracker.add_user('user1')
        self.tracker.add_expense(10.0, 'Test expense', 'user1')
        self.tracker.remove_expense(0, 'user1')
        self.assertEqual(len(self.tracker.users['user1']['expenses']), 0)

    def test_print_expense_history(self):
        self.tracker.add_user('user1')
        self.tracker.add_expense(10.0, 'Test expense', 'user1')
        self.tracker.print_expense_history('user1')

    def test_save_expense_history(self):
        self.tracker.add_user('user1')
        self.tracker.add_expense(10.0, 'Test expense', 'user1')
        self.tracker.save_expense_history()
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            self.assertIn('users', data)
            self.assertIn('user1', data['users'])
            self.assertIn('expenses', data['users']['user1'])
            self.assertEqual(len(data['users']['user1']['expenses']), 1)

if __name__ == "__main__":
    unittest.main()