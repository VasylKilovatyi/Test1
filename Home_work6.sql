-- Active: 1706797900068@@127.0.0.1@5432@django_site_lesson@public
CREATE TABLE IF NOT EXISTS public.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    
    
);

-- Insert data
INSERT INTO users (name) VALUES ('Вася');
INSERT INTO users (name) VALUES ('Влад');
INSERT INTO users (name) VALUES ('Макс');

-- Select data
SELECT * FROM users;

-- Delete data
DELETE FROM users WHERE id > 4;

-- Drop table
DROP TABLE users;

CREATE TABLE IF NOT EXISTS article (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    user_id INTEGER CONSTRAINT fr_user_id REFERENCES users(id)
);
INSERT INTO article (title, content, user_id) VALUES ('Статя1', 'Текст1', 1);
INSERT INTO article (title, content, user_id) VALUES ('Статя2', 'Текст2', 2);
INSERT INTO article (title, content, user_id) VALUES ('Статя3', 'Текст3', 3);

SELECT * FROM article;

DROP TABLE article;