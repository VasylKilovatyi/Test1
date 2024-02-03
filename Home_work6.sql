-- Active: 1706797900068@@127.0.0.1@5432@django_site_lesson@public
  CREATE TABLE IF NOT EXISTS comment (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    
    
);

INSERT INTO comment (name) VALUES ('John');
INSERT INTO comment (name) VALUES ('Jane');
INSERT INTO comment (name) VALUES ('John');

SELECT * FROM comment;


-- delete 
DELETE FROM comment WHERE id > 4;

DROP TABLE comment;