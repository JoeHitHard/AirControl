import cv2
import mediapipe as mp
from math import sqrt

from config import configure_logging

logger = configure_logging()

class HandProcessor:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands


    def process_frame(self, image):
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb_image)

    @staticmethod
    def count_raised_fingers(hand_landmarks):
        raised = 0
        tip_ids = [8, 12, 16, 20]  # Finger tip landmarks

        for tip_id in tip_ids:
            tip = hand_landmarks.landmark[tip_id]
            pip = hand_landmarks.landmark[tip_id - 2]
            mcp = hand_landmarks.landmark[tip_id - 3]

            if tip.y < pip.y < mcp.y:
                raised += 1
        return raised

    @staticmethod
    def get_landmark_position(hand_landmarks, landmark_id, frame_size):
        landmark = hand_landmarks.landmark[landmark_id]
        return (int(landmark.x * frame_size[0]), int(landmark.y * frame_size[1]))

    @staticmethod
    def calculate_click_distance(hand_landmarks):
        index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
        thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
        return sqrt((index_tip.x - thumb_tip.x)**2 + (index_tip.y - thumb_tip.y)**2)

    def draw_landmarks(self, image, hand_landmarks):
        self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

    @staticmethod
    def get_scroll_position(hand_landmarks):
        """Calculate average vertical position of index and middle fingers"""
        try:
            index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]
            return (index_tip.y + middle_tip.y) / 2
        except Exception as e:
            logger.error(f"Scroll position error: {str(e)}")
            return 0