UPDATE system SET value = 'mailhog' WHERE key = 'smtp_server';
UPDATE system SET value =  1025 WHERE key = 'smtp_port';
UPDATE system SET value = 'openldap' WHERE key = 'ldap_servers';
UPDATE system SET value = true WHERE key = 'ldap_on'; 
UPDATE system SET value = 'STARTTLS' WHERE key = 'ldap_encryption_type';

INSERT INTO processes VALUES (4, 'Ask operator');
INSERT INTO processes_users VALUES (4, 2), (4, 3);

INSERT INTO connectors (id_connector, active, connector_code, connector_label, connector_params, import_freq, max_retries, name)
VALUES (0, true, 'geoshopextract', 'Plugin Geoshop STIN', '{"uploadSize":"","detailsUrl":"","pass":"5%G*1jA^BpJDiEpi","login":"extract","url":"http://geoshop:8000"}', 4, 3, 'Extract')
ON CONFLICT DO NOTHING;

INSERT INTO tasks(id_task, task_code, task_label, task_params, position, id_process)
VALUES(4, 'VALIDATION', 'Validation opérateur', '{"reject_msgs":"","valid_msgs":""}', 1, 4);

INSERT INTO rules VALUES (4, true, 1, '*', 0, 4);