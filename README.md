
# ✈️ AirControl - Gesture-Based Mouse Controller

**Control your computer mouse with hand gestures!** AirControl leverages computer vision and AI to translate your hand movements into precise cursor actions. Perfect for presentations, interactive setups, or just impressing your friends!

[Demo](https://www.linkedin.com/posts/joseph-meghanath-9880ba149_aircontrol-python-computervision-activity-7288136176350216192-Kwa4?utm_source=share&utm_medium=member_desktop)  

## ✨ Features

- **Finger Tracking**: Move the cursor with your index finger
- **Intuitive Clicking**: Pinch thumb and index finger to click
- **Smart Scrolling**: Raise two fingers for smooth vertical scrolling
- **Real-Time Overlay**: Interactive control panel with system stats
- **Customizable Settings**: Fine-tune sensitivity and smoothing
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🛠 Technologies

| Technology       | Role                                   | Version  |
|------------------|----------------------------------------|----------|
| **MediaPipe**    | Hand landmark detection                | 0.9.0+   |
| **OpenCV**       | Real-time video processing             | 4.6.0+   |
| **PyAutoGUI**    | System mouse control                   | 0.9.53+  |
| **NumPy**        | Mathematical operations                | 1.23.3+  |
| **Python**       | Core programming language              | 3.8+     |

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Webcam
- Chrome browser (for best performance)

### Installation
```bash
# Clone repository
git clone https://github.com/JoeHitHard/AirControl.git
cd AirControl

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt


### Launching the Controller
```bash
python main.py
```

## 🖱 Usage Guide

1. **Cursor Movement**:  
   Extend your index finger and move it in front of the camera

2. **Left Click**:  
   Bring thumb and index finger close together (distance < 0.07 by default)

3. **Scrolling**:  
   Raise index and middle fingers together:
   - Move up to scroll down
   - Move down to scroll up

4. **Exit**:  
   Press `ESC` key or close the window

## ⚙️ Configuration

Customize behavior in `config.py`:
```python
# Click sensitivity (lower = more sensitive)
CLICK_CONFIG = {
    'THRESHOLD': 0.07,    # Activation distance (0-1)
    'DEBOUNCE': 0.2,      # Minimum time between clicks
    'HOLD_TIME': 0.15     # Click registration duration
}

# Cursor smoothness (higher = smoother)
SMOOTHENING_FACTOR = 5    # Range 1-10 recommended

# Scroll speed
SCROLL_CONFIG = {
    'MULTIPLIER': 1500,   # Scroll intensity
    'SMOOTHING': 0.8      # Motion fluidity (0-1)
}
```

## 🙌 Acknowledgements

- Original concept by [Joseph Hit Hard](https://github.com/JoeHitHard)
- Hand tracking powered by Google's [MediaPipe](https://mediapipe.dev)
- Icon set from [Flaticon](https://www.flaticon.com)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
*Always respect privacy laws when using camera-based software in public spaces.*

---

**Happy gesturing!** ✋🖥️  
*For support or feature requests, please open an issue on GitHub.*
