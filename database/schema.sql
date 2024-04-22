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