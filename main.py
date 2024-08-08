import cv2
from tapp.camera import Camera
from tapp.keyboard_input import KeyboardInput
from tapp.streamer import Streamer
from tapp.tracker import Tracker


def main():
    camera = Camera()
    tracker = Tracker()
    streamer = Streamer(640, 480)  # Adjust width and height as necessary
    keyboard_input = KeyboardInput()

    running = True
    while running:
        frame = camera.read_frame()
        if frame is None:
            break

        running = keyboard_input.check_key()
        tracking = keyboard_input.is_tracking()

        if tracking:
            if tracker.prev_points is None:
                init_points = cv2.goodFeaturesToTrack(
                    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 100, 0.3, 7, blockSize=7
                )
                tracker.start_tracking(frame, init_points)
            else:
                points_new, points_old = tracker.track(frame)
                streamer.show_frame(frame, points_new)
        else:
            streamer.show_frame(frame)

    camera.release()
    streamer.close()


if __name__ == "__main__":
    main()
