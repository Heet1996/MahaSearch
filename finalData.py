#import urllib.request
import json
import requests
import pymysql

conn = pymysql.connect(host='localhost',user='root',password='',db='mahasearch',use_unicode=True, charset="utf8")
cursor = conn.cursor()

"""
urls = ["https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMantralayMainNews?id=1&pageindex=1&pagesize=2575","https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMukhyabatmiMainNews?pageindex=1&pagesize=7000","https://www.mahanews.gov.in/webservice/utility/utility.asmx/GetMantralayMainNews?id=1&pageindex=1&pagesize=2500"]
jsons = []
for url in urls:
    uh = urllib.request.urlopen(url)
    data = uh.read()
    st = data.decode("utf-8")
    s = st[76:len(st)-9]
    js = json.loads(s)
    jsons = jsons + js

"""
finalData = []    

with open('JsonData.txt') as json_data:
    finalData = json.load(json_data)


import MySQLdb
import os
from PIL import Image, ImageDraw
import training as face_recognition
names = os.listdir("registered")

known_face_encodings = []
    
for name in names:
    img = face_recognition.load_image_file("registered/"+name)
    known_face_encodings.append(face_recognition.face_encodings(img)[0])

def insert_into_mapping(id, name):
    sql= "Insert into mapping values ("+ id +",'"+ name +"')"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print("mapping error")
        conn.rollback()
    

def insert_into_images(id, news, news_from, from_date, marathi_date, subject, path):
    if news is None:
        news = ""
    if news_from is None:
        news_from = ""
    if from_date is None:
        from_date = ""
    if marathi_date is None:
        marathi_date = ""
    if subject is None:
        subject = ""
    news = news.replace("'","")
    news_from = news_from.replace("'","")
    from_date = from_date.replace("'","")
    marathi_date = marathi_date.replace("'","")
    subject = subject.replace("'","")
    query = "Insert into images values ("+ id +", '"+ news +"', '"+ news_from +"', '"+ from_date +"', '"+ marathi_date +"', '"+ subject +"', '"+ path +"')"
    try:
        cursor.execute(query)
        conn.commit()
    except MySQLdb.Error as e:
        print('Got error {!r}, errno is {}'.format(e, e.args[0]))
        conn.rollback()   

no_of_images = 3970
for i in range(3970,len(finalData)):
    j = finalData[i]
    print(no_of_images)
    image_url = j['imgname']
    img_data = requests.get(image_url).content
    img_path = 'Images/image'+str(no_of_images)+'.jpg'
    with open(img_path, 'wb') as handler:
        handler.write(img_data)
    unknown_image = face_recognition.load_image_file(img_path)
    face_locations = face_recognition.face_locations(unknown_image)
    face_locations = sorted(sorted(face_locations, key = lambda x: x[0]),key = lambda x:x[3])
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    
    count = 1
    pil_image = Image.fromarray(unknown_image)
    draw = ImageDraw.Draw(pil_image)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.45)
        name = "Unknown"
        #for z in range(len(matches)):
            #print(str(matches[z])+" "+names[z])
        index = matches.index(min(matches))
        first_match_index = index
        if matches[index] <= 0.45:
            name = names[first_match_index]
            pos = name.find("(")
            name = name[0:pos-1]
            name = "Honorable "+name
            insert_into_mapping(str(no_of_images), name)
            #print(str(count) + name) 
            name  = str(count)
            count = count+1
            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))
            text_width, text_height = draw.textsize(name)
            #draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left - 8, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
            
    pil_image.save(img_path)        
    del draw
    insert_into_images(str(no_of_images), j['News'], j['NewsFrom'], j['fromdate'], j['marathidate'], j['subject'], img_path)
    no_of_images = no_of_images + 1
conn.close()
cursor.close()


        
        
    
    

    