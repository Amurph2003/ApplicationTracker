INSERT INTO apps(position, company_name, city, state, country, company_info, resume, coverletter, github, notes, extra, extra_material, applied, in_contact, result) VALUES 
    ('Lifeguard', 'YMCA', 'Phoenixville', 'Pennsylvania', 'United States', 'Fitness/Chilcare center', True, True, False, '', True, 'References and Clearances', True, False, 'Recieved and Accepted offer summer 2019'),
    ('French Fryer Cook', 'Thrashers French Fries', 'Ocean City', 'Maryland', 'United States', 'Fry shop at the beach', True, False, False, 'Not ready to apply yet; deadline Jun 17; need cover letter', False, '', False, NULL, NULL),
    ('Pizza Chef', 'Uno Pizzeria & Grill', 'Chicago', 'Illinois', 'United States', 'Pizza Place', False, False, True, 'Need to customize resume', False, '', False, NULL, NULL)
;

INSERT INTO dates(app_id, deadline, applied_on, recent, finalized) VALUES 
    (1, '2023-01-31', '2022-12-23', '2022-12-30', '2023-01-02'),
    (2, '2023-06-17', '2023-01-12', NULL, NULL),
    (3, '2022-12-24', '2023-01-12', NULL, NULL)
;

INSERT INTO users(name, username, hashedpw, email, datejoined, age) VALUES 
    ('Alex', 'Alex486', '12e3iomqeomdew', 'amurph0602@icloud.com', '2023-01-22', 19)
;