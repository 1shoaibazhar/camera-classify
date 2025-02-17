import cv2 as cv

class Camera:

    def __init__(self):
        self.camera = cv.VideoCapture(0, cv.CAP_AVFOUNDATION)
        if not self.camera.isOpened():
            raise ValueError("Could not open video camera")
        
        self.width = 640  # Example: Reduce width
        self.height = 480  # Example: Reduce height
        self.camera.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
        self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)

        # Resize the OpenCV window
        cv.namedWindow("Camera", cv.WINDOW_NORMAL)
        cv.resizeWindow("Camera", self.width, self.height)
        
    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()
            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (False, None)