from flask_restful import Resource, reqparse, request
from db.dbapplying import *

class Applications(Resource):
    def get(self, uid):
        applicationData = listUsersEverything(uid)
        applicationsForUser = {}
        for item in applicationData:
            print(item)
            applicationsForUser[item[0]] = { 'User ID': item[1], 'Position': item[2], 'Company ID': item[3], 'City': item[4], 'State': item[5], 'Country': item[6], 'Applied': item[7], 'Contact': item[8], 'Result': item[9], 'Company ID': item[10], 'Company Name': item[11], 'Company Info': item[12], 'Materials ID': item[13], 'App ID (materials)': item[14], 'Resume': item[15], 'Cover letter': item[16], 'Github': item[17], 'Application Notes': item[18], 'Extra materials?': item[19], 'Extra materials submitted': item[20], 'Dates ID': item[21], 'App ID (dates)': item[22], 'Deadline': str(item[23]), 'Applied On': str(item[24]), 'Recent Communication': str(item[25]), 'Finalized Date': str(item[26]) }        
        return applicationsForUser
    
    def post(self, uid):
        parser = reqparse.RequestParser()
        parser.add_argument('position', type=str)
        parser.add_argument('companyName', type=str)
        parser.add_argument('companyInfo', type=str)
        parser.add_argument('city', type=str)
        parser.add_argument('state', type=str)
        parser.add_argument('country', type=str)
        parser.add_argument('resume', type=str)
        parser.add_argument('cv', type=str)
        parser.add_argument('git', type=str)
        parser.add_argument('notes', type=str)
        parser.add_argument('extras', type=str)
        parser.add_argument('materials', type=str)
        parser.add_argument('applied', type=str)
        parser.add_argument('contact', type=str)
        parser.add_argument('result', type=str)
        parser.add_argument('deadline')
        parser.add_argument('appliedOn')
        parser.add_argument('recent')
        parser.add_argument('finalized')
        args = parser.parse_args()
        
        position = args['position']
        companyName = args['companyName']
        companyInfo = args['companyInfo']
        city = args['city']
        state = args['state']
        country = args['country']
        resume = args['resume']
        cv = args['cv']
        git = args['git']
        notes = args['notes']
        extras = args['extras']
        materials = args['materials']
        applied = args['applied']
        contact = args['contact']
        result = args['result']
        deadline = args['deadline']
        appliedOn = args['appliedOn']
        recent = args['recent']
        finalized = args['finalized']
        
        if deadline == '':
            deadline = None
        if appliedOn == '':
            appliedOn = None
        if recent == '':
            recent = None
        if finalized == '':
            finalized = None
        
        newApplicationData = newApplication(uid, position, companyName, companyInfo, city, state, country, resume, cv, git, notes, extras, materials, applied, contact, result, deadline, appliedOn, recent, finalized)
        
        print('New Application:', newApplicationData)
        if newApplicationData == None:
            return None
        newA = {}
        item = newApplicationData
        newA[item[0]] = { 'User ID': item[1], 'Position': item[2], 'City': item[3], 'State': item[4], 'Country': item[5], 'Applied': item[6], 'Contact': item[7], 'Result': item[8], 'Company Name': item[9], 'Company Info': item[10],  'Resume': item[11], 'Cover letter': item[12], 'Github': item[13], 'Application Notes': item[14], 'Extra materials?': item[15], 'Extra materials submitted': item[16], 'Deadline': str(item[17]), 'Applied On': str(item[18]), 'Recent Communication': str(item[19]), 'Finalized Date': str(item[20]) }
        return newA
    
    def put(self, uid):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('position', type=str)
        parser.add_argument('companyName', type=str)
        parser.add_argument('companyInfo', type=str)
        parser.add_argument('city', type=str)
        parser.add_argument('state', type=str)
        parser.add_argument('country', type=str)
        parser.add_argument('resume', type=str)
        parser.add_argument('cv', type=str)
        parser.add_argument('git', type=str)
        parser.add_argument('notes', type=str)
        parser.add_argument('extras', type=str)
        parser.add_argument('materials', type=str)
        parser.add_argument('applied', type=str)
        parser.add_argument('contact', type=str)
        parser.add_argument('result', type=str)
        parser.add_argument('deadline')
        parser.add_argument('appliedOn')
        parser.add_argument('recent')
        parser.add_argument('finalized')
        args = parser.parse_args()
        
        id = args['id']
        position = args['position']
        companyName = args['companyName']
        companyInfo = args['companyInfo']
        city = args['city']
        state = args['state']
        country = args['country']
        resume = args['resume']
        cv = args['cv']
        git = args['git']
        notes = args['notes']
        extras = args['extras']
        materials = args['materials']
        applied = args['applied']
        contact = args['contact']
        result = args['result']
        deadline = args['deadline']
        appliedOn = args['appliedOn']
        recent = args['recent']
        finalized = args['finalized']
        
        if deadline == '':
            deadline = None
        if appliedOn == '':
            appliedOn = None
        if recent == '':
            recent = None
        if finalized == '':
            finalized = None
        
        editedApplication = editApplication(id, position, companyName, companyInfo, city, state, country, resume, cv, git, notes, extras, materials, applied, contact, result, deadline, appliedOn, recent, finalized)
        
        print('Edited Application:', editedApplication)
        if editedApplication == None:
            return None
        editA = {}
        item = editedApplication
        editA[item[0]] = { 'User ID': item[1], 'Position': item[2], 'City': item[3], 'State': item[4], 'Country': item[5], 'Applied': item[6], 'Contact': item[7], 'Result': item[8], 'Company Name': item[9], 'Company Info': item[10],  'Resume': item[11], 'Cover letter': item[12], 'Github': item[13], 'Application Notes': item[14], 'Extra materials?': item[15], 'Extra materials submitted': item[16], 'Deadline': str(item[17]), 'Applied On': str(item[18]), 'Recent Communication': str(item[19]), 'Finalized Date': str(item[20]) }
        return editA
    
    def delete(self, uid):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        args = parser.parse_args()
        id = args['id']
        
        gottenUID = exec_get_one('SELECT uid FROM apps WHERE id=%s', (id,))[0]
        if gottenUID == uid:
            deleted = deleteApplication(id)
            return deleted
        return 'Not able to delete'
    
class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        un = args['username']
        pw = args['password']
        result = signin(un, pw)
        print(result)
        return result