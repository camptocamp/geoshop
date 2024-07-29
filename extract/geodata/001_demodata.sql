SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;


CREATE SCHEMA tiger;
ALTER SCHEMA tiger OWNER TO extractuser;

CREATE SCHEMA tiger_data;
ALTER SCHEMA tiger_data OWNER TO extractuser;

CREATE SCHEMA topology;
ALTER SCHEMA topology OWNER TO extractuser;
COMMENT ON SCHEMA topology IS 'PostGIS Topology schema';

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;
COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';

CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;
COMMENT ON EXTENSION postgis IS 'PostGIS geometry and geography spatial types and functions';

CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder WITH SCHEMA tiger;
COMMENT ON EXTENSION postgis_tiger_geocoder IS 'PostGIS tiger geocoder and reverse geocoder';

CREATE EXTENSION IF NOT EXISTS postgis_topology WITH SCHEMA topology;
COMMENT ON EXTENSION postgis_topology IS 'PostGIS topology spatial types and functions';


SET default_tablespace = '';
SET default_table_access_method = heap;

CREATE TABLE public.polygons (
    id_0 integer NOT NULL,
    geom public.geometry(Polygon,4326),
    id character(36),
    created timestamp without time zone
);

ALTER TABLE public.polygons OWNER TO extractuser;
COMMENT ON COLUMN public.polygons.id IS 'Polygon UUID';

CREATE SEQUENCE public.polygons_id_0_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE public.polygons_id_0_seq OWNER TO extractuser;
ALTER SEQUENCE public.polygons_id_0_seq OWNED BY public.polygons.id_0;
ALTER TABLE ONLY public.polygons ALTER COLUMN id_0 SET DEFAULT nextval('public.polygons_id_0_seq'::regclass);
INSERT INTO public.polygons (id_0, geom, id, created) VALUES (1, '0103000020E6100000010000000B000000D35C21D6B7532140BCD5D9C656A747402077525EC8232140761944F590B94740697F3D179D9A20409B20E22FB0BA4740C56F8A41FF6B1F402E11F83396AD47408F38455417612040FB3627D51F854740E403734D93AB204012C148878A8E474081D78BFFE36C2040D040F306F49B47408DE0666233A42040399ED8F775A14740C6FB6781845F214010A472E5F1974740804B5BBA93A52140F8EE8979B59F4740D35C21D6B7532140BCD5D9C656A74740', 'a6393c3b-8999-45f0-b6ec-3fc355e6f865', '2024-07-29 00:00:00');

SELECT pg_catalog.setval('public.polygons_id_0_seq', 1, true);
SELECT pg_catalog.setval('topology.topology_id_seq', 1, false);

ALTER TABLE ONLY public.polygons ADD CONSTRAINT polygons_pkey PRIMARY KEY (id_0);
CREATE INDEX sidx_polygons_geom ON public.polygons USING gist (geom);
