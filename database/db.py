import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "spendly.db")


def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Creates all tables using CREATE TABLE IF NOT EXISTS."""
    conn = get_db()
    try:
        # Users table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now'))
            )
        """)

        # Expenses table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """)
        conn.commit()
    finally:
        conn.close()


def seed_db():
    """Inserts sample data for development if not already present."""
    conn = get_db()
    try:
        # Check if users already exist
        cursor = conn.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] > 0:
            return

        # Insert demo user
        password_hash = generate_password_hash("demo123")
        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Demo User", "demo@spendly.com", password_hash)
        )
        user_id = cursor.lastrowid

        # Insert 8 sample expenses
        expenses = [
            ("Food", 15.50, "2026-06-01", "Lunch at cafe"),
            ("Transport", 25.00, "2026-06-03", "Bus pass"),
            ("Bills", 120.00, "2026-06-05", "Electric bill"),
            ("Health", 45.00, "2026-06-08", "Pharmacy"),
            ("Entertainment", 12.99, "2026-06-10", "Movie ticket"),
            ("Shopping", 89.99, "2026-06-12", "New headphones"),
            ("Food", 35.00, "2026-06-15", "Dinner with friends"),
            ("Other", 10.00, "2026-06-18", "Miscellaneous"),
        ]

        for category, amount, date, description in expenses:
            conn.execute(
                "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
                (user_id, amount, category, date, description)
            )

        conn.commit()
    finally:
        conn.close()