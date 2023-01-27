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