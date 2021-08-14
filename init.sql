CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users (
    userID          uuid            DEFAULT     uuid_generate_v4 (), 
    age             SMALLINT        NOT NULL,
    PRIMARY KEY (userId)
);

CREATE TABLE items (
    itemID          uuid            DEFAULT     uuid_generate_v4 (),
    price           NUMERIC(7, 2)   NOT NULL,
    PRIMARY KEY (itemID)
);

CREATE TABLE purchases (
    purchaseID      uuid            DEFAULT     uuid_generate_v4 (),
    userID          uuid            NOT NULL    REFERENCES users (userID),
    itemID          uuid            NOT NULL    REFERENCES items (itemID),
    purchase_date   DATE            NOT NULL
)
