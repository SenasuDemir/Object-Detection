# 🚗🦴 Object Detection & Counting using CVlib

## 📌 Overview
This project uses **CVlib** and **OpenCV** to detect and count common objects in images. The program can identify objects like **cars, people, trucks, cats, and dogs** and display bounding boxes around them. 🏎️🐕

## 🖼️ Example Images & Object Counting
The project processes images and outputs the detected objects along with their counts.

### 🏎️ Example 1: Counting Cars, People, and Trucks
```python
image=cv2.imread('cars2.png')
box,label,count=cv.detect_common_objects(image)
output=draw_bbox(image,box,label,count)
plt.imshow(output)
plt.show()
print("Number of cars in this image are " +str(label.count('car')))
print("Number of person in this image are " +str(label.count('person')))
print("Number of truck in this image are " +str(label.count('truck')))
```

### 🐶 Example 2: Counting Cats and Dogs
```python
image=cv2.imread('animal.jpg')
box,label,count=cv.detect_common_objects(image)
output=draw_bbox(image,box,label,count)
plt.imshow(output)
plt.show()
print("Number of cat in this image are " +str(label.count('cat')))
print("Number of dog in this image are " +str(label.count('dog')))
```

## 🛠️ Installation
Make sure you have Python and the required dependencies installed:
```bash
pip install opencv-python numpy matplotlib cvlib
```

## 🎯 Features
✅ Detects common objects in an image using **CVlib** (built on YOLO)
✅ Draws bounding boxes around detected objects
✅ Counts objects like **cars, people, trucks, cats, and dogs**
✅ Displays the processed image using **Matplotlib**

## 🚀 Try it Online
You can test this project online at **Hugging Face Spaces**:
🔗 [Count Objects in Image](https://huggingface.co/spaces/Senasu/Count_Object_In_Image)

## 🖥️ Running the Code
Run the Python script in a Jupyter Notebook or Python environment:
```python
python object_count.py
```

## 📌 Output Example
After running the script, you will see:
```
Number of cars in this image are 3
Number of persons in this image are 2
Number of trucks in this image are 1
```

## 👩‍💻 Author
Made with ❤️ by **Senasu Demir** 🚀
