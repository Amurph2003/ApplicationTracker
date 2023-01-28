import datetime
import unittest
from db.dbfunc import connectToServer, exec_get_one
from db.dbapplying import *

class Tests(unittest.TestCase):
    def setUp(self):
        tableConstruction()
        loadTestData()
        
    def test_connection(self):
        connectToServer()
        result = exec_get_one('SELECT VERSION()')
        self.assertTrue(result[0].startswith('PostgreSQL'))
        
    def test_constructTables(self):
        tableConstruction()
        expected = []
        actual = exec_get_all('SELECT * FROM apps, users, dates, materials, companies')
        self.assertEqual(expected, actual)
        
    def test_loadTablesApps(self):
        exepected = 4
        actual = listApplications()
        self.assertEqual(exepected, len(actual))
        
    def test_loadTablesDates(self):
        exepected = 4
        actual = listDates()
        self.assertEqual(exepected, len(actual))
        
    def test_loadTablesUsers(self):
        expected = 2
        actual = listUsers()
        self.assertEqual(expected, len(actual))
        
    def test_loadTablesCompanies(self):
        expected = 4
        actual = listCompanies()
        self.assertEqual(expected, len(actual))
        
    def test_loadTablesMaterials(self):
        expected = 4
        actual = listMaterials()
        self.assertEqual(expected, len(actual))
        
    def test_listUsersEverything(self):
        expected = 3
        actual = listUsersEverything(1)
        self.assertEqual(expected, len(actual))
        
    def test_listUsersEverything(self):
        expected = 1
        actual = listUsersEverything(2)
        self.assertEqual(expected, len(actual))
        
    def test_getApplication(self):
        expected = (3, 1, 'Pizza Chef', 'Uno Pizzeria & Grill', '', 'Chicago', 'Illinois', 'United States', False, False, True, 'Need to customize resume', False, '', False, None, None, datetime.date(2022, 12, 24), datetime.date(2023, 1, 12), None, None)
        actual = getApplication(3)
        self.assertEqual(expected, actual)
        
    def test_newUser(self):
        expected = (3, 'unittest', 'unittestAcct', 'unit123test', 'unittest@test.unit', datetime.date(2023, 1, 27), 34)
        actual = newUser('unittest', 'unittestAcct', 'unittest@test.unit', 'unit123test', '2023-01-27', 34)
        self.assertEqual(expected, actual)
        
    def test_newApplication(self):
        expected = (5, 2, 'Student', 'Rochester Institute of Technology', 'RIT', 'Rochester', 'New York', 'United States', True, True, True, 'Software Engineering', True, 'Supplemental Essays were required', True, False, 'Accepted', datetime.date(2021, 1, 1), datetime.date(2020, 12, 21), None, datetime.date(2021, 3, 29))
        actual = newApplication(2, 'Student', 'Rochester Institute of Technology', 'RIT', 'Rochester', 'New York', 'United States', True, True, True, 'Software Engineering', True, 'Supplemental Essays were required', True, False, 'Accepted', datetime.date(2021, 1, 1), datetime.date(2020, 12, 21), None, datetime.date(2021, 3, 29))
        self.assertEqual(expected, actual)
        
    def test_signin(self): 
        expected = 'Login Successful'
        actual = signin('Test123', '123')
        self.assertEqual(expected, actual)
        
    def test_signinFail(self):
        expected = 'Login Unsuccessful'
        actual = signin('Test123', '321')
        self.assertEqual(expected, actual)
    
    