# MySQL Setup Guide for Fynd AI Assessment

## Prerequisites
- MySQL Workbench installed
- MySQL Server running (version 5.7+ or 8.0+)

## Step-by-Step Setup

### 1. Create Database in MySQL Workbench

Open MySQL Workbench and run the following SQL commands:

```sql
-- Create database
CREATE DATABASE fynd_reviews CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Verify database creation
SHOW DATABASES;

-- Use the database
USE fynd_reviews;
```

### 2. Create MySQL User (Optional - for security)

```sql
-- Create a dedicated user for the application
CREATE USER 'fynd_user'@'localhost' IDENTIFIED BY 'your_secure_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON fynd_reviews.* TO 'fynd_user'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
```

### 3. Configure Environment Variables

Edit your `.env` file with your MySQL credentials:

**Option A: Using root user (for development)**
```
DATABASE_URL=mysql+pymysql://root:your_mysql_password@localhost:3306/fynd_reviews
```

**Option B: Using dedicated user (recommended)**
```
DATABASE_URL=mysql+pymysql://fynd_user:your_secure_password@localhost:3306/fynd_reviews
```

### 4. Install Dependencies

Make sure you have the MySQL connector installed:

```bash
pip install pymysql cryptography
```

Or reinstall all requirements:

```bash
pip install -r requirements.txt
```

### 5. Initialize Database Tables

The tables will be created automatically when you first run the backend:

```bash
cd task2/backend
uvicorn main:app --reload
```

### 6. Verify Tables in MySQL Workbench

After running the backend once, check that the `reviews` table was created:

```sql
USE fynd_reviews;
SHOW TABLES;
DESCRIBE reviews;
```

You should see a table with these columns:
- id (INT, PRIMARY KEY)
- rating (INT)
- review_text (TEXT)
- ai_response (TEXT)
- ai_summary (TEXT)
- ai_action (TEXT)
- created_at (DATETIME)

## Troubleshooting

### Connection Error
- Verify MySQL server is running
- Check username and password in `.env`
- Ensure database `fynd_reviews` exists
- Check port number (default: 3306)

### Authentication Error
- MySQL 8.0+ uses `caching_sha2_password` by default
- If you get authentication errors, run:
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
FLUSH PRIVILEGES;
```

### Port Already in Use
- Check if another MySQL instance is running
- Change port in connection string if needed

## Switching Back to SQLite

If you want to use SQLite instead, simply change the `.env` file:

```
DATABASE_URL=sqlite:///./reviews.db
```

The code automatically detects the database type and uses appropriate settings.
