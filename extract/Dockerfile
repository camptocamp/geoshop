# Extract builder
FROM ubuntu:oracular AS builder
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"

WORKDIR /extract-build

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git openjdk-21-jdk maven npm && \
    npm install -g corepack && \
    git clone https://github.com/asit-asso/extract && \
    git clone https://github.com/sitn/sitn_geoshop_connector

RUN cd /extract-build/sitn_geoshop_connector/plugin-interface && \
    mvn clean install && \
    cd /extract-build/sitn_geoshop_connector/connectors/extract-connector-geoshop/ && \
    mvn clean install && \
    cp target/extract-connector-geoshop-2.0-BETA1.jar /extract-build/extract/extract/src/main/resources/connectors

RUN  cd /extract-build/extract/extract/ && \
     bash install_dependencies.sh && \
     cd /extract-build/extract && \
     mvn clean install

# Extract service
FROM tomcat:9.0.64-jre17
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"
COPY --from=builder /extract-build/extract/extract/target/extract##2.1-RELEASE.war /usr/local/tomcat/webapps/
