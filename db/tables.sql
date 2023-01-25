DROP TABLE IF EXISTS apps;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS users;

CREATE TABLE apps(
    id              SERIAL PRIMARY KEY NOT NULL,
    position        VARCHAR(200) NOT NULL,
    company_name    VARCHAR(500) NOT NULL,
    company_info    VARCHAR(500) NOT NULL,
    city            VARCHAR(200) NOT NULL,
    state           VARCHAR(200) NOT NULL,
    country         VARCHAR(200) NOT NULL,
    resume          BOOLEAN NOT NULL,
    coverletter     BOOLEAN NOT NULL,
    github          BOOLEAN NOT NULL,
    notes           VARCHAR(500),
    extra           BOOLEAN NOT NULL,
    extra_material  VARCHAR(200),
    applied         BOOLEAN NOT NULL,
    in_contact      BOOLEAN,
    result          VARCHAR(200)
);

CREATE TABLE dates(
    id              SERIAL PRIMARY KEY NOT NULL,
    app_id          INTEGER NOT NULL,
    deadline        DATE,
    applied_on      DATE NOT NULL DEFAULT CURRENT_DATE,
    recent          DATE,
    finalized       DATE
);

CREATE TABLE users(
    id              SERIAL PRIMARY KEY NOT NULL,
    name            VARCHAR(200) NOT NULL,
    username        VARCHAR(200) NOT NULL,
    hashedpw        VARCHAR(200) NOT NULL,
    email           VARCHAR(200) NOT NULL,
    datejoined      DATE NOT NULL DEFAULT CURRENT_DATE,
    age             INTEGER NOT NULL
);