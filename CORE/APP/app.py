"""
AvatarArts Website - Official Website for avatararts.org
Creative Automation Platform for Steven Chaplinski
"""

import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from datetime import datetime
import json
from pathlib import Path

# Initialize Flask app
app = Flask(__name__, 
            template_folder='../TEMPLATES',
            static_folder='../STATIC')

# Configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'avatararts-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', False)
    # nocTurneMeLoDieS V4 integration settings
    NOCTURNEMELODIES_PATH = '/Users/steven/Music/nocTurneMeLoDieS'
    AVATARARTS_V4_PATH = '/Users/steven/Music/nocTurneMeLoDieS/github.com/ichoake/AvaTar-Arts/V4_SUNO_INTEGRATION'

# Apply configuration
app.config.from_object(Config)

# Import nocTurneMeLoDieS V4 data
def get_avatararts_collection():
    """Get AvatarArts collection data from V4 system"""
    try:
        # This would normally connect to the V4 API or read from the system
        # For now, we'll return mock data based on the V4 system
        collection_data = {
            "total_tracks": 1184,
            "total_albums": 665,
            "total_repositories": 12,
            "avatararts_repositories": 3,
            "special_collections": {
                "alley_chronicles": {
                    "name": "Alley Chronicles",
                    "track_count": 151,
                    "primary_theme": "Urban Mythology"
                },
                "willow_variations": {
                    "name": "Willow Variations", 
                    "track_count": 47,
                    "primary_theme": "Nature Mythology"
                },
                "summer_remixes": {
                    "name": "Summer Remixes",
                    "track_count": 34,
                    "primary_theme": "Emotional Journey"
                },
                "hero_collections": {
                    "name": "Hero Collections",
                    "track_count": 30,
                    "primary_theme": "Hero Mythology"
                },
                "junkyard_symphonies": {
                    "name": "Junkyard Symphonies",
                    "track_count": 50,
                    "primary_theme": "Urban Mythology"
                }
            },
            "avatararts_themes": [
                "Urban Mythology",
                "Nature Mythology", 
                "Emotional Journey",
                "Hero Mythology",
                "Classical Mythology"
            ],
            "suno_integration": {
                "username": "avatararts",
                "tracks_count": 1184,
                "followers_count": 156,
                "status": "connected"
            },
            "github_integration": {
                "username": "ichoake",
                "repositories_count": 47,
                "avatararts_repos": 3,
                "status": "connected"
            },
            "last_updated": datetime.now().isoformat()
        }
        return collection_data
    except Exception as e:
        print(f"Error loading AvatarArts collection: {str(e)}")
        return {}

def get_avatararts_insights():
    """Get insights about the AvatarArts collection"""
    try:
        # This would normally connect to the V4 AI analysis
        # For now, we'll return mock insights
        insights = {
            "collection_overview": {
                "total_tracks": 1184,
                "total_duration_hours": 1247.5,
                "average_duration_seconds": 378.2,
                "most_popular_track": "In This Alley Where I Hide",
                "most_popular_track_plays": 1247
            },
            "thematic_analysis": {
                "theme_distribution": {
                    "Urban Mythology": 320,
                    "Nature Mythology": 180,
                    "Emotional Journey": 210,
                    "Hero Mythology": 150,
                    "Classical Mythology": 80,
                    "General": 244
                },
                "top_themes": [
                    ["Urban Mythology", 320],
                    ["Emotional Journey", 210],
                    ["Nature Mythology", 180],
                    ["Hero Mythology", 150],
                    ["Classical Mythology", 80]
                ],
                "theme_diversity_score": 0.78
            },
            "genre_analysis": {
                "genre_distribution": {
                    "Folk/Acoustic": 280,
                    "Ambient": 190,
                    "Chill/Lo-fi": 150,
                    "Rock/Punk": 120,
                    "Electronic": 180,
                    "Classical": 80,
                    "Mixed": 184
                },
                "top_genres": [
                    ["Folk/Acoustic", 280],
                    ["Ambient", 190],
                    ["Electronic", 180],
                    ["Chill/Lo-fi", 150],
                    ["Rock/Punk", 120]
                ],
                "genre_diversity_score": 0.82
            },
            "mood_analysis": {
                "mood_distribution": {
                    "melancholic": 290,
                    "calm": 210,
                    "joyful": 180,
                    "epic": 150,
                    "energetic": 120,
                    "neutral": 234
                },
                "top_moods": [
                    ["melancholic", 290],
                    ["calm", 210],
                    ["joyful", 180],
                    ["epic", 150],
                    ["energetic", 120]
                ],
                "mood_balance_score": 0.65
            },
            "avatararts_brand": "AvatarArts",
            "artist_identity": "Steven Chaplinski",
            "analysis_timestamp": datetime.now().isoformat()
        }
        return insights
    except Exception as e:
        print(f"Error loading AvatarArts insights: {str(e)}")
        return {}

# Routes
@app.route('/')
def index():
    """Home page"""
    collection = get_avatararts_collection()
    insights = get_avatararts_insights()
    
    return render_template('index.html', 
                         collection=collection, 
                         insights=insights,
                         current_year=datetime.now().year)

@app.route('/about')
def about():
    """About page"""
    collection = get_avatararts_collection()
    return render_template('about.html', 
                         collection=collection,
                         current_year=datetime.now().year)

@app.route('/collection')
def collection():
    """Collection page showing AvatarArts content"""
    collection = get_avatararts_collection()
    insights = get_avatararts_insights()
    
    return render_template('collection.html', 
                         collection=collection,
                         insights=insights,
                         current_year=datetime.now().year)

@app.route('/technology')
def technology():
    """Technology page explaining nocTurneMeLoDieS V4 system"""
    collection = get_avatararts_collection()
    
    tech_info = {
        "v4_features": [
            "Dual Platform Integration (Suno.com & GitHub)",
            "AI-Enhanced Content Analysis",
            "Album-Based Organization System",
            "AvatarArts-Themed Content Grouping",
            "Cross-Platform Content Linking",
            "Advanced Recommendation Engine"
        ],
        "core_technologies": [
            "Python 3.8+",
            "Flask Web Framework",
            "React 18 (Frontend)",
            "PyTorch (AI Models)",
            "Librosa (Audio Analysis)",
            "PostgreSQL (Database)"
        ],
        "integration_points": [
            "Suno.com/@avatararts",
            "GitHub.com/ichoake/AvaTar-Arts",
            "Local nocTurneMeLoDieS System",
            "AI Content Analysis Engine"
        ]
    }
    
    return render_template('technology.html',
                         collection=collection,
                         tech_info=tech_info,
                         current_year=datetime.now().year)

@app.route('/contact')
def contact():
    """Contact page"""
    collection = get_avatararts_collection()
    return render_template('contact.html',
                         collection=collection,
                         current_year=datetime.now().year)

@app.route('/api/collection-stats')
def api_collection_stats():
    """API endpoint for collection statistics"""
    collection = get_avatararts_collection()
    return jsonify(collection)

@app.route('/api/insights')
def api_insights():
    """API endpoint for collection insights"""
    insights = get_avatararts_insights()
    return jsonify(insights)

@app.route('/favicon.ico')
def favicon():
    """Serve favicon"""
    return send_from_directory('../STATIC/IMAGES', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/robots.txt')
def robots():
    """Serve robots.txt"""
    return send_from_directory('../STATIC', 'robots.txt', mimetype='text/plain')

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    collection = get_avatararts_collection()
    return render_template('404.html', collection=collection, current_year=datetime.now().year), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    collection = get_avatararts_collection()
    return render_template('500.html', collection=collection, current_year=datetime.now().year), 500

# Health check endpoint
@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "avatararts-website",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    # For development
    app.run(debug=True, host='0.0.0.0', port=8080)