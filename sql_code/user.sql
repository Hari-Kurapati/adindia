CREATE DATABASE IF NOT EXISTS adindia;
USE adindia;

CREATE TABLE IF NOT EXISTS users (
	user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(255) NOT NULL,
    user_phone VARCHAR(30),
    user_email VARCHAR(50) NOT NULL,
    user_password VARCHAR(50) NOT NULL,
    PRIMARY KEY (user_id));