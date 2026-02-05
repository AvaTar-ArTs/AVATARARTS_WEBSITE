# AvatarArts Website Documentation
## Official Website for avatararts.org

### Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Development](#development)
6. [Deployment](#deployment)
7. [API Documentation](#api-documentation)
8. [nocTurneMeLoDieS V4 Integration](#nocturnemelodies-v4-integration)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)

### Overview

The AvatarArts website (avatararts.org) is a Flask-based web application that serves as the official website for the AvatarArts creative automation platform. The site showcases the nocTurneMeLoDieS V4 system and provides information about the creative automation tools developed by Steven Chaplinski.

#### Key Features
- Responsive design optimized for all devices
- Integration with nocTurneMeLoDieS V4 system
- Dynamic content from the AvatarArts collection
- Interactive visualizations of collection data
- Clean, modern UI with accessibility in mind

#### Technology Stack
- **Backend**: Flask (Python 3.8+)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5, custom CSS
- **Visualization**: Chart.js
- **Deployment**: Gunicorn, Nginx, Docker

### Architecture

#### Directory Structure
```
AVATARARTS_WEBSITE/
├── CORE/                    # Core application files
│   ├── APP/                # Main Flask application
│   ├── MODELS/             # Data models (if using database)
│   ├── SERVICES/           # Business logic services
│   ├── UTILS/              # Utility functions
│   └── API/                # API endpoints
├── TEMPLATES/              # Jinja2 templates
│   ├── LAYOUTS/            # Layout templates
│   ├── PAGES/              # Page templates
│   └── COMPONENTS/         # Reusable components
├── STATIC/                 # Static assets
│   ├── CSS/                # Stylesheets
│   ├── JS/                 # JavaScript files
│   ├── IMAGES/             # Image assets
│   ├── FONTS/              # Font files
│   └── ASSETS/             # Other assets
├── CONFIG/                 # Configuration files
├── DEPLOYMENT/             # Deployment configurations
├── DOCUMENTATION/          # Documentation files
└── README.md               # Project documentation
```

#### Application Flow
1. User requests a page from the Flask application
2. Flask routes the request to the appropriate handler
3. Handler retrieves data from nocTurneMeLoDieS V4 system
4. Handler renders the appropriate template with data
5. Flask returns the rendered HTML to the user

### Installation

#### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

#### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/ichoake/avatararts-website.git
   cd avatararts-website
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r CONFIG/requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp CONFIG/.env.example CONFIG/.env
   # Edit CONFIG/.env with your configuration
   ```

5. Run the development server:
   ```bash
   python CORE/APP/app.py
   ```

6. Visit `http://localhost:5000` in your browser

### Configuration

#### Environment Variables
The application uses several environment variables for configuration:

- `FLASK_ENV`: Development environment (`development` or `production`)
- `FLASK_DEBUG`: Enable/disable debug mode
- `AVATARARTS_SECRET_KEY`: Secret key for session management
- `NOCTURNEMELODIES_PATH`: Path to nocTurneMeLoDieS system
- `AVATARARTS_V4_PATH`: Path to V4 integration system
- `SUNO_API_KEY`: API key for Suno integration
- `GITHUB_TOKEN`: Token for GitHub integration

#### Configuration File
See `CONFIG/config.py` for detailed configuration options.

### Development

#### Running in Development Mode
```bash
export FLASK_ENV=development
export FLASK_DEBUG=true
python CORE/APP/app.py
```

#### Frontend Development
- CSS files are located in `STATIC/CSS/`
- JavaScript files are located in `STATIC/JS/`
- Templates are located in `TEMPLATES/`

#### Code Standards
- Use 4 spaces for indentation
- Follow PEP 8 for Python code
- Use semantic HTML
- Follow BEM methodology for CSS classes
- Write accessible HTML

### Deployment

#### Production Deployment
For production deployment, use the configuration files in the `DEPLOYMENT/` directory:

1. **Gunicorn Configuration**: Use `gunicorn.conf.py` for WSGI server configuration
2. **Nginx Configuration**: Use the provided Nginx configuration for reverse proxy
3. **Docker Configuration**: Use `Dockerfile` and `docker-compose.yml` for containerized deployment
4. **Systemd Service**: Use the systemd service file for process management

#### Deployment Checklist
- [ ] Set `FLASK_ENV=production`
- [ ] Configure SSL certificates
- [ ] Set up environment variables securely
- [ ] Configure static file serving
- [ ] Set up logging
- [ ] Configure backup procedures
- [ ] Set up monitoring

### API Documentation

The website provides several API endpoints for retrieving data:

#### GET /api/collection-stats
Returns statistics about the AvatarArts collection.

**Response:**
```json
{
  "total_tracks": 1184,
  "total_albums": 665,
  "total_repositories": 12,
  "avatararts_repositories": 3,
  "special_collections": {...},
  "avatararts_themes": [...],
  "suno_integration": {...},
  "github_integration": {...},
  "last_updated": "2026-01-30T10:30:00Z"
}
```

#### GET /api/insights
Returns insights about the AvatarArts collection.

**Response:**
```json
{
  "collection_overview": {...},
  "thematic_analysis": {...},
  "genre_analysis": {...},
  "mood_analysis": {...},
  "avatararts_brand": "AvatarArts",
  "artist_identity": "Steven Chaplinski",
  "analysis_timestamp": "2026-01-30T10:30:00Z"
}
```

#### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-01-30T10:30:00Z",
  "service": "avatararts-website",
  "version": "1.0.0"
}
```

### nocTurneMeLoDieS V4 Integration

#### Integration Points
The website integrates with the nocTurneMeLoDieS V4 system in several ways:

1. **Data Retrieval**: The website retrieves collection data from the V4 system
2. **Statistics Display**: Shows real-time statistics from the V4 system
3. **Content Organization**: Reflects the album-based organization of the V4 system
4. **Thematic Grouping**: Displays content organized by AvatarArts themes

#### V4 System Features Showcased
- **Album-Based Organization**: Each song becomes its own album with all variations
- **Special Collections**: Alley Chronicles, Willow Variations, Summer Remixes, etc.
- **Thematic Content Grouping**: Urban Mythology, Nature Mythology, etc.
- **AI Enhancement**: Content analysis and recommendations
- **Cross-Platform Integration**: Suno and GitHub integration

#### AvatarArts-Specific Content
The website highlights the following AvatarArts-specific content:

**Special Collections:**
- Alley Chronicles: 151+ variations of "In This Alley Where I Hide"
- Willow Variations: 47+ versions of "Willow Whispers"
- Summer Remixes: 34+ versions of "Summer Love"
- Hero Collections: 30+ versions of "Heroes Rise Villains Overthrow"
- Junkyard Symphonies: 50+ versions of "Junkyard Symphony"

**Creative Themes:**
- Urban Mythology: Alley, street, urban legends
- Nature Mythology: Willow, nature, ethereal themes
- Emotional Journey: Summer, love, beautiful mess themes
- Hero Mythology: Epic, heroic, dramatic themes
- Classical Mythology: Orpheus, Eurydice, Hecate themes

### Troubleshooting

#### Common Issues

**Issue**: Application won't start
**Solution**: Check that all dependencies are installed and environment variables are set correctly.

**Issue**: Templates not rendering
**Solution**: Verify that template paths are correct and Flask is configured to find templates.

**Issue**: Static files not loading
**Solution**: Check that static file paths are configured correctly in Flask.

**Issue**: Data not loading from V4 system
**Solution**: Verify that the path to the V4 system is correctly configured and accessible.

#### Debugging Tips
- Enable Flask debug mode for detailed error messages
- Check application logs for error details
- Verify all environment variables are set
- Test API endpoints independently
- Use browser developer tools to inspect network requests

### Contributing

#### Development Workflow
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

#### Code Review Process
- All submissions require review
- Follow the project's code style
- Include tests for new functionality
- Update documentation as needed

#### Reporting Issues
- Use the GitHub issue tracker
- Provide detailed steps to reproduce
- Include environment information
- Suggest possible solutions if known

### Contact Information

**Developer**: Steven Chaplinski  
**Brand**: AvatarArts  
**GitHub**: https://github.com/ichoake  
**Suno**: https://suno.com/@avatararts  
**Email**: sjchaplinski@gmail.com  
**Website**: https://avatararts.org  

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

- The AvatarArts website is built upon the nocTurneMeLoDieS V4 system
- Special thanks to the open-source community for Flask, Bootstrap, and other tools
- Gratitude to Steven Chaplinski for the creative vision behind AvatarArts