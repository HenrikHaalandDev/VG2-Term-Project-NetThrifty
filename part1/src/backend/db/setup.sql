CREATE DATABASE NetThirftyDB;

USE NetThirftyDB;


CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number CHAR(8),
    date_of_birth DATE,
    address TEXT
);

