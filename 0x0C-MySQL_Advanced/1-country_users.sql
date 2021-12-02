-- mysql script that make table users

CREATE DATABASE IF NOT EXISTS holberton;
CREATE TABLE IF NOT EXISTS users (
    id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM ('US', 'CO', 'TN') NOT NULL
);
