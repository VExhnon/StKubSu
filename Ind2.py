import cv2
import datetime

def webcam():
    video = cv2.VideoCapture(r"http://192.168.43.1:8080/video")
    # video = cv2.VideoCapture(1)
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer1 = cv2.VideoWriter('output_all.mov', fourcc, 25, (w, h))
    video_writer2 = cv2.VideoWriter('output_actions.mov', fourcc, 25, (w, h))

    cur_frame = None
    ok, img = video.read()
    old_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    while (True):

        ok, img = video.read()
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if ok:
            font = cv2.FONT_HERSHEY_SIMPLEX

            dt = str(datetime.datetime.now())

            frame = cv2.putText(img, dt,
                                (30, 30),
                                font, 1,
                                (0, 0, 0),
                                2, cv2.LINE_8)

        cv2.imshow('img', img)
        video_writer1.write(img)


        frame_diff = cv2.absdiff(cur_frame, old_frame)
        ret, thresh = cv2.threshold(frame_diff, 50, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for i in contours:
            if cv2.contourArea(i) > 200:
                video_writer2.write(img)
                break
        old_frame = cur_frame
        if cv2.waitKey(1) & 0xFF == 27:
            break
    video.release()

webcam()