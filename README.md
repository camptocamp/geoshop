asit-asso-extract docker package
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
keytool -import -trustcacerts -keystore /opt/java/openjdk/lib/security/cacerts -storepass changeit -noprompt -alias geoshop-back -file /cert/geoshop-back.crt
keytool -import -trustcacerts -keystore /opt/java/openjdk/lib/security/cacerts -storepass changeit -noprompt -alias geoshop-front -file /cert/geoshop-back.crt
```

To generate new certificates, go to the ```volumes/cert``` and run ```bash gencert.sh <domain>```.  Certificates are used only for tests and there is no need to worry about exposing them.

### How to run (cold start)
1. ```docker compose up``` to bring the system up
2. ```vncviewer localhost:5900``` connects to the Selenium instance with browser.
3. Do the initialization steps and first run steps.
4. Keep ```volumes``` folder somewhere to avoid lengthy configuration process.

### How to run (hot start)
1. Get ```volumes``` content from someone
2. ```docker compose up``` to bring the system up

### How to test

```docker compose up tests```

### Sources
* [Extract](https://github.com/asit-asso/extract)
* [Geoshop Extract connector](https://github.com/sitn/sitn_geoshop_connector)
* [Geoshop backend](https://github.com/camptocamp/geoshop-back/)
