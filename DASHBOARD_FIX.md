# Dashboard Navigation Fix - Quick Test Guide

## What Was Fixed

1. ✅ Changed relative imports to absolute imports in `app.py`
2. ✅ Added navigation buttons between dashboards
3. ✅ Created `__init__.py` for frontend package
4. ✅ Added page titles for better UX

## How to Test

### 1. Stop Current Frontend (if running)
Press `Ctrl+C` in the frontend terminal

### 2. Restart Frontend
```bash
cd task2/frontend
reflex run
```

### 3. Test Navigation

**User Dashboard (http://localhost:3000):**
- Should see "Submit Your Review" heading
- Should see "Go to Admin Dashboard" button at the top
- Click the button → Should navigate to `/admin`

**Admin Dashboard (http://localhost:3000/admin):**
- Should see "Admin Dashboard" heading
- Should see "Refresh" and "Go to User Dashboard" buttons
- Click "Go to User Dashboard" → Should navigate back to `/`

### 4. Test Full Flow

1. Go to http://localhost:3000
2. Submit a review
3. Click "Go to Admin Dashboard"
4. Click "Refresh" to see your review
5. Click "Go to User Dashboard" to return

## If Issues Persist

### Clear Reflex Cache
```bash
cd task2/frontend
rm -rf .web
reflex init
reflex run
```

### Check Backend is Running
Visit http://localhost:8000/docs - should show API documentation

### Check Console for Errors
Look for errors in the terminal where `reflex run` is running

## Navigation URLs

- **User Dashboard**: http://localhost:3000/
- **Admin Dashboard**: http://localhost:3000/admin
- **Backend API**: http://localhost:8000/docs
