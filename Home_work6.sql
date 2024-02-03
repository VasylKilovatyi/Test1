-- Active: 1706797900068@@127.0.0.1@5432@django_site_lesson@public
  CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INTEGER NOT NULL
);

INSERT INTO users (first_name, last_name, age) VALUES ('John', 'Doe', 42);
INSERT INTO users (first_name, last_name, age) VALUES ('Jane', 'Doe', 36);
INSERT INTO users (first_name, last_name, age) VALUES ('John', 'Smith', 24);

SELECT * FROM users;


-- delete 
DELETE FROM users WHERE id > 4;

DROP TABLE users;
