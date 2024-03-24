-- creating a database and a table known as cities
create DATABASE IF NOT EXISTS hbtn_0d_usa;
create TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
	name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
