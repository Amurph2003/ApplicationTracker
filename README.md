# Application Tracker

An online system that allows users to track and manage job/co-op 
applications. This system was built with Python 3.9, Angular 15.1, 
and PostgreSQL 15.1. 

# Future Feature Plans
- Implement file upload and views 
    - User should be able to upload a file (such as a resume) 
    - User should be able to view the file in the browser
    - User should be able to download the file from the browser
- Implement overall status of an application
    - User should be able to designate an application as
      Not Applied, Working On, Applied, Contacting, and Completed
    - Application background shall differ depending upon its status
    - Users should be able to sort and filter by status
- User profile
    - Users should have a profile page that allows them to see 
      and edit their data 
- User location
    - Users should be able to specify a town/city, state and zip 
      code as their home location
    - Given a home location is specified, a user should be able to
      sort applications by distance 

# Features In Progress
- Filter applications
    - Users should be able to filter applications based upon 
      criteria from each application
- Auto Sign Out
    - If a user has been inactive for 2-3 hours, user should 
      be signed out to protect user data

# How to Run
1. Ensure that the necessary technology is installed properly
    - Python (3.9 or greater)
    - Angular (15.1 or later)
    - PostgreSQL (Anything version 11 or later)
2. Setup your PostgreSQL Database by following the PostgreSQL
   Documentation. The default settings are acceptable for this 
   application, but should work with existing PostgreSQL setups
3. From the root repository, open config > server.yml and adjust 
   the following:
    - host to refelct the ip address of your PostgreSQL instance 
    - database to the name of a database within PostgreSQL
    - username to the a login username of the database
    - password to the password of the database for the login role 
      chosen
4. Run the command 'pip install -r requirements.txt' in the root 
   of the repository. This will install the libraries needed 
   for everything to run properly
5. Run the command 'python -m unittest' to run the unittests, which
   will also create the tables and load the test data
6. In the following files, adjust the URL variables to reflect the 
   ip of the machine running the python/flask backend (or it can
   be set to localhost if it's running on the same machine):
   - application.service.ts
   - auth.service.ts
   - auth.ts
   - overview.service.ts
6. In a new command prompt, navigate from the root repository to 
   angular-application-tracker and run the command 'ng serve -o' 
   to run the angular app and open it in the browser automatically
7. Click the register button and sign up for an account
8. Everything should work now. Congratulations!
