-- script that creates the table id_not_null on your MySQL server
CREATE Table IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);