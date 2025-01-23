import logging
from datetime import datetime
import pyautogui

# Logging configuration
def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'handcontrol_{datetime.now().strftime("%Y%m%d_%H%M")}.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger('HandControl')

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
CAMERA_WIDTH, CAMERA_HEIGHT = 640, 480

CLICK_CONFIG = {
    'THRESHOLD': 0.07,
    'DEBOUNCE': 0.2,
    'HOLD_TIME': 0.15,
    'HISTORY_SIZE': 10
}

SCROLL_CONFIG = {
    'THRESHOLD': 0.008,
    'SMOOTHING': 0.8,
    'MULTIPLIER': 1500
}

SMOOTHENING_FACTOR = 5