UPDATE system SET value = 'mailhog' WHERE key = 'smtp_server';
UPDATE system SET value =  1025 WHERE key = 'smtp_port';
UPDATE system SET value = 'openldap' WHERE key = 'ldap_servers';
UPDATE system SET value = true WHERE key = 'ldap_on'; 
UPDATE system SET value = 'STARTTLS' WHERE key = 'ldap_encryption_type';

INSERT INTO public.processes (id_process, name) VALUES (4, 'Execute script');
INSERT INTO public.processes_users (id_process, id_user) VALUES (4, 2);
INSERT INTO public.processes_users (id_process, id_user) VALUES (4, 3);

INSERT INTO connectors (id_connector, active, connector_code, connector_label, connector_params, error_count, import_freq, last_import_date, last_import_msg, max_retries, name) VALUES (4, true, 'geoshopextract', 'Plugin Geoshop SITN', '{"uploadSize":"","detailsUrl":"","pass":"5%G*1jA^BpJDiEpi","login":"external_provider","url":"' || :geoshop_backend || '"}', 0, 5, '2024-07-17 10:25:13.03', '', 3, 'Demo extract connector');
INSERT INTO public.tasks (id_task, task_code, task_label, task_params, "position", id_process) VALUES (7, 'EXECUTE', 'Execute script', '{"path":"/extract/script.py"}', 1, 4);
INSERT INTO public.rules (id_rule, active, "position", rule, id_connector, id_process) VALUES (4, true, 1, 'surface > 0', 4, 4);