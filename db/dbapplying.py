from db.dbfunc import exec_get_one, exec_get_all, exec_sql_file, exec_commit, exec_commit_return
import secrets

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
    print(allApplications)
    return allApplications

def getCompany(companyID):
    company = exec_get_one('SELECT * FROM companies WHERE id=%s', (companyID,))
    return company

def getMaterial(appID):
    materials = exec_get_one("SELECT * FROM materials WHERE appID=%s", (appID,))
    return materials

def getApp(id):
    app = exec_get_one("SELECT * FROM apps WHERE id=%s", (id,))
    return app

def getDate(appID):
    dates = exec_get_one("SELECT * FROM dates WHERE appID=%s", (appID,))
    return dates

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
        key = generateKey(exists[0])
        return ('Login Successful', key)
    return ("Login Unsuccessful", -1)

def editApplication(id, position, companyName, companyInfo, city, state, country, resume, cv, git, notes, extra, materials, applied, contact, result, deadline, appliedOn, recentContact, finalized):
    companyID = exec_get_one("SELECT companyID FROM apps WHERE id=%s", (id,))
    companyO = getCompany(companyID)
    # print("companies: ", companyO)
    if (companyO[1] != companyName) or (companyO[2] != companyInfo):
        print("Updated companies: ", exec_commit_return("UPDATE companies SET name=%s, info=%s WHERE id=%s RETURNING *", (companyName, companyInfo, companyID)))
    appO = getApp(id)
    # print('apps: ', appO)
    if (appO[2] != position) or (appO[4] != city) or (appO[5] != state) or (appO[6] != country) or (appO[7] != applied) or (appO[8] != contact) or (appO[9] != result):
        print("Updated apps: ", exec_commit_return("UPDATE apps SET position=%s, city=%s, state=%s, country=%s, applied=%s, contact=%s, result=%s WHERE id=%s RETURNING *", (position, city, state, country, applied, contact, result, id)))
    materialO = getMaterial(id)
    # print('material0', materialO)
    if (materialO[2] != resume) or (materialO[3] != cv) or (materialO[4] != git) or (materialO[5] != notes) or (materialO[6] != extra) or (materialO[7] != materials):
        print("Updated materials: ", exec_commit_return("UPDATE materials SET resume=%s, coverletter=%s, github=%s, notes=%s, extra=%s, extraMATERIAL=%s WHERE id=%s AND appID=%s RETURNING *", (resume, cv, git, notes, extra, materials, id, id)))
    datesO = getDate(id)
    # print('date:', datesO)
    if (datesO[2] != deadline) or (datesO[3] != applied) or (datesO[4] != recentContact) or (datesO[5] != finalized): 
        print("Updated dates: ", exec_commit_return("UPDATE dates SET deadline=%s, applied=%s, recent=%s, finalized=%s WHERE id=%s AND appID=%s RETURNING *", (deadline, appliedOn, recentContact, finalized, id, id)))
    edited = getApplication(id)
    return edited

def deleteApplication(id):
    deletedApp = exec_commit_return("""
        DELETE FROM apps
        WHERE id=%s RETURNING *""", (id,))
    deletedDates = exec_commit_return("""
        DELETE FROM dates
        WHERE appID=%s RETURNING *""", (id,))
    deletedMaterials = exec_commit_return("""
        DELETE FROM materials
        WHERE appID=%s RETURNING *""", (id,))
    if (deletedApp or deletedDates or deletedMaterials) == None:
        return 'Error'
    return deletedApp

def generateKey(uid):
    key = secrets.token_hex()
    generate = exec_commit_return("UPDATE users SET sessionKey=%s WHERE id=%s RETURNING *", (key, uid))
    if generate != None:
        return ("Successful Key generation", key)
    return ("Key was not generated successfully", -1)

def keyCheck(uid, key):
    existKey = exec_get_one('SELECT sessionKey FROM users WHERE id=%s', (uid,))
    if existKey == key:
        return True
    return False

def removeKey(uid):
    deleteKey = exec_commit_return("UPDATE users SET sessionKey=NULL WHERE id=%s RETURNING sessionKey", (uid,))
    if deleteKey != None:
        return 'Key removed successfully'
    return "Key was not removed"
    