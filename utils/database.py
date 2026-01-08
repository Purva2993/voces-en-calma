"""
Database module for Voces en Calma
Handles all database operations with privacy-first design
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path

# Database path
DB_PATH = Path(__file__).parent.parent / "data" / "voces.db"

def init_database():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Stories table - NO personal identifiers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            story_text TEXT NOT NULL,
            emotion_label TEXT,
            emotion_confidence REAL,
            support_choices TEXT NOT NULL,
            practitioner_note TEXT,
            language TEXT DEFAULT 'en'
        )
    """)
    
    # External sentiment table (for Week 3)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS external_sentiment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            text_snippet TEXT NOT NULL,
            emotion_label TEXT,
            theme TEXT,
            source_type TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully")


def save_story(story_text, support_choices, practitioner_note="", language="en"):
    """
    Save a story to the database
    Returns the story ID if successful, None otherwise
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Convert support_choices list to JSON string
        support_json = json.dumps(support_choices)
        
        cursor.execute("""
            INSERT INTO stories (story_text, support_choices, practitioner_note, language)
            VALUES (?, ?, ?, ?)
        """, (story_text, support_json, practitioner_note, language))
        
        story_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return story_id
    except Exception as e:
        print(f"❌ Error saving story: {e}")
        return None


def update_story_emotion(story_id, emotion_label, confidence):
    """Update a story with its emotion label after NLP processing"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE stories 
            SET emotion_label = ?, emotion_confidence = ?
            WHERE id = ?
        """, (emotion_label, confidence, story_id))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Error updating emotion: {e}")
        return False


def get_all_stories():
    """Retrieve all stories for analysis (practitioners only)"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, timestamp, story_text, emotion_label, 
                   emotion_confidence, support_choices, practitioner_note
            FROM stories
            ORDER BY timestamp DESC
        """)
        
        stories = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries for easier handling
        story_list = []
        for story in stories:
            story_list.append({
                'id': story[0],
                'timestamp': story[1],
                'story_text': story[2],
                'emotion_label': story[3],
                'emotion_confidence': story[4],
                'support_choices': json.loads(story[5]),
                'practitioner_note': story[6]
            })
        
        return story_list
    except Exception as e:
        print(f"❌ Error retrieving stories: {e}")
        return []


def get_story_count():
    """Get total number of stories"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM stories")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    except Exception as e:
        print(f"❌ Error getting count: {e}")
        return 0


def get_emotion_distribution():
    """Get distribution of emotions for analytics"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT emotion_label, COUNT(*) as count
            FROM stories
            WHERE emotion_label IS NOT NULL
            GROUP BY emotion_label
            ORDER BY count DESC
        """)
        
        results = cursor.fetchall()
        conn.close()
        
        return {emotion: count for emotion, count in results}
    except Exception as e:
        print(f"❌ Error getting emotion distribution: {e}")
        return {}


def get_support_distribution():
    """Get distribution of requested support types"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("SELECT support_choices FROM stories")
        all_supports = cursor.fetchall()
        conn.close()
        
        # Count each support type
        support_counts = {}
        for (support_json,) in all_supports:
            supports = json.loads(support_json)
            for support in supports:
                support_counts[support] = support_counts.get(support, 0) + 1
        
        return support_counts
    except Exception as e:
        print(f"❌ Error getting support distribution: {e}")
        return {}


def save_external_sentiment(text_snippet, emotion_label, theme, source_type):
    """
    Save external sentiment data to database
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO external_sentiment (text_snippet, emotion_label, theme, source_type)
            VALUES (?, ?, ?, ?)
        """, (text_snippet, emotion_label, theme, source_type))
        
        sentiment_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return sentiment_id
    except Exception as e:
        print(f"❌ Error saving external sentiment: {e}")
        return None


def get_external_sentiment(limit=100):
    """
    Retrieve external sentiment data
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, timestamp, text_snippet, emotion_label, theme, source_type
            FROM external_sentiment
            ORDER BY timestamp DESC
            LIMIT ?
        """, (limit,))
        
        sentiments = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries
        sentiment_list = []
        for sentiment in sentiments:
            sentiment_list.append({
                'id': sentiment[0],
                'timestamp': sentiment[1],
                'text_snippet': sentiment[2],
                'emotion_label': sentiment[3],
                'theme': sentiment[4],
                'source_type': sentiment[5]
            })
        
        return sentiment_list
    except Exception as e:
        print(f"❌ Error retrieving external sentiment: {e}")
        return []


def get_external_emotion_distribution():
    """Get distribution of emotions from external sources"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT emotion_label, COUNT(*) as count
            FROM external_sentiment
            WHERE emotion_label IS NOT NULL
            GROUP BY emotion_label
            ORDER BY count DESC
        """)
        
        results = cursor.fetchall()
        conn.close()
        
        return {emotion: count for emotion, count in results}
    except Exception as e:
        print(f"❌ Error getting external emotion distribution: {e}")
        return {}


def get_theme_distribution():
    """Get distribution of themes from external sources"""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT theme, COUNT(*) as count
            FROM external_sentiment
            WHERE theme IS NOT NULL
            GROUP BY theme
            ORDER BY count DESC
        """)
        
        results = cursor.fetchall()
        conn.close()
        
        return {theme: count for theme, count in results}
    except Exception as e:
        print(f"❌ Error getting theme distribution: {e}")
        return {}


# Initialize database when module is imported
init_database()