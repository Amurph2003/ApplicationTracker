from flask_restful import Resource, reqparse, request
from db.dbapplying import *

# class Companies(Resource):
#     def get(self):
#         allCompanies = listCompanies()
#         companies = []
#         for row in allCompanies:
#             companies.append({ 'id': row[0], 'name': row[1], 'city': row[2], 'state': row[3], 'country': row[4], 'info': row[5] })
#         #     print(row)
            
#         # print('comp:', companies)
#         return companies
    
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str)
#         parser.add_argument('city', type=str)
#         parser.add_argument('state', type=str)
#         parser.add_argument('country', type=str)
#         parser.add_argument('info', type=str)
#         args = parser.parse_args()
        
#         name = args['name']
#         city = args['city']
#         state = args['state']
#         country = args['country']
#         info = args['info']
        
#         data = addCompany(name, city, state, country, info)
#         if data == None:
#             return None
#         company = {}
#         company[data[0]] = { 'name': data[1], 'city': data[2], 'state': data[3], 'country': data[4], 'notes': data[5] }
#         return company
        
#     def put(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str)
#         parser.add_argument('city', type=str)
#         parser.add_argument('state', type=str)
#         parser.add_argument('country', type=str)
#         parser.add_argument('info', type=str)
#         args = parser.parse_args()
        
#         name = args['name']
#         city = args['city']
#         state = args['state']
#         country = args['country']
#         info = args['info']
        
#         data = editCompany(name, city, state, country, info)
#         if data == None:
#             return None
#         company = {}
#         company[data[0]] = { 'name': data[1], 'city': data[2], 'state': data[3], 'country': data[4], 'notes': data[5] }
#         return company
    
#     def delete(self):
#         id = request.headers.get('id')
#         deletion = deleteCompany(id)
#         if deletion == None:
#             return None
#         company = {}
#         company[deletion[0]] = { 'name': deletion[1], 'city': deletion[2], 'state': deletion[3], 'country': deletion[4], 'notes': deletion[5] }
#         return company
    
class Applications(Resource):
    def get(self):
        allApps = listApps()
        apps = []
        for row in allApps:
            apps.append({ 'id': row[0], 'companyName': row[2], 'position': row[1], 'city': row[4], 'state': row[5], 'country': row[6], 'companyInfo': row[3], 'resume': row[7], 'coverletter': row[8], 'github': row[9], 'application notes': row[10], 'extras': row[11], 'extra materials': row[12], 'applied': row[13], 'in contact': row[14], 'result': row[15] })
        print(apps)
        return apps
        
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('position', type=str)
        parser.add_argument('company name', type=str)
        parser.add_argument('city', type=str)
        parser.add_argument('state', type=str)
        parser.add_argument('country', type=str)
        parser.add_argument('company notes', type=str)
        parser.add_argument('resume', type=str)
        parser.add_argument('coverletter', type=str)
        parser.add_argument('github', type=str)
        parser.add_argument('app notes', type=str)
        parser.add_argument('extra', type=str)
        parser.add_argument('extra materials', type=str)
        parser.add_argument('applied', type=str)
        parser.add_argument('in contact', type=str)
        parser.add_argument('result', type=str)
        args = parser.parse_args()
        
        position = args['position']
        comp_name = args['company name']
        city = args['city']
        state = args['state']
        country = args['country']
        comp_notes = args['company notes']
        resume = args['resume']
        coverletter = args['coverletter']
        github = args['github']
        app_notes = args['app notes']
        extra = args['extra']
        extra_materials = args['extra materials']
        applied = args['applied']
        contact = args['in contact']
        result = args['result']
        
        data = newApplication(position, comp_name, comp_city, comp_state, comp_country, comp_notes, resume, coverletter, github, app_notes, extra, extra_materials, applied, contact, result)
        return data
    
    def put(self):
        return 
    def delete(self):
        return