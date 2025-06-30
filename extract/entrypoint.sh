#!/bin/bash

keystore="/cert/extract/keystore"
mkdir -p /cert/extract/
export JAVA_TOOL_OPTIONS="$JAVA_TOOL_OPTIONS -Djavax.net.ssl.trustStore=$keystore "

keytool -delete -keystore $keystore -storepass changeit -alias geoshop-ca | true
keytool -import -trustcacerts -keystore $keystore -storepass changeit -noprompt -alias geoshop-ca -file /cert/geoshop-ca.crt

keytool -delete -keystore -keystore $keystore -storepass changeit -alias geoshop-back | true
keytool -import -trustcacerts -keystore $keystore -storepass changeit -noprompt -alias geoshop-back -file /cert/geoshop-back.crt | 0

keytool -delete -keystore -keystore $keystore -storepass changeit -alias geoshop-front | true
keytool -import -trustcacerts -keystore $keystore -storepass changeit -noprompt -alias geoshop-front -file /cert/geoshop-back.crt | 0

catalina.sh run