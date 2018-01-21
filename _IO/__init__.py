import cv2
import numpy as np
from matplotlib import pyplot as plt


def display(images, labels, rows = 2, cols = 2, fg = 1):
	plt.figure(fg)
	for i in xrange(len(images)) :
		images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
		plt.subplot(rows , cols, i + 1),plt.imshow(images[i])
		plt.title(labels[i])
		plt.xticks([]),plt.yticks([])

def readMatrix(fp) :
	lines = list(fp)
	matrix = []
	for line in lines:
		line = line.replace('\n', '')
		line = line.split('\t')
		matrix.append(map(float, line))
	return matrix


class VideoReader:
    def __init__(self, path, size_ratio=None, size=None, out_path=None):
        self.cap = cv2.VideoCapture(path)
        self.frame_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.size_ratio = size_ratio
        self.re_size = size
        self.out_path = out_path
        self.out = None

    def display(self):
        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            if ret == True:

                if self.re_size is not None:
                    frame = cv2.resize(frame, (self.re_size[0], self.re_size[1]))
                if self.size_ratio is not None:
                    frame = cv2.resize(frame, (int(frame.shape[1] * self.size_ratio), int(frame.shape[1])))
                cv2.imshow('frame', frame)
                if self.out_path is not None:
                    if self.out is None:
                        fourcc = cv2.VideoWriter_fourcc(*'XVID')
                        self.out = cv2.VideoWriter('output.avi', fourcc, self.fps,
                                                   (frame.shape[1], frame.shape[0]))
                    self.out.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        self.cap.release()
        self.out.release()


# code test
# reader = VideoReader(path='My Movie.mp4', size=(1920, 1080), out_path='test_out.mp4')
# reader.display()
# print(reader.fps)