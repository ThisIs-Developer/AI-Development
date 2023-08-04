# [OpenCV/Working with Images](https://opencv.org/)
![channels_combined](https://github.com/ThisIs-Developer/Python/assets/109382325/55990dd2-407e-446b-93b6-8ac41d848d9f)
**OpenCV (Open Source Computer Vision Library) is a popular open-source computer vision and image processing library. It provides a wide range of tools and functions that allow developers to work with images and perform various tasks such as image manipulation, analysis, object detection, and more.**
## Installation
```bash
  pip install opencv-python
```
## Image that are used
![GridArt_20230804_220521622](https://github.com/ThisIs-Developer/Python/assets/109382325/c3888daa-f8e1-4f5f-ab05-8f2558848046)
## 🌟OpenCV🎨the Magic of Images
**Addition Image**
```bash
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
if image1.shape[2] == 1:
    image1 = cv2.cvtColor(image1, cv2.COLOR_GRAY2BGR)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
cv2.imshow('Weighted Image', weightedSum)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()

# Convert BGR image to RGB for plotting using matplotlib
weightedSum_rgb = cv2.cvtColor(weightedSum, cv2.COLOR_BGR2RGB)
```
![bitwise_NOT](https://github.com/ThisIs-Developer/Python/assets/109382325/84ec9507-f3e0-4910-81e3-60ce55be17aa)
![bitwise_OR](https://github.com/ThisIs-Developer/Python/assets/109382325/c7b174db-2bac-48a1-b279-88319c6b1584)

