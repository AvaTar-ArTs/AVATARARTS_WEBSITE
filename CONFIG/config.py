# AvatarArts Website Configuration
# Configuration file for avatararts.org Flask application

import os
from datetime import datetime

class Config:
    """Base configuration class."""
    
    # Secret key for session management and CSRF protection
    SECRET_KEY = os.environ.get('AVATARARTS_SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Debug mode - should be False in production
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    # nocTurneMeLoDieS V4 Integration Settings
    NOCTURNEMELODIES_PATH = os.environ.get('NOCTURNEMELODIES_PATH') or '/Users/steven/Music/nocTurneMeLoDieS'
    AVATARARTS_V4_PATH = os.environ.get('AVATARARTS_V4_PATH') or '/Users/steven/Music/nocTurneMeLoDieS/github.com/ichoake/AvaTar-Arts/V4_SUNO_INTEGRATION'
    
    # Suno.com Integration Settings
    SUNO_USERNAME = os.environ.get('SUNO_USERNAME') or 'avatararts'
    SUNO_API_KEY = os.environ.get('SUNO_API_KEY')  # Should be set in environment
    
    # GitHub Integration Settings
    GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME') or 'ichoake'
    GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')  # Should be set in environment
    
    # Database Configuration (if using database)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.dirname(__file__), '..', 'avatararts.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Redis Configuration (if using Redis for caching)
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    
    # Email Configuration (if sending emails)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() == 'true'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Security Settings
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'false').lower() == 'true'  # True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Upload Settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or os.path.join(os.path.dirname(__file__), '..', 'STATIC', 'uploads')
    
    # API Rate Limiting
    RATELIMIT_STORAGE_URL = os.environ.get('RATELIMIT_STORAGE_URL') or 'memory://'
    
    # Application Settings
    APPLICATION_NAME = 'AvatarArts Website'
    VERSION = '1.0.0'
    AUTHOR = 'Steven Chaplinski'
    BRAND = 'AvatarArts'
    
    # nocTurneMeLoDieS V4 Specific Settings
    COLLECTION_STATS_CACHE_TIMEOUT = 300  # 5 minutes
    INSIGHTS_CACHE_TIMEOUT = 600  # 10 minutes
    SPECIAL_COLLECTIONS = {
        'alley_chronicles': {
            'name': 'Alley Chronicles',
            'track_count': 151,
            'primary_theme': 'Urban Mythology'
        },
        'willow_variations': {
            'name': 'Willow Variations',
            'track_count': 47,
            'primary_theme': 'Nature Mythology'
        },
        'summer_remixes': {
            'name': 'Summer Remixes',
            'track_count': 34,
            'primary_theme': 'Emotional Journey'
        },
        'hero_collections': {
            'name': 'Hero Collections',
            'track_count': 30,
            'primary_theme': 'Hero Mythology'
        },
        'junkyard_symphonies': {
            'name': 'Junkyard Symphonies',
            'track_count': 50,
            'primary_theme': 'Urban Mythology'
        }
    }
    
    # AvatarArts Themes
    AVATARARTS_THEMES = [
        'Urban Mythology',
        'Nature Mythology',
        'Emotional Journey',
        'Hero Mythology',
        'Classical Mythology'
    ]


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    # Additional development-specific settings
    ASSETS_DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Additional production-specific settings
    SESSION_COOKIE_SECURE = True  # Force HTTPS in production
    PREFERRED_URL_SCHEME = 'https'


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    # Additional testing-specific settings
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}