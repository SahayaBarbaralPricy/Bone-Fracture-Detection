-- ============================================================
-- BONE FRACTURE DETECTION SYSTEM
-- DATABASE
-- ============================================================

-- ============================================================
-- CREATE DATABASE
-- ============================================================

CREATE DATABASE IF NOT EXISTS bone_fracture_db;

USE bone_fracture_db;


-- ============================================================
-- USERS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS users (

    id INT AUTO_INCREMENT PRIMARY KEY,

    fullname VARCHAR(100) NOT NULL,

    email VARCHAR(100) NOT NULL UNIQUE,

    phone VARCHAR(15),

    username VARCHAR(50) NOT NULL UNIQUE,

    password VARCHAR(255) NOT NULL,

    profile_image VARCHAR(255)
        DEFAULT 'avatar.png',

    created_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP

);


-- ============================================================
-- PREDICTIONS TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS predictions (

    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    patient_name VARCHAR(100),

    age INT,

    gender VARCHAR(20),

    body_part VARCHAR(100),

    image_name VARCHAR(255) NOT NULL,

    prediction_result VARCHAR(100) NOT NULL,

    confidence DECIMAL(5,2),

    report_file VARCHAR(255)
        DEFAULT NULL,

    predicted_at TIMESTAMP
        DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_predictions_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE

);


-- ============================================================
-- INDEXES
-- ============================================================

CREATE INDEX idx_predictions_user_id
ON predictions(user_id);

CREATE INDEX idx_predictions_predicted_at
ON predictions(predicted_at);


-- ============================================================
-- OPTIONAL TEST USER
-- ============================================================
-- Do NOT insert a test user unless you want one.
--
-- You can register normally through your Flask application.
-- ============================================================


-- ============================================================
-- VERIFY TABLES
-- ============================================================

SHOW TABLES;


-- ============================================================
-- VERIFY USERS TABLE
-- ============================================================

DESCRIBE users;


-- ============================================================
-- VERIFY PREDICTIONS TABLE
-- ============================================================

DESCRIBE predictions;