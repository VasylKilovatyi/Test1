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

CREATE TABLE IF NOT EXISTS articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    user_id INTEGER CONSTRAINT fr_user_id REFERENCES users(id)
);
INSERT INTO articles (title, content, user_id) VALUES ('Статя1', 'Текст1', 1);
INSERT INTO articles (title, content, user_id) VALUES ('Статя2', 'Текст2', 2);
INSERT INTO articles (title, content, user_id) VALUES ('Статя3', 'Текст3', 3);

SELECT * FROM articles;

DROP TABLE articles;

CREATE TABLE IF NOT EXISTS comment (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    comment TEXT NOT NULL,
    article_id INTEGER CONSTRAINT fr_article_id REFERENCES articles(id),
    user_id INTEGER CONSTRAINT fr_user_id REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO comment (name, comment, article_id, user_id) VALUES ('Статя1', 'Текст1', 1, 2);
INSERT INTO comment (name, comment, article_id, user_id) VALUES ('Статя2', 'Текст2', 2, 3);
INSERT INTO comment (name, comment, article_id, user_id) VALUES ('Статя3', 'Текст3', 3, 1);


SELECT * FROM comment;

DROP TABLE comment;


SELECT
    comment.comment AS comment_content,
    users.name AS user_name
FROM
    comment
INNER JOIN
    users ON comment.user_id = users.id;

