from flask_restful import Resource, reqparse, request
from db.dbapplying import *

class Application(Resource):
    def get(self, uid):
        key = request.headers.get('key')
        appID = request.headers.get('appID')
        applicationData = getApplication(appID, uid, key)
        for item in applicationData:
            print(item)
            applicationsForUser = {'appId': item[0], 'uid': item[1], 'position': item[2], 'companyName': item[3], 'companyNotes': item[4], 'city': item[5], 'state': item[6], 'country': item[7], 'resume': item[8], 'coverletter': item[9], 'github': item[10], 'appNotes': item[11], 'extras': item[12], 'materials': item[13], 'applied': item[14], 'contact': item[15], 'result': item[16], 'deadline': str(item[17]), 'appliedOn': str(item[18]), 'recentCommunication': str(item[19]), 'finalizedDate': str(item[20])}
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
        
        key = request.headers.get('key')
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
        
        newApplicationData = newApplication(uid, key, position, companyName, companyInfo, city, state, country, resume, cv, git, notes, extras, materials, applied, contact, result, deadline, appliedOn, recent, finalized)
        
        print('New Application:', newApplicationData)
        if newApplicationData == None:
            return None
        item = newApplicationData[0]
        newA = {'appId': item[0], 'uid': item[1], 'position': item[2], 'companyName': item[3], 'companyNotes': item[4], 'city': item[5], 'state': item[6], 'country': item[7], 'resume': item[8], 'coverletter': item[9], 'github': item[10], 'appNotes': item[11], 'extras': item[12], 'materials': item[13], 'applied': item[14], 'contact': item[15], 'result': item[16], 'deadline': str(item[17]), 'appliedOn': str(item[18]), 'recentCommunication': str(item[19]), 'finalizedDate': str(item[20])}
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
        
        key = request.headers.get('key')
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
            
        # gottenID = exec_get_one('SELECT id FROM apps WHERE uid=%s AND id=%s', (uid, id))[0]
        # if gottenID != id:
        #     return None
        editedApplication = editApplication(key, uid, id, position, companyName, companyInfo, city, state, country, resume, cv, git, notes, extras, materials, applied, contact, result, deadline, appliedOn, recent, finalized)[0]
        
        editA = {}
        item = editedApplication
        editA = {'appId': item[0], 'uid': item[1], 'position': item[2], 'companyName': item[3], 'companyNotes': item[4], 'city': item[5], 'state': item[6], 'country': item[7], 'resume': item[8], 'coverletter': item[9], 'github': item[10], 'appNotes': item[11], 'extras': item[12], 'materials': item[13], 'applied': item[14], 'contact': item[15], 'result': item[16], 'deadline': str(item[17]), 'appliedOn': str(item[18]), 'recentCommunication': str(item[19]), 'finalizedDate': str(item[20])}
        
        return editA
    
    def delete(self, uid):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        args = parser.parse_args()
        id = args['id']
        key = request.headers.get('key')
        
        gottenUID = exec_get_one('SELECT uid FROM apps WHERE id=%s', (id,))[0]
        if gottenUID == uid:
            deleted = deleteApplication(key, uid, id)
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
    
class Overview(Resource):
    def get(self, uid):
        key = request.headers.get('key')
        allApplications = listUsersEverything(uid, key)
        applicationsForUser = []
        print(allApplications)
        for item in allApplications:
            applicationsForUser.append({'appID': item[0], 'uid': item[1], 'position': item[2], 'companyId': item[3], 'city': item[4], 'state': item[5], 'country': item[6], 'applied': item[7], 'contact': item[8], 'result': item[9], 'companyName': item[11], 'companyInfo': item[12], 'resume': item[15], 'coverletter': item[16], 'github': item[17], 'applicationNotes': item[18], 'extraMaterials': item[19], 'materialsSubmitted': item[20],'deadline': str(item[23]), 'appliedOn': str(item[24]), 'recentCommunication': str(item[25]), 'finalizedDate': str(item[26])})
        return applicationsForUser
    
class Users(Resource):
    def get(self, uid):
        key = request.headers.get('key')
        result = keyCheck(uid, key)
        
        return {'result': result}
        