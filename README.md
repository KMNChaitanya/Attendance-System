# Facial Recognition Attendance-System
## Description
A facial recognition attendance system is a biometric solution that automates the process of recording attendance using facial recognition technology. Here are the key points:

1. How It Works:
   - The system detects and identifies faces of individuals (such as students or employees) present in a class or workplace.
   - It registers their attendance by comparing their facial features with stored profiles.
   - The recorded attendance information is typically transmitted to a central server, which computes attendance data and updates a database.

2. Components:
   - Face Detection: The system locates faces in images or video streams.
   - Feature Extraction: It extracts unique features from facial images.
   - Face Matching: Compares detected faces with stored profiles.
   - Liveness Detection: Prevents spoofing by verifying that the face is live (not a photograph or video).

3. Applications:
   - Education: Used in schools, colleges, and universities for student attendance.
   - Workplaces: Tracks employee attendance in offices, factories, and other organizations.
   - **Events**: Manages attendance at conferences, seminars, and workshops.

In summary, facial recognition attendance systems enhance efficiency, accuracy, and security in attendance management. 

## TechStack Used
1. Image Processing and Recognition Libraries:
   - OpenCV: A powerful open-source computer vision library that provides tools for image processing, face detection, and feature extraction.
   - Dlib: A C++ library with Python bindings for machine learning, including facial recognition and feature extraction.
2. Programming Languages:
   - Python: Widely used for its simplicity, extensive libraries, and community support. Python is the primary language for implementing facial recognition
   algorithms.
3. Additional Libraries and Tools:
   - Numpy and Pandas: For data manipulation and analysis.
   - Face Encodings: Used to represent facial features numerically for comparison.
## Libraries and Dependencies Required
1. Install all these libraries from cmd:
   - OpenCv-python
   - dilib
   - cmake
   - numpy
   - pandas
   - face_recognition
     ```bash
        pip install OpenCv-python dilib cmake numpy pandas face_recognition
     ```
2. Download the python compiler to run it in the VScode.

## How to run the code
1.)First please download the libraries of python which are face_recognition , dilib , opencv-python , numpy , Python compiler for VsCode.

2.)Now create a folder in the desktop named byteverse and copy these files of photos and maincode in it.

3.)Now in this maincode give the locations of the images in it.

4.)Now run the code using vs code.

5.)Now bring the faces which were given in the photos folder onto the webcam and their attendance will be marked.

6.)Now this marked attendance list is shown on the Excel file which is created in our byteverse folder only which is in the desktop.
