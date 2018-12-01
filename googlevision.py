import io
import os
import os.path
import pymysql
import pymongo

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def label(username,img_num,URL):
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="Gary", db="mini3", charset="utf8")
    mycursor = conn.cursor()
    mycursor.execute("use mini_project3")
    client = vision.ImageAnnotatorClient()
    os.chdir("D:/EC601/mini_project3/@KicksFinder" )
    path=os.getcwd()
    dir=path
    num=0
    for root,dirname,filenames in os.walk(dir):
        for filename in filenames:
            if os.path.splitext(filename)[1]=='.jpg':
                num = num +1

    i=1
    while (i<num+1):
        file_name = os.path.join(os.path.dirname(__file__),path+'/'+str(i)+'.jpg')
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = client.label_detection(image=image)
        descrip=""
        j=0
        # get the labels of corresponding picture
        labels = response.label_annotations
        print('Labels:')
        for label in labels:
            descrip=descrip+ label.description+","
            #insert to mysql db
            sql = "INSERT INTO user_data (username, img_num, URL, description,description_num) VALUES (%s, %s, %s, %s, %s)"
            descrip = descrip[:-1]
            val = (username, img_num, URL, descrip,j)
            mycursor.execute(sql, val)
            conn.commit()

            # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            # mydb = myclient["mydatabase"]
            # mycol = mydb["users"]
            # mydict = { "username": username, "img_num": img_num,"description":descrip,"description_num":j }
            # x = mycol.insert_one(mydict)
            j=j+1
            print(label.description)
            print('==========================')
        i += 1





# if __name__ == '__main__':
#
#   label("@KicksFinder",10)
