INSERT INTO companies(name, city, state, country, position_title) VALUES 
('YMCA', 'Phoenixville', 'Pennsylvania', 'United States', 'Head Lifeguard'),
('Thrashers French Fries', 'Ocean City', 'Maryland', 'United States', 'Fryer'),
('Uno Pizzeria & Grill', 'Chicago', 'Illinois', 'United States', 'Cook')
;

INSERT INTO apps(company_id, resume, coverletter, github, notes, extra, extra_material, applied, in_contact, result) VALUES 
(1, True, True, False, '', True, 'References and Clearances', True, False, 'Recieved and Accepted offer summer 2019'),
(2, True, False, False, 'Not ready to apply yet; deadline Jun 17; need cover letter', False, '', False, NULL, NULL),
(3, False, False, True, 'Need to customize resume', False, '', False, NULL, NULL)
;

INSERT INTO dates(app_id, deadline, applied_on, recent, finalized) VALUES 
(1, '2023-01-31', '2022-12-23', '2022-12-30', '2023-01-02'),
(2, '2023-06-17', '2023-01-12', NULL, NULL),
(3, '2022-12-24', '2023-01-12', NULL, NULL)
;