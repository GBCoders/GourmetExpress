-- USE codepy;
-- CREATE TABLE signup (
--     name VARCHAR,
--     phone NUMBER,
--     email VARCHAR UNIQUE NOT NULL,
--      password VARCHAR NOT NULL

-- );

-- INSERT INTO signup (name, phone, email, password) VALUES ('paula', '61992345870', 'gleiscylima@gmail.com', 'Brasil0105')

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    phone VARCHAR,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);
CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR UNIQUE
);
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    description VARCHAR,
    price DECIMAL,
    category_id INTEGER REFERENCES category(id)
);

