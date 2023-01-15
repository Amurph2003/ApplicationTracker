from src.dbfunc import exec_get_one, exec_get_all, exec_sql_file, exec_commit

def tableConstruction():
    exec_sql_file('applicationtracker/src/tables.sql')

def loadTestData():
    exec_sql_file('applicationtracker/tests/testdata.sql')

def listApps():
    allApps = exec_get_all("""
        SELECT * FROM apps"""
    )
    return allApps

def listCompanies(search=""):
    if search == "":
        allCompanies = exec_get_all(
            """SELECT * FROM companies"""
        )
        return allCompanies
    else:
        query = '%' + search + '%'
        searchedCompanies = exec_get_all(
            """SELECT * FROM companies WHERE name LIKE %s""", (query)
        )
        return searchedCompanies

