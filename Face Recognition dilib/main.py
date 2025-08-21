import face_recognition

img1 = face_recognition.load_image_file("The Rock.jpg")
img2 = face_recognition.load_image_file("The rockkckck.jpg")

enc1 = face_recognition.face_encodings(img1)[0]
enc2 = face_recognition.face_encodings(img2)[0]

match = face_recognition.compare_faces([enc1], enc2, tolerance = 0.6)[0]
print("SAME PERSON" if match else "DIFFERENT PEOPLE")