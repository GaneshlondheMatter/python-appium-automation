#!/usr/bin/env python
"""Quick script to test database connection"""

from utils.db_connection import DBConnection

try:
    print("Attempting to connect to database...")
    conn = DBConnection.get_connection()
    print("Database connected successfully!")
    conn.close()
except Exception as e:
    print(f"Database connection failed: {e}")
    exit(1)
