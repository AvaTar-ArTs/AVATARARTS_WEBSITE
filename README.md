# AvatarArts Website
## Official Website for avatararts.org

The official website for the AvatarArts creative automation platform, showcasing the nocTurneMeLoDieS V4 system developed by Steven Chaplinski.

### Overview

The AvatarArts website serves as the central hub for information about the AvatarArts creative automation platform. The site showcases the nocTurneMeLoDieS V4 system, which integrates content from Suno.com/@avatararts and GitHub.com/ichoake/AvaTar-Arts into a unified, AI-enhanced organization system.

### Features

- **Responsive Design**: Works on all devices from mobile to desktop
- **nocTurneMeLoDieS V4 Integration**: Real-time data from the V4 system
- **Collection Showcase**: Displays the AvatarArts collection with statistics
- **Thematic Organization**: Highlights the creative themes and special collections
- **Technology Showcase**: Explains the underlying technology stack
- **Developer Information**: Details about Steven Chaplinski and the development process

### Special Collections

The website highlights the following signature collections from the AvatarArts collection:

- **Alley Chronicles**: 151+ variations of "In This Alley Where I Hide"
- **Willow Variations**: 47+ versions of "Willow Whispers"
- **Summer Remixes**: 34+ versions of "Summer Love"
- **Hero Collections**: 30+ versions of "Heroes Rise Villains Overthrow"
- **Junkyard Symphonies**: 50+ versions of "Junkyard Symphony"

### Creative Themes

Content is organized around five primary creative themes:

1. **Urban Mythology**: Alley Chronicles, TrashCat, Raccoon themes
2. **Nature Mythology**: Willow Variations, Echoes, Moonlight themes
3. **Emotional Journey**: Summer Love, Beautiful Mess, Heartbeats themes
4. **Hero Mythology**: Heroes Rise Villains Overthrow, Epic themes
5. **Classical Mythology**: Orpheus, Eurydice, Hecate themes

### Technology Stack

- **Backend**: Flask (Python 3.8+)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5, custom CSS
- **Visualization**: Chart.js
- **Deployment**: Gunicorn, Nginx, Docker

### Installation

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

The application uses several environment variables for configuration. See `CONFIG/config.py` for detailed configuration options.

### Deployment

For production deployment, refer to the configuration files in the `DEPLOYMENT/` directory, which include:

- Gunicorn configuration
- Nginx configuration
- Docker configuration
- Docker Compose configuration
- Systemd service file

### API Endpoints

The website provides several API endpoints:

- `GET /api/collection-stats` - Collection statistics
- `GET /api/insights` - Collection insights
- `GET /health` - Health check

### nocTurneMeLoDieS V4 Integration

The website integrates with the nocTurneMeLoDieS V4 system to display real-time data about the AvatarArts collection, including:

- Collection statistics and insights
- Special collections information
- Thematic organization details
- Integration points with Suno and GitHub

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Contact

**Developer**: Steven Chaplinski  
**Brand**: AvatarArts  
**GitHub**: https://github.com/ichoake  
**Suno**: https://suno.com/@avatararts  
**Email**: sjchaplinski@gmail.com  
**Website**: https://avatararts.org  

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Acknowledgments

- Built upon the nocTurneMeLoDieS V4 system
- Inspired by the creative automation engineering approach
- Developed for artists and musicians

### Development

For development purposes, the project includes Node.js tooling:

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Or use the development script directly
./dev-server.sh
```# AVATARARTS_WEBSITE
