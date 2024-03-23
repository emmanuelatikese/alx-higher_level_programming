-- creating a table
CREATE TABLE IF NOT EXISTS states (
        id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
        name VARCHAR(256) not null,
        UNIQUE(id)
);
