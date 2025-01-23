import cv2
import time
import mediapipe as mp

from config import configure_logging, CLICK_CONFIG, SCROLL_CONFIG, SMOOTHENING_FACTOR, CAMERA_WIDTH, CAMERA_HEIGHT, \
    SCREEN_WIDTH, SCREEN_HEIGHT
from hand_processor import HandProcessor
from mouse_controller import MouseController
from interface import InterfaceManager

logger = configure_logging()


def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, CAMERA_WIDTH)
    cap.set(4, CAMERA_HEIGHT)

    hand_processor = HandProcessor()
    mouse_controller = MouseController({
        **CLICK_CONFIG,
        **SCROLL_CONFIG,
        'SCREEN_WIDTH': SCREEN_WIDTH,
        'SCREEN_HEIGHT': SCREEN_HEIGHT,
        'SMOOTHENING': SMOOTHENING_FACTOR
    })

    try:
        logger.info("Starting main control loop")
        start_time = time.time()
        frame_count = 0

        while True:
            success, image = cap.read()
            if not success:
                logger.warning("Frame capture failed")
                continue

            frame_count += 1
            image = cv2.flip(image, 1)
            results = hand_processor.process_frame(image)
            current_time = time.time()
            clicking = False

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    raised_fingers = hand_processor.count_raised_fingers(hand_landmarks)
                    hand_processor.draw_landmarks(image, hand_landmarks)

                    if raised_fingers == 1:
                        index_pos = hand_processor.get_landmark_position(
                            hand_landmarks, mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP,
                            (CAMERA_WIDTH, CAMERA_HEIGHT)
                        )
                        mouse_controller.move_cursor(*index_pos, (CAMERA_WIDTH, CAMERA_HEIGHT))

                        distance = hand_processor.calculate_click_distance(hand_landmarks)
                        clicking = mouse_controller.handle_click(distance, current_time)

                        thumb_pos = hand_processor.get_landmark_position(
                            hand_landmarks, mp.solutions.hands.HandLandmark.THUMB_TIP,
                            (CAMERA_WIDTH, CAMERA_HEIGHT)
                        )
                        InterfaceManager.draw_distance_line(
                            image, index_pos, thumb_pos,
                            (0, 255, 0) if clicking else (0, 0, 255)
                        )

                    elif raised_fingers == 2:
                        scroll_y = hand_processor.get_scroll_position(hand_landmarks)
                        mouse_controller.handle_scroll(scroll_y)

            InterfaceManager.draw_control_panel(
                image,
                distance if 'distance' in locals() else 0,
                clicking,
                CLICK_CONFIG
            )

            cv2.imshow('Hand Control System', image)
            if cv2.waitKey(5) == 27:
                break

    except Exception as e:
        logger.critical(f"Critical error: {str(e)}", exc_info=True)
    finally:
        cap.release()
        cv2.destroyAllWindows()
        duration = time.time() - start_time
        logger.info(f"Session duration: {duration:.1f}s, FPS: {frame_count / duration:.1f}")


if __name__ == "__main__":
    main()