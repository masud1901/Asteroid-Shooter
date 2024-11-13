# 🚀 Asteroid Shooter

A classic arcade-style space shooter game built with Python and Pygame. Defend against incoming asteroids, collect power-ups, and aim for the highest score!

## 🎮 Game Features

- Mouse-controlled spaceship movement
- Progressive difficulty system
- Explosion animations and particle effects
- Sound effects and background music
- Multiple game states (Welcome, Playing, Game Over)
- Score tracking system

## 🛠️ Requirements

- Python 3.8+
- Pygame 2.6+
- PyInstaller (for building executables)

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/asteroid-shooter.git
cd asteroid-shooter
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 How to Play

1. Run the game:
```bash
python main.py
```

2. Controls:
   - Move ship: Mouse movement
   - Shoot: Left mouse click
   - Start/Restart: Left mouse click

## 🏗️ Building Executables

Build standalone executables for different platforms:

### Windows
```bash
python build.py
# Output: dist/AsteroidShooter.exe
```

### Linux
```bash
python build.py
# Output: dist/AsteroidShooter
```

### macOS
```bash
python build.py
# Output: dist/AsteroidShooter.app
```

## 📁 Project Structure

```
asteroid-shooter/
├── main.py              # Main game file
├── components.py        # Game components (Ship, Laser, etc.)
├── settings.py          # Game settings and configurations
├── utils.py            # Utility functions
├── build.py            # Build script
├── main.spec           # PyInstaller specification
├── requirements.txt    # Python dependencies
└── space shooter/      # Assets directory
    ├── audio/         # Sound effects and music
    └── images/        # Sprites and textures
```

## 🔧 Development

To modify the game:
1. Make your changes
2. Test locally with `python main.py`
3. Build executable with `python build.py`
4. Test the built executable

## 📦 Distribution

After building:
1. Windows: Share `dist/AsteroidShooter.exe`
2. Linux: Share `dist/AsteroidShooter`
3. macOS: Share `dist/AsteroidShooter.app`

Users don't need Python installed to run the executables.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Credits

- Game assets: [List your asset sources]
- Built with [Pygame](https://www.pygame.org/)
- Font: Oxanium Bold

## 📞 Contact

Akmol Masud Ayon - akmolmasud@gmail.com
