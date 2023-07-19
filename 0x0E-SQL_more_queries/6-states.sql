--Create database hbtn_0d_usa and table states in database
--hbtn_0d_usa.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.usa (
		PRIMARY KEY(`id`),
		`id` INT	NOT NULL AUTO_INCREMENT,
		`name` VARCHAR(256) NOT NULL
);
