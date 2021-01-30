DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS attractions;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    wishlist BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    wishlist BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    entry_fee BOOLEAN,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    attraction_id INT REFERENCES attractions(id) ON DELETE CASCADE
);

    
