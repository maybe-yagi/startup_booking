SET CHARSET UTF8mb4;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    nickname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    student_num INT,
    role_id INT NOT NULL,
    created_at INT,
    password_hash VARCHAR(100) 
);
