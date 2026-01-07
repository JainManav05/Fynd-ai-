# Complete MySQL Workbench Setup Guide - Step by Step

## Part 1: Installing MySQL (If Not Already Installed)

### Step 1: Download MySQL
1. Go to https://dev.mysql.com/downloads/mysql/
2. Download MySQL Community Server for Windows
3. Download MySQL Workbench from https://dev.mysql.com/downloads/workbench/

### Step 2: Install MySQL Server
1. Run the MySQL installer
2. Choose "Developer Default" or "Server only"
3. Click "Next" through the installation
4. **IMPORTANT**: Set a root password (remember this!)
5. Complete the installation

---

## Part 2: Connecting to MySQL Workbench

### Step 1: Launch MySQL Workbench
1. Open MySQL Workbench from Start Menu
2. You should see the home screen

### Step 2: Create/Open Connection
1. Look for "MySQL Connections" section
2. You should see a default connection called "Local instance MySQL80" (or similar)
3. **Double-click** on this connection

### Step 3: Enter Password
1. A dialog box will appear asking for password
2. Enter the **root password** you set during installation
3. ✅ Check "Save password in vault" (optional, for convenience)
4. Click **OK**

### Step 4: Verify Connection
- If successful, you'll see the SQL Editor with a query tab
- You should see "localhost" in the connection name at the top

---

## Part 3: Creating the Database for Fynd AI Project

### Step 1: Open a New Query Tab
1. In MySQL Workbench, look for the SQL Editor area
2. You should see a blank query tab
3. If not, click the "Create a new SQL tab" icon (looks like a document with +)

### Step 2: Create the Database
Copy and paste this SQL command into the query tab:

```sql
CREATE DATABASE fynd_reviews 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
```

### Step 3: Execute the Command
1. Click the **lightning bolt icon** ⚡ in the toolbar (or press Ctrl+Enter)
2. You should see "1 row(s) affected" in the output panel below
3. ✅ Success! Database created

### Step 4: Verify Database Creation
Run this command to see all databases:

```sql
SHOW DATABASES;
```

You should see `fynd_reviews` in the list.

### Step 5: Select the Database
Make this database active by running:

```sql
USE fynd_reviews;
```

You should see "Database changed" in the output.

---

## Part 4: Getting Connection Details for .env File

### Step 1: Note Your Connection Details
You need these details for your `.env` file:

- **Host**: `localhost` (if MySQL is on your computer)
- **Port**: `3306` (default MySQL port)
- **Username**: `root` (or the username you created)
- **Password**: The password you set during installation
- **Database**: `fynd_reviews` (we just created this)

### Step 2: Update Your .env File
Open `project_root/.env` and update this line:

```
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/fynd_reviews
```

**Replace `YOUR_PASSWORD`** with your actual MySQL root password.

**Example:**
If your password is `MyPass123`, it should look like:
```
DATABASE_URL=mysql+pymysql://root:MyPass123@localhost:3306/fynd_reviews
```

---

## Part 5: Testing the Connection from Python

### Step 1: Install Dependencies
Open terminal in `project_root/` and run:

```bash
pip install pymysql cryptography sqlalchemy python-dotenv
```

### Step 2: Test Connection Script
Create a test file `test_db.py` in `project_root/`:

```python
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print(f"Connecting to: {DATABASE_URL.replace(DATABASE_URL.split(':')[2].split('@')[0], '****')}")

try:
    engine = create_engine(DATABASE_URL)
    connection = engine.connect()
    print("✅ Connection successful!")
    connection.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

### Step 3: Run Test
```bash
python test_db.py
```

If you see "✅ Connection successful!" - you're all set!

---

## Part 6: Running the Fynd AI Backend (Creates Tables Automatically)

### Step 1: Navigate to Backend
```bash
cd task2/backend
```

### Step 2: Start the Backend
```bash
uvicorn main:app --reload
```

### Step 3: Verify Tables Were Created
Go back to MySQL Workbench and run:

```sql
USE fynd_reviews;
SHOW TABLES;
```

You should see:
- `reviews`

### Step 4: Check Table Structure
```sql
DESCRIBE reviews;
```

You should see columns:
- id
- rating
- review_text
- ai_response
- ai_summary
- ai_action
- created_at

---

## Common Issues & Solutions

### Issue 1: "Access denied for user 'root'@'localhost'"
**Solution:**
- Wrong password in `.env` file
- Check your MySQL root password
- Update `.env` with correct password

### Issue 2: "Can't connect to MySQL server on 'localhost'"
**Solution:**
- MySQL Server is not running
- Open "Services" (Windows) and start "MySQL80" service
- Or restart MySQL from MySQL Workbench: Server → Startup/Shutdown

### Issue 3: "Unknown database 'fynd_reviews'"
**Solution:**
- Database not created yet
- Go back to Part 3 and create the database

### Issue 4: Authentication plugin error
**Solution:**
Run this in MySQL Workbench:
```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
FLUSH PRIVILEGES;
```

### Issue 5: Port 3306 already in use
**Solution:**
- Another MySQL instance is running
- Check Task Manager and close other MySQL processes
- Or change port in connection string

---

## Quick Reference Card

### MySQL Workbench Shortcuts
- **Ctrl + Enter**: Execute current SQL statement
- **Ctrl + Shift + Enter**: Execute all statements
- **Ctrl + T**: New query tab
- **Ctrl + W**: Close current tab

### Useful SQL Commands
```sql
-- Show all databases
SHOW DATABASES;

-- Use a database
USE fynd_reviews;

-- Show all tables
SHOW TABLES;

-- Show table structure
DESCRIBE reviews;

-- Show all data in reviews table
SELECT * FROM reviews;

-- Count reviews
SELECT COUNT(*) FROM reviews;

-- Delete all data (careful!)
TRUNCATE TABLE reviews;
```

---

## Next Steps

1. ✅ MySQL Workbench connected
2. ✅ Database `fynd_reviews` created
3. ✅ `.env` file updated with credentials
4. ✅ Backend running (creates tables automatically)
5. 🚀 Start the frontend and test the application!

**To start the frontend:**
```bash
cd task2/frontend
reflex run
```

Visit http://localhost:3000 to use the app!
