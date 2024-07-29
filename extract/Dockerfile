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

COPY extract-task-exec /extract-build/extract-task-exec

RUN cd /extract-build/sitn_geoshop_connector/plugin-interface && \
    mvn clean install && \
    cd /extract-build/sitn_geoshop_connector/connectors/extract-connector-geoshop/ && \
    mvn clean install && \
    cp target/extract-connector-geoshop-2.0-BETA1.jar /extract-build/extract/extract/src/main/resources/connectors && \
    cd /extract-build/extract/extract-interface && \
    mvn clean install && \
    cd /extract-build/extract-task-exec && \
    mvn clean install  && \
    cp /extract-build/extract-task-exec/target/original-extract-task-exec-2.1-RELEASE.jar /extract-build/extract/extract/src/main/resources/task_processors/extract-task-exec-2.1-RELEASE.jar

RUN  cd /extract-build/extract/extract/ && \
     bash install_dependencies.sh && \
     cd /extract-build/extract && \
     mvn clean install

# Extract service
FROM tomcat:9.0.64-jre17
LABEL Maintainer="andrey.rusakov@camptocamp.com" Vendor="Camptocamp"
RUN apt update && apt upgrade -y && \
    apt install -y python3 python3-gdal && \
    mkdir -p /var/extract/orders && mkdir -p /extract/
COPY --from=builder /extract-build/extract/extract/target/extract##2.1-RELEASE.war /usr/local/tomcat/webapps/
COPY script.py /extract/script.py
