INSERT INTO companies(name, info) VALUES 
    ('YMCA', 'Head Lifeguard'),
    ('Thrashers French Fries', 'Fryer'),
    ('Uno Pizzeria & Grill', '')
;

INSERT INTO apps(position, uid, companyID, city, state, country,  applied, contact, result) VALUES 
    ('Lifeguard', 1, 1, 'Phoenixville', 'Pennsylvania', 'United States', True, False, 'Recieved and Accepted offer summer 2019'),
    ('French Fryer Cook', 1, 2, 'Ocean City', 'Maryland', 'United States', False, NULL, NULL),
    ('Pizza Chef', 1, 3, 'Chicago', 'Illinois', 'United States', False, NULL, NULL)
;

INSERT INTO materials(appID, resume, coverletter, github, notes, extra, extraMATERIAL) VALUES 
    (1, True, True, False, '', True, 'References and Clearances'), 
    (2, True, False, False, 'Not ready to apply yet; deadline Jun 17; need cover letter', False, ''), 
    (3, False, False, True, 'Need to customize resume', False, '')
;


INSERT INTO dates(appID, deadline, applied, recent, finalized) VALUES 
    (1, '2023-01-31', '2022-12-23', '2022-12-30', '2023-01-02'),
    (2, '2023-06-17', '2023-01-12', NULL, NULL),
    (3, '2022-12-24', '2023-01-12', NULL, NULL)
;

INSERT INTO users(name, username, hashedpw, email, datejoined, age) VALUES 
    ('Alex', 'Alex486', '12e3iomqeomdew', 'amurph0602@icloud.com', '2023-01-22', 19)
;