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

def getApplication(appID):
    application = exec_get_all('''
        SELECT apps.id, uid, position, companies.Name, companies.Info, city, state, country, materials.resume, materials.coverletter, materials.github, materials.notes, materials.extra, materials.extraMATERIAL, apps.applied, contact, result, dates.deadline, dates.applied, dates.recent, dates.finalized FROM apps 
        INNER JOIN companies ON apps.companyID=companies.id
        INNER JOIN materials ON materials.appID=apps.id
        INNER JOIN dates ON dates.appID=apps.id
        WHERE apps.id=%s''', (appID,))[0]
    return application

def newUser(name, username, email, password, date, age):
    exists = exec_get_one('SELECT username, email FROM users WHERE email=%s OR username=%s', (email, username))
    if exists != None:
        return exists
    user = exec_commit_return('''INSERT INTO users (username, hashedpw, name, email, datejoined, age) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *''', (username, password, name, email, date, age))
    return user

def newCompany(name, info):
    exists = exec_get_one("SELECT * FROM companies WHERE name=%s AND info=%s", (name, info))
    if exists != None:
        return exists
    company = exec_commit_return('INSERT INTO companies (name, info) VALUES (%s, %s) RETURNING *', (name, info))
    return company

def newApp(uid, position, company, city, state, country, applied, contact, result):
    app = exec_commit_return('INSERT INTO apps (uid, position, companyID, city, state, country, applied, contact, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *', (uid, position, company, city, state, country, applied, contact, result))
    return app

def newMaterials(appID, resume, cv, git, notes, extra, eMaterials):
    materials = exec_commit_return('INSERT INTO materials (appID, resume, coverletter, github, notes, extra, extraMATERIAL) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *', (appID, resume, cv, git, notes, extra,eMaterials))
    return materials

def newDates(appID, deadline, applied, recent, finalized):
    dates = exec_commit_return('INSERT INTO dates (appID, deadline, applied, recent, finalized) VALUES (%s, %s, %s, %s, %s) RETURNING *', (appID, deadline, applied, recent, finalized))
    return dates

def newApplication(uid, position, companyName, companyInfo, city, state, country, resume, cv, git, notes, extra, materials, applied, contact, result, deadline, appliedOn, recentContact, finalized):
    company = newCompany(companyName, companyInfo)
    companyID = company[0]
    application = newApp(uid, position, companyID, city, state, country, applied, contact, result)
    applicationID = application[0]
    material = newMaterials(applicationID, resume, cv, git, notes, extra, materials)
    dates = newDates(applicationID, deadline, appliedOn, recentContact, finalized)
    app = getApplication(applicationID)
    return app

def signin(username, password):
    exists = exec_get_one("SELECT * FROM users WHERE username=%s", (username,))
    if exists == None:
        return 'Username not found'
    gottenPW = exists[3]
    if gottenPW == password:
        return 'Login Successful'
    return "Login Unsuccessful"

def editApplication():
    edited = exec_commit_return()
    return edited

def deleteApplication():
    deleted = exec_commit_return()
    return deleted