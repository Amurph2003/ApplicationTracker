from db.dbfunc import exec_get_one, exec_get_all, exec_sql_file, exec_commit, exec_commit_return

def tableConstruction():
    exec_sql_file('applicationtracker/db/tables.sql')

def loadTestData():
    exec_sql_file('applicationtracker/tests/testdata.sql')

def listApplications():
    allApps = exec_get_all("""SELECT * FROM apps""")
    return allApps

def listCompanies():
    allCompanies = exec_get_all("""SELECT * FROM companies""")
    return allCompanies

def listDates():
    allDates = exec_get_all("""SELECT * FROM dates""")
    return allDates

def listMaterials():
    allMaterials = exec_get_all("""SELECT * FROM materials""")
    return allMaterials

def listUsers():
    allUsers = exec_get_all("""SELECT * FROM users""")
    return allUsers


def listUsersEverything(uid):
    allApplications = exec_get_all("""SELECT * FROM apps
        INNER JOIN companies ON apps.companyID=companies.id
        INNER JOIN materials ON materials.appID=apps.id
        INNER JOIN dates ON dates.appID=apps.id
        WHERE uid=%s""", (uid,))
    return allApplications

def newUser():
    user = exec_commit_return()
    return user

def newApplication():
    app = exec_commit_return()
    return app

def signin():
    signin = 0
    return signin

def editApplication():
    edited = exec_commit_return()
    return edited

def deleteApplication():
    deleted = exec_commit_return()
    return deleted