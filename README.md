# Application Tracker

Application Tracker is an web-based system that allows users to manage
and track job applications in an organized manner. It utilizes a Python 
backend to communicate with a PostgreSQL database and displays the data
in an Angular application. 

# Features In Development
- Filter applications
    - Users should be able to filter applications based upon 
      criteria from each application
- Auto Sign Out
    - If a user has been inactive for 2-3 hours, user should 
      be signed out to protect user data

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

# Long Term Feature Plans
- Notifications
    - Users should be notified if an application deadline is 
      approaching and they have not yet applied
    - Users should be notified if they haven't updated any 
      communications after a week with each application
- Mobile Companion App(s)

# How to Run
1. Ensure that the necessary technology is installed properly
    - Python (3.9 or greater)
    - Angular (15.1 or later)
    - PostgreSQL (Anything version 11 or later)
2. Setup PostgreSQL using the admin panel. Create a user called 
   AppTracker and choose any password, making sure you remember 
   what it is.
3. Also in the admin panel, create a database named AppTracker.
4. Within the root of the project structure, create a directory 
   named 'config'.
5. Create a file called server.yml within the config directory,
   and insert the following:
      host: localhost
      database: AppTracker
      user: AppTracker
      password: replaceme
      port: 5432
6. Replace the 'replaceme' with the password you created in step 2. 
   If you installed PostgreSQL on a different machine, change 
   'localhost' to the IP address of that machine. 
7. Run the command 'pip install -r requirements.txt' in a command 
   prompt. This will install the libraries needed for everything 
   to run properly.
8. Run the command 'pip install psycopg2'.
      If running on a mac use the 'psycopg2-binary' instead.
9. Run the command 'python -m unittest' to run the unittests, which
   will also create the tables and load the test data
10. In the following files, adjust the URL variables to 'localhost' 
   or the IP address of PostgreSQL:
   - application.service.ts
   - auth.service.ts
   - auth.ts
   - overview.service.ts
11. In a new command prompt, navigate from the root repository to 
   angular-application-tracker and run the command 'ng serve -o' 
   to run the angular app and open it in the browser automatically
12. Click the register button and sign up for an account
13. Everything should work now. Congratulations!
