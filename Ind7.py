import cv2
import numpy as np
import imutils
from matplotlib import pyplot as pl
import time
import datetime

def main1():
    name_videosos = "vid"
    cap = cv2.VideoCapture(f"C:/Users/rzarg/PycharmProjects/ind7/vid.mp4")
    # ret, frame = video.read()  # Берёт первый кадр
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # куда видео записывать
    cap_writer = cv2.VideoWriter(f"C:/Users/rzarg/PycharmProjects/ind7/v230.mp4", fourcc, 25, (w, h))
    old = datetime.datetime.now()
    old = float(old.strftime('%M:%S.%f')[:-4].split(':')[1])
    i = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        now = datetime.datetime.now()
        now = float(now.strftime('%M:%S.%f')[:-4].split(':')[1])
        if(now - old >= .0): # здесь меняем время задержку, то есть через сколько следующее видео брать
            old = now
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 30, 200)

            cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cont = imutils.grab_contours(cont)
            cont = sorted(cont, key=cv2.contourArea, reverse=True)[:8]
            pos = np.zeros(gray.shape, np.uint8)
            for c in cont:
                approx = cv2.approxPolyDP(c, 10, True)
                if len(approx) == 4:
                    pos = approx
                    break
            if(pos.any()!= 0): # проверка на то, что нашёл ли он контур
                mask = np.zeros(gray.shape, np.uint8)
                new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
                bitwisw_img = cv2.bitwise_and(frame, frame, mask=mask)

                (x, y) = np.where(mask == 255)
                (x1, y1) = (np.min(x), np.min(y))
                (x2, y2) = (np.max(x), np.max(y))
                cropp = gray[x1:x2, y1:y2]  # тут хранится фотка номеров!
                final_img = cv2.cvtColor(cv2.rectangle(frame, (y1, x1), (y2, x2), (0, 255, 0), 2), cv2.COLOR_BGR2RGB)
                now1 = datetime.datetime.now()
                # ставим время
                cv2.putText(final_img,str(now1),(w-500,h-100), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),8,cv2.LINE_AA)
                # time.sleep(0.3)
                cv2.imshow('img',final_img)
                cv2.imwrite(f'C:/Users/rzarg/PycharmProjects/ind7/img2/_out_img_{i}.jpg',cropp)
                i+=1
                cap_writer.write(final_img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap_writer.release()
                cap.release()
                break

    cap_writer.release()
    cap.release()
    cv2.destroyAllWindows()


main1()
