CREATE EXTENSION postgis;
CREATE EXTENSION fuzzystrmatch;
CREATE EXTENSION postgis_tiger_geocoder;

CREATE SCHEMA IF NOT EXISTS tiger; 
CREATE SCHEMA IF NOT EXISTS tiger_data; 
CREATE SCHEMA IF NOT EXISTS topology; 

ALTER SCHEMA tiger OWNER TO extractuser;
ALTER SCHEMA tiger_data OWNER TO extractuser;
ALTER SCHEMA topology OWNER TO extractuser;

CREATE TABLE public.cantons (
    id character(36) PRIMARY KEY,
    name character(512) NOT NULL,
    geom public.geometry(MultiPolygon, 2056) NOT NULL 
    -- geom public.geometry(MultiPolygon,4326) NOT NULL
    -- Note - EPSG:2056 is for Switzerland, 4326 is for the world
);
ALTER TABLE public.cantons OWNER TO extractuser;
