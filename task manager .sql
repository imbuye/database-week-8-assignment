-- Create the database
CREATE DATABASE IF NOT EXISTS taskdb;
USE taskdb;

-- Drop tables if they already exist (for testing/demo purposes)
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Create tasks table
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Insert sample users
INSERT INTO users (name, email) VALUES 
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com');

-- Insert sample tasks
INSERT INTO tasks (title, description, completed, user_id) VALUES 
('Buy groceries', 'Milk, Eggs, Bread', FALSE, 1),
('Finish project', 'Complete FastAPI backend', TRUE, 2),
('Call dentist', 'Appointment on Thursday', FALSE, 1);
