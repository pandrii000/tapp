import cv2


class Tracker:
    def __init__(self):
        self.lk_params = dict(
            winSize=(15, 15),
            maxLevel=2,
            criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
        )
        self.prev_points = None
        self.prev_gray = None

    def start_tracking(self, frame, points):
        self.prev_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.prev_points = points

    def track(self, frame):
        if self.prev_points is None:
            return None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        next_points, status, _ = cv2.calcOpticalFlowPyrLK(
            self.prev_gray, gray, self.prev_points, None, **self.lk_params
        )

        good_new = next_points[status == 1]
        good_old = self.prev_points[status == 1]

        self.prev_gray = gray.copy()
        self.prev_points = good_new.reshape(-1, 1, 2)

        return good_new, good_old
