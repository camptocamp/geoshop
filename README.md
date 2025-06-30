Geoshop docker package
=====

## Demo and the config for Extract and Geoshop

This repository contains a working example of the
[Extract](https://github.com/asit-asso/extract/) interacting with Geoshop (
[backend](https://github.com/camptocamp/geoshop-back/) and [frontend](https://github.com/camptocamp/geoshop-front/)) and
using [Zitadel](https://github.com/zitadel) as an authentication service.

### Structure
The system is operated through a remote desktop (VNC) connection to the node which is also used for
an automated testing. Such a solution was made to reduce configuration complexity and having same
system for the tests and manual interaction (experiments and debugging).

### HTTPs/TLS configuration
All services expect certificates to be in ```/cert``` and ```/usr/local/share/ca-certificates/geoshop``` folders and run ```update-ca-certificates``` before start so
the generated certificates could be used by the system.

Python-based services also updated specially to see the system and custom certificates:
1. ```truststore``` installed in addition to other packages
2. ```main.py``` and ```settings.py``` are patched to allow truststore do it's stuff before any network interaction:
```python
import ...
import truststore
truststore.inject_into_ssl()
# ...All other code...
```

Java-based services (extract in our case) also require a special command to import the certs:
```bash
keytool -import -trustcacerts -keystore /cert/extract/cacerts -storepass changeit -noprompt -alias geoshop-back -file /cert/geoshop-back.crt
keytool -import -trustcacerts -keystore /cert/extract/cacerts -storepass changeit -noprompt -alias geoshop-front -file /cert/geoshop-back.crt
```

To generate new certificates, go to the ```volumes/cert``` and run ```bash gencert.sh <domain>```.  Certificates are used only for tests and there is no need to worry about exposing them.

### Initial setup
```volumes``` folder contains database files and other persistent content, so you can remove it
for a clean start or get it from somewhere else to check another configuration.

1. ```docker compose up selenium zitadel``` to start and configure Zitadel authentication
2. ```docker compose exec -d selenium firefox``` to start firefox in the Selenium container
3. ```vncviewer localhost:5900```, password is ```secret``` to enter a session
4. Go to ```https://zitadel```, log in using initial credentials ```zitadel-admin@zitadel.localhost``` and ```Password1!```. Zitadel will ask you to update this password after. I used ```(d9kKNA*``` - it's safe because the password is used only for testing.
5. Create project "Geoshop"
6. Add an application of type ```web``` and call it ```geoshop-front```
    1. When zitadel asks you for redirect links, use "https://geoshop-front/de/auth/oidc"
    2. Edit credentials in the geoshop-front/config.json, update clientId field
7. Add an application of type ```API``` and call it ```geoshop-back```
    1. Add a key with no expiration date and save it to ```/geoshop-keys/private_key.json```
    2. Edit credentials in the geoshop-back/geoshop-back.env and set proper zitadel-project and client-id
8. Configure geoshop-backend to work with extract:
    1. Go to https://geoshop-front/api, log in with default credentials ```admin/Test1234``
    2. Go to Users, set password for user ```extract```, something like "Aa!1Aa!1"
    3. Go to the products section, for each product set provider to ```extract``` if differs.
9. Go to ```https://extract/extract```:
    1. Add an initial admin user
    2. Go to "Connectors", select "Demo extract connector" and check if username is "extract", password is as in previous step (Aa!1Aa!1) and url is


### How to run

1. ```docker compose up``` to bring the system up
2. ```vncviewer localhost:5900``` connects to the Selenium instance with browser.
3. ```docker compose exec selenium firefox``` to start a new browser instance.

### How to test

```docker compose up tests```

### Sources
* [Extract](https://github.com/asit-asso/extract)
* [Geoshop Extract connector](https://github.com/sitn/sitn_geoshop_connector)
* [Geoshop backend](https://github.com/camptocamp/geoshop-back/)
