import unittest
from db.dbfunc import connectToServer, exec_get_one
from db.dbapplying import *

class Tests(unittest.TestCase):
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
        tableConstruction()
        loadTestData()
        exepected = 3
        actual = exec_get_all('SELECT * FROM apps')
        self.assertEqual(exepected, len(actual))
        
    def test_loadTablesDates(self):
        tableConstruction()
        loadTestData()
        exepected = 3
        actual = exec_get_all('SELECT * FROM dates')
        self.assertEqual(exepected, len(actual))
        
    def test_loadTablesUsers(self):
        tableConstruction()
        loadTestData()
        expected = 1
        actual = exec_get_all("SELECT * FROM users")
        self.assertEqual(expected, len(actual))
        
    def test_loadTablesCompanies(self):
        tableConstruction()
        loadTestData()
        expected = 3
        actual = exec_get_all("SELECT * FROM companies")
        self.assertEqual(expected, len(actual))
        
    def test_loadTablesMaterials(self):
        tableConstruction()
        loadTestData()
        expected = 3
        actual = exec_get_all("SELECT * FROM materials")
        self.assertEqual(expected, len(actual))