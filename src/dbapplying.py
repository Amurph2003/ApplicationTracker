from src.dbfunc import exec_get_one, exec_get_all, exec_sql_file, exec_commit

def tableConstruction():
    exec_sql_file('applicationtracker/src/tables.sql')

def loadTestData():
    exec_sql_file('applicationtracker/tests/testdata.sql')