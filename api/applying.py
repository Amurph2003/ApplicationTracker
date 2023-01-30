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
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=str)
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
        parser.add_argument('deadline', type=str)
        parser.add_argument('appliedOn', type=str)
        parser.add_argument('recent', type=str)
        parser.add_argument('finalized', type=str)
        args = parser.parse_args()
        
        uid = args['uid']
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
        
        newApplicationData = newApplication(uid, position, companyName, companyInfo, city, state, country, resume, cv, git, notes, extras, materials, applied, contact, result, deadline, appliedOn, recent, finalized)
        
        print('New Application:', newApplicationData)
        if newApplicationData == None:
            return None
        return newApplicationData