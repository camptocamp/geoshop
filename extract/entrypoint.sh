#!/bin/bash

cacerts="/opt/java/openjdk/lib/security/cacerts"

keytool -delete -keystore -cacerts -storepass changeit -alias geoshop-ca
keytool -import -trustcacerts -cacerts -storepass changeit -noprompt -alias geoshop-ca -file /cert/geoshop-ca.crt

keytool -delete -keystore -cacerts -storepass changeit -alias geoshop-back
keytool -import -trustcacerts -cacerts -storepass changeit -noprompt -alias geoshop-back -file /cert/geoshop-back.crt | 0

keytool -delete -keystore -cacerts -storepass changeit -alias geoshop-front
keytool -import -trustcacerts -cacerts -storepass changeit -noprompt -alias geoshop-front -file /cert/geoshop-back.crt | 0

catalina.sh run