asit-asso-extract docker package
=====

## Demo and the config for Extract and Geoshop

This repository contains a working example of the
[Extract](https://github.com/asit-asso/extract/) interacting with [Geoshop](https://github.com/camptocamp/geoshop-back/).

### Based on
* [Extract](https://github.com/asit-asso/extract)
* [Geoshop Extract connector](https://github.com/sitn/sitn_geoshop_connector)
* [Geoshop backend](https://github.com/camptocamp/geoshop-back/)

### How to run
* ```docker compose up``` to bring the system up
* ```docker compose up extract-db-update``` to add test data and geoshop configuration.

### How to test

After everything is started, do ```python tests/extract_geoshop_smoke.py```