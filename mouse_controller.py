import pyautogui
import numpy as np
from collections import deque


class MouseController:
    def __init__(self, config):
        self.config = config
        self.prev_x, self.prev_y = pyautogui.position()
        self.click_history = deque(maxlen=config['HISTORY_SIZE'])
        self.last_click_time = 0
        self.scroll_velocity = 0
        self.prev_scroll_y = None

    def move_cursor(self, index_x, index_y, frame_size):
        screen_x = np.interp(index_x, (0, frame_size[0]), (0, self.config['SCREEN_WIDTH']))
        screen_y = np.interp(index_y, (0, frame_size[1]), (0, self.config['SCREEN_HEIGHT']))

        curr_x = self.prev_x + (screen_x - self.prev_x) / self.config['SMOOTHENING']
        curr_y = self.prev_y + (screen_y - self.prev_y) / self.config['SMOOTHENING']

        pyautogui.moveTo(curr_x, curr_y)
        self.prev_x, self.prev_y = curr_x, curr_y

    def handle_click(self, distance, current_time):
        self.click_history.append((current_time, distance))
        valid_clicks = [d for t, d in self.click_history
                        if (current_time - t) < self.config['HOLD_TIME']]

        if not valid_clicks:
            return False

        avg_distance = np.mean(valid_clicks)
        if avg_distance < self.config['THRESHOLD']:
            if (current_time - self.last_click_time) > self.config['DEBOUNCE']:
                pyautogui.click()
                self.last_click_time = current_time
                return True
        return False

    def handle_scroll(self, current_y):
        if self.prev_scroll_y is None:
            self.prev_scroll_y = current_y
            return

        delta_y = (self.prev_scroll_y - current_y) * self.config['MULTIPLIER']
        self.scroll_velocity = self.scroll_velocity * self.config['SMOOTHING'] + delta_y * (
                    1 - self.config['SMOOTHING'])
        pyautogui.scroll(int(self.scroll_velocity))
        self.prev_scroll_y = current_y