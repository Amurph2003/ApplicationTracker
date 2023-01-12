DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS apps;
DROP TABLE IF EXISTS dates;

CREATE TABLE companies(
    id              SERIAL PRIMARY KEY NOT NULL,
    name            VARCHAR(150) NOT NULL,
    city            VARCHAR(150) NOT NULL,
    state           VARCHAR(150) NOT NULL,
    country         VARCHAR(150) NOT NULL,
    position_title  VARCHAR(200) NOT NULL,
    info            VARCHAR(200)
);

CREATE TABLE apps(
    id              SERIAL PRIMARY KEY NOT NULL,
    company_id      INTEGER NOT NULL,
    resume          BOOLEAN NOT NULL,
    coverletter     BOOLEAN NOT NULL,
    github          BOOLEAN NOT NULL,
    notes           VARCHAR(500) NOT NULL,
    extra           BOOLEAN NOT NULL,
    extra_material  VARCHAR(200) NOT NULL,
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