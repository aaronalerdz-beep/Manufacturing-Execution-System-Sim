--
-- PostgreSQL database dump
--

\restrict fxn5ier0a74CGcxOl7ZZ5WvkP20wkCvGP7hVrklC9wbvUABOvWSqN56uAGXzrd2

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cycles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cycles (
    id integer NOT NULL,
    recorded_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    finished boolean,
    parts_per_cycle integer NOT NULL,
    config_id integer NOT NULL
);


ALTER TABLE public.cycles OWNER TO postgres;

--
-- Name: cycles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cycles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cycles_id_seq OWNER TO postgres;

--
-- Name: cycles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cycles_id_seq OWNED BY public.cycles.id;


--
-- Name: machine_config; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.machine_config (
    id integer NOT NULL,
    machine_id integer NOT NULL,
    pressure integer NOT NULL,
    grit integer NOT NULL,
    cycle_duration numeric(6,2) NOT NULL,
    operator_name character varying(50) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.machine_config OWNER TO postgres;

--
-- Name: machine_config_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.machine_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.machine_config_id_seq OWNER TO postgres;

--
-- Name: machine_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.machine_config_id_seq OWNED BY public.machine_config.id;


--
-- Name: machines; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.machines (
    idm integer NOT NULL,
    name_machine character varying(100) NOT NULL,
    area character varying(100) NOT NULL
);


ALTER TABLE public.machines OWNER TO postgres;

--
-- Name: machines_idm_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.machines ALTER COLUMN idm ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.machines_idm_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: parts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.parts (
    id_seq integer NOT NULL,
    part_num text GENERATED ALWAYS AS (('PN-'::text || lpad((id_seq)::text, 5, '0'::text))) STORED NOT NULL,
    description text NOT NULL,
    material character varying(50) NOT NULL,
    sequence character varying(50),
    weight numeric
);


ALTER TABLE public.parts OWNER TO postgres;

--
-- Name: parts_id_seq_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.parts ALTER COLUMN id_seq ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.parts_id_seq_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: production_orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.production_orders (
    order_num integer NOT NULL,
    part_id integer NOT NULL,
    target_quantity integer NOT NULL,
    final_quantity integer,
    start_time timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.production_orders OWNER TO postgres;

--
-- Name: production_orders_order_num_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.production_orders ALTER COLUMN order_num ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.production_orders_order_num_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: cycles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cycles ALTER COLUMN id SET DEFAULT nextval('public.cycles_id_seq'::regclass);


--
-- Name: machine_config id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.machine_config ALTER COLUMN id SET DEFAULT nextval('public.machine_config_id_seq'::regclass);


--
-- Name: cycles cycles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cycles
    ADD CONSTRAINT cycles_pkey PRIMARY KEY (id);


--
-- Name: machine_config machine_config_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.machine_config
    ADD CONSTRAINT machine_config_pkey PRIMARY KEY (id);


--
-- Name: machines machines_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.machines
    ADD CONSTRAINT machines_pkey PRIMARY KEY (idm);


--
-- Name: parts parts_part_num_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parts
    ADD CONSTRAINT parts_part_num_key UNIQUE (part_num);


--
-- Name: parts parts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.parts
    ADD CONSTRAINT parts_pkey PRIMARY KEY (id_seq);


--
-- Name: production_orders production_orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.production_orders
    ADD CONSTRAINT production_orders_pkey PRIMARY KEY (order_num);


--
-- Name: cycles cycles_config_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cycles
    ADD CONSTRAINT cycles_config_id_fkey FOREIGN KEY (config_id) REFERENCES public.machine_config(id);


--
-- Name: machine_config machine_config_machine_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.machine_config
    ADD CONSTRAINT machine_config_machine_id_fkey FOREIGN KEY (machine_id) REFERENCES public.machines(idm);


--
-- Name: production_orders production_orders_part_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.production_orders
    ADD CONSTRAINT production_orders_part_id_fkey FOREIGN KEY (part_id) REFERENCES public.parts(id_seq);


--
-- PostgreSQL database dump complete
--

\unrestrict fxn5ier0a74CGcxOl7ZZ5WvkP20wkCvGP7hVrklC9wbvUABOvWSqN56uAGXzrd2

