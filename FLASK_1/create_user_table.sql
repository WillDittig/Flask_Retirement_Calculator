CREATE TABLE users (
    iduser SERIAL PRIMARY KEY,
    username VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL,
    isadmin BIT DEFAULT 0::BIT,
    isactive BIT DEFAULT 0::BIT
);