from db.dbfunc import exec_get_one, exec_get_all, exec_sql_file, exec_commit, exec_commit_return

def tableConstruction():
    exec_sql_file('applicationtracker/db/tables.sql')

def loadTestData():
    exec_sql_file('applicationtracker/tests/testdata.sql')

def listApps():
    allApps = exec_get_all("""
        SELECT * FROM apps"""
    )
    # print(allApps)
    return allApps

# def listCompanies(search=""):
#     if search == "":
#         allCompanies = exec_get_all(
#             """SELECT * FROM companies"""
#         )
#         return allCompanies
#     else:
#         query = '%' + search + '%'
#         searchedCompanies = exec_get_all(
#             """SELECT * FROM companies WHERE name LIKE %s""", (query)
#         )
#         return searchedCompanies

# def addCompany(name, city, state, country, info):
#     exist = exec_get_one('SELECT * FROM companies WHERE name=%s AND city=%s AND state=%s AND country=%s AND info=%s', (name, city, state, country, info))
#     if exist != None:
#         return None
#     company = exec_commit_return('''INSERT INTO companies (name, city, state, country, info) VALUES (%s,%s,%s, %s, %s) RETURNING *''', (name, city, state, country, info))
#     return company

# def editCompany(id, name='', city='', state='', country='', info=''):
#     exists = exec_get_one('SELECT * FROM companies WHERE id=%s RETURNING *', (id, ))
#     if exists == None:
#         return None
#     id = exists[0]
#     if city:
#         exec_commit('UPDATE companies SET city=%s WHERE id=%s', (city, id))
#     if state:
#         exec_commit('UPDATE companies SET state=%s WHERE id=%s', (state, id))
#     if country:
#         exec_commit('UPDATE companies SET country=%s WHERE id=%s', (country, id))
#     if info:
#         exec_commit('UPDATE companies SET info=%s WHERE id=%s', (info, id))
#     updated = exec_get_one('SELECT * FROM companies WHERE id=%s', (id,))
#     if updated == None:
#         return None
#     return updated

# def deleteCompany(id):
#     exists = exec_get_one('SELECT * FROM companies WHERE id=%s RETURNING *', (id, ))
#     if exists == None:
#         return None
#     id = exists[0]
#     deleted = exec_commit_return('DELETE FROM companies WHERE id=%s RETURNING *', (id,))
#     return deleted

def newApplication(position, comp_name, comp_city, comp_state, comp_country, comp_notes, resume, coverletter, github, app_notes, extra, extra_material, applied, contact, result):
    newAppComp = addCompany(comp_name, comp_city, comp_state, comp_country,comp_notes)
    if newAppComp == None:
        return 'Company not created'
    comp_id = newAppComp[0]
    print(comp_id)
    newApp = exec_commit_return(
        """INSERT INTO apps (position, company_id, resume, coverletter, github, notes, extra, extra_material, applied, in_contact, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *""", (position, comp_id, resume, coverletter, github, app_notes, extra, extra_material, applied, contact, result)
    )
    return newApp