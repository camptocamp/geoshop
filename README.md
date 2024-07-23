assit-asso-extract docker package
=====

## Demo and the config for Extract and Geoshop

This repository contains a working example of the 
[Extract](https://github.com/asit-asso/extract/) interacting with [Geoshop](https://github.com/camptocamp/geoshop-back/).

### Based on
* [Extract](https://github.com/asit-asso/extract)
* [Geoshop Extract connector](https://github.com/sitn/sitn_geoshop_connector)
* [Geoshop backend](https://github.com/camptocamp/geoshop-back/)

## How to run
It should be enough to run ```docker compose up```, docker will build all the images and start the containers.

### How to test
Extract fetches orders by sending a ```GET http://geoshop_host:8000/extract/order/``` request periodically. Geoshop returns all requests that are eligible for extracting, marks them as ```in_extract``` and will not return it again.

[ExtractOrderView](https://github.com/camptocamp/geoshop-back/blob/master/api/views.py#L349) handles the request, it will return OrderItems which are:

* Order status is either READY or PARTIALLY_DELIVERED
* Order provider is the user that makes request (extract in our case)
* OrderItem status is PENDING

### Utility scripts

To create an order to be picked by Extract, send this script to the ```Geoshop's``` postgres database.

```sql

-- Needed for the gen_random_uuid
CREATE EXTENSION pgcrypto;

-- Wrapping everything in a transaction so Extract won't load only part of an order
START TRANSACTION; 

--- Create an Order (A rectangle, with autoincrement ID and random download uuid)
INSERT INTO "order" (
  title, description, processing_fee_currency, processing_fee, total_without_vat_currency, total_without_vat, part_vat_currency, part_vat, total_with_vat_currency, total_with_vat, geom, invoice_reference, date_ordered, date_downloaded, date_processed, client_id, invoice_contact_id, order_type_id, extract_result, download_guid, email_deliver, order_status)VALUES ('Demo order ' || to_char(NOW(), 'HH:MI'), 'An order for experiments', 'CHF', NULL, 'CHF', NULL, 'CHF', NULL, 'CHF', NULL, '0103000020080800000100000005000000E0609D479AAF1141DCE4284375FD4BC1009C5A7EEBDDCEC066574A1D448B52C111DEA19A8E293A41E8A550A937FF53C1EC647D947B943B41523BEBFDA75E4EC1E0609D479AAF1141DCE4284375FD4BC1', '', NOW(), NULL, NULL, 3, NULL, 1, '', gen_random_uuid(), '', 'READY');

-- Create a relevant OrderItem order_id=CURRVAL('order_id_seq')
INSERT INTO order_item (last_download, price_status, _price_currency, _price, _base_fee_currency, _base_fee, data_format_id, order_id, product_id, extract_result, srid, status, comment, token, validation_date) VALUES (NULL, 'CALCULATED', 'CHF', 0.00, 'CHF', NULL, 1, CURRVAL('order_id_seq'), 1, '', 2056, 'PENDING', NULL, NULL, NULL);

-- Create a relevant OrderItem order_id=CURRVAL('order_id_seq')
INSERT INTO order_item (last_download, price_status, _price_currency, _price, _base_fee_currency, _base_fee, data_format_id, order_id, product_id, extract_result, srid, status, comment, token, validation_date) VALUES (NULL, 'CALCULATED', 'CHF', 0.00, 'CHF', NULL, 1, CURRVAL('order_id_seq'), 1, '', 2056, 'PENDING', NULL, NULL, NULL);

-- Create a relevant OrderItem order_id=CURRVAL('order_id_seq')
INSERT INTO order_item (last_download, price_status, _price_currency, _price, _base_fee_currency, _base_fee, data_format_id, order_id, product_id, extract_result, srid, status, comment, token, validation_date) VALUES (NULL, 'CALCULATED', 'CHF', 0.00, 'CHF', NULL, 1, CURRVAL('order_id_seq'), 1, '', 2056, 'PENDING', NULL, NULL, NULL);

END TRANSACTION;
```
