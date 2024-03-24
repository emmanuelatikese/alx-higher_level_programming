-- creating a database and a table known as cities
create database if not exists hbtn_0d_usa;
create table if not exists hbtn_0d_usa.cities (
	id int auto_increment primary_key not null,
	name varchar(256) not null,
	state_id int,
	foreign key (state_id) references states(id)
);
