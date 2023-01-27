DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS apps;
DROP TABLE IF EXISTS dates;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS materials;

CREATE TABLE companies(
    id              SERIAL PRIMARY KEY NOT NULL,
    name            VARCHAR(150) NOT NULL,
    info            VARCHAR(200)
);

CREATE TABLE apps(
    id              SERIAL PRIMARY KEY NOT NULL,
    uid             INTEGER NOT NULL,
    position        VARCHAR(200) NOT NULL,
    companyID      INTEGER NOT NULL,
    city            VARCHAR(150) NOT NULL,
    state           VARCHAR(150) NOT NULL,
    country         VARCHAR(150) NOT NULL,
    applied         BOOLEAN NOT NULL,
    contact         BOOLEAN,
    result          VARCHAR(200)
);

CREATE Table materials(
    id              SERIAL PRIMARY KEY NOT NULL,
    appID           INTEGER NOT NULL,
    resume          BOOLEAN NOT NULL,
    coverletter     BOOLEAN NOT NULL,
    github          BOOLEAN NOT NULL,
    notes           VARCHAR(500),
    extra           BOOLEAN NOT NULL,
    extraMATERIAL   VARCHAR(200)
);

CREATE TABLE dates(
    id              SERIAL PRIMARY KEY NOT NULL,
    appID           INTEGER NOT NULL,
    deadline        DATE,
    applied         DATE,
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