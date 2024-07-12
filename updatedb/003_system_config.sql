UPDATE system SET value = 'mailhog' WHERE key = 'smtp_server';
UPDATE system SET value =  1025 WHERE key = 'smtp_port';
UPDATE system SET value = 'openldap' WHERE key = 'ldap_servers';
UPDATE system SET value = true WHERE key = 'ldap_on'; 
UPDATE system SET value = STARTTLS WHERE key = 'ldap_encryption_type';