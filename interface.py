import cv2


class InterfaceManager:
    @staticmethod
    def draw_control_panel(image, distance, clicking, config):
        cv2.rectangle(image, (10, 10), (300, 160), (50, 50, 50), -1)
        color = (0, 255, 0) if clicking else (0, 0, 255)
        status = "ACTIVE" if clicking else "INACTIVE"

        texts = [
            (f"CLICK: {status}", (20, 40), color, 0.6, 2),
            (f"Distance: {distance:.3f}", (20, 75), (200, 200, 200), 0.5, 1),
            (f"Threshold: {config['THRESHOLD']:.3f}", (20, 100), (200, 200, 200), 0.5, 1),
            ("Press 'C' to calibrate", (20, 135), (200, 200, 255), 0.5, 1),
            ("Press ESC to quit", (20, 160), (200, 200, 255), 0.5, 1)
        ]

        for text, pos, color, scale, thickness in texts:
            cv2.putText(image, text, pos, cv2.FONT_HERSHEY_SIMPLEX,
                        scale, color, thickness)

    @staticmethod
    def draw_distance_line(image, start, end, color):
        cv2.line(image, start, end, color, 2)