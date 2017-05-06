
--DROP DATABASE mtdatabase;
--CREATE DATABASE mtdatabase;

CREATE TABLE Worker
(
    Nr serial PRIMARY KEY,
    Lastname text NOT NULL,
    Firstname text NOT NULL,
    CONSTRAINT Worker_lastname_firstname UNIQUE (Lastname, Firstname)
);
CREATE TABLE Workday
(
    Nr serial PRIMARY KEY,
    Worker_nr integer NOT NULL REFERENCES Worker ON UPDATE RESTRICT ON DELETE RESTRICT,
    Begin_at timestamptz,
    End_at timestamptz,
    Break interval minute NOT NULL,
    Vacation boolean NOT NULL,
    Sick boolean NOT NULL
);
CREATE TABLE Tasktype
(
    Nr serial PRIMARY KEY,
    Title text NOT NULL UNIQUE
);
CREATE TABLE Company
(
    Nr serial PRIMARY KEY,
    Title text NOT NULL UNIQUE
);
CREATE TABLE Client
(
    Nr serial PRIMARY KEY,
    Company_nr integer NOT NULL REFERENCES Company ON UPDATE RESTRICT ON DELETE RESTRICT,
    Lastname text NOT NULL,
    Firstname text NOT NULL,
    CONSTRAINT Client_lastname_firstname UNIQUE (Lastname, Firstname)
);
CREATE TABLE Task
(
    Nr serial PRIMARY KEY,
    Workday_nr integer NOT NULL REFERENCES Workday ON UPDATE RESTRICT ON DELETE RESTRICT,
    Type_nr integer NOT NULL REFERENCES Tasktype ON UPDATE RESTRICT ON DELETE RESTRICT,
    Client_nr integer REFERENCES Client ON UPDATE RESTRICT ON DELETE RESTRICT,
    Lastedit_at timestamptz NOT NULL,
    Description text NOT NULL
);
