#include <iostream> 
#include <opencv2/opencv.hpp> 
using namespace std;
using namespace cv;

int main() 
{ 
	Mat image; 
	image = imread("test.jpeg", 1); 
	 imshow("Image", image); 
	//cvtColor(image,image,COL
	OR_RGB2HSV);
	
	if (!image.data)
	 { 
	 	cout << "No image data \n"; 
	 	return -1;
	 } 
	 namedWindow("Image", WINDOW_AUTOSIZE);
	 imshow("Image1", image); 
	 	waitKey(0); 
	 return 0;
	 }
	  
