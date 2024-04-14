import cv2
import face_recognition
import pandas as pd
from datetime import datetime
import os

# Load known student images and encode their faces
known_students = {}
known_students["Tesla"] = face_recognition.face_encodings(face_recognition.load_image_file("photos/tesla.jpg"))[0]
known_students["SteveJobs"] = face_recognition.face_encodings(face_recognition.load_image_file("photos/stevejobs.jpg"))[0]
# known_students["Nikhil"] = face_recognition.face_encodings(face_recognition.load_image_file(""))[0]
# known_students["Chaitanya"] = face_recognition.face_encodings(face_recognition.load_image_file(""))[0]


# Initialize attendance dictionary
attendance = {student: False for student in known_students}

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Set the desired frame rate (e.g., 30 frames per second)
desired_fps = 30
video_capture.set(cv2.CAP_PROP_FPS, desired_fps)

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
        # Compare the face encoding with known student encodings
        matches = face_recognition.compare_faces(list(known_students.values()), face_encoding)

        if True in matches:
             # Identify the student
            student_name = list(known_students.keys())[matches.index(True)]
            attendance[student_name] = True

            # Draw a green frame around the recognized face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, student_name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Video', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture
video_capture.release()
cv2.destroyAllWindows()

# Create a CSV file for attendance
attendance_df = pd.DataFrame({"Student": list(attendance.keys()), "Attendance": ["Present" if v else "Absent" for v in attendance.values()]})
attendance_df["Date"] = datetime.now().strftime("%Y-%m-%d")
attendance_df.to_csv("attendance.csv", index=False)

print("Attendance marked and saved to attendance.csv")
