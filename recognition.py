import os
from PIL import Image, ImageDraw
import face_recognition
names = os.listdir("registered")
known_face_encodings = []
    
for name in names:
    img = face_recognition.load_image_file("registered/"+name)
    known_face_encodings.append(face_recognition.face_encodings(img)[0])
result_names = []
unknownImageNames = os.listdir("testing")
unknownImageNames = ["abc.jpg"]
for unknownname in unknownImageNames:
    unknown_image = face_recognition.load_image_file(unknownname)
    face_locations = face_recognition.face_locations(unknown_image)
    face_locations = sorted(sorted(face_locations, key = lambda x: x[0]),key = lambda x:x[3])
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    count = 1
    pil_image = Image.fromarray(unknown_image)
    draw = ImageDraw.Draw(pil_image)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.45)
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = names[first_match_index]
            pos = name.find("(")
            name = name[0:pos-1]
            name = "Honorable "+name
            result_names.append(name)
            name  = str(count)
            count = count+1
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
            text_width, text_height = draw.textsize(name)
            #draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left - 8, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
    if not os.path.exists(name):
        os.makedirs(name)
    pil_image.save("sorted location.jpg")        
    del draw
    break
print(result_names)
