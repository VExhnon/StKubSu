#include <opencv2/opencv.hpp>

using namespace cv;

int main()
{
Mat img = imread("img2.jpg");
Mat hsvImg;
cvtColor(img, hsvImg, COLOR_BGR2HSV);

imshow("RGB image", img);
imshow("HSV image", hsvImg);
waitKey(0);
destroyAllWindows();

return 0;
}
