# app.py

import numpy as np
import cvlib as cv
from cvlib.object_detection import draw_bbox
import streamlit as st
from PIL import Image
from collections import Counter

st.write(Counter.__version__)

# Streamlit app title
st.set_page_config(page_title="Object Detection App", page_icon="🖼️", layout="centered")
st.title("Object Detection with cvlib 🖼️")

# Custom header and instructions
st.markdown("""
### Detect Objects in Your Images
Upload an image to automatically detect common objects and get a count of each detected object. 
The application will display the image with bounding boxes around the objects.
""")

# Upload image
st.markdown("### Step 1: Upload an Image for Object Detection")
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert image file to OpenCV format
    image = np.array(Image.open(uploaded_file))

    # Perform object detection
    box, label, count = cv.detect_common_objects(image)
    
    # Draw bounding boxes on the image
    output_image = draw_bbox(image, box, label, count)
    
    # Step 2: Display image with bounding boxes
    st.markdown("### Step 2: Detected Objects in the Image")
    st.image(output_image, channels="BGR", use_column_width=True)
    
    # Step 3: Display the count of detected objects dynamically
    st.markdown("### Step 3: Detected Objects Count")
    
    # Count each label in the image using Counter
    label_counts = Counter(label)
    
    # Display counts in a well-formatted table
    for obj, count in label_counts.items():
        st.markdown(f"**{obj.capitalize()}s**: {count}")
        
    st.markdown("""
    ---
    ### Tips:
    - You can upload different images to see how the object detection model works.
    - Supported formats: PNG, JPG, JPEG.
    - The app uses cvlib to detect common objects in the images, such as people, cars, trucks, and more.
    """)

# Display a footer
st.markdown("""
---
Made with ❤️ by [SenasuDemir](https://github.com/SenasuDemir).
""")
