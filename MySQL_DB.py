# /usr/bin/env python3
import pymysql
import getpics as getpics

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="Gary", db="mini3", charset="utf8")
mycursor = conn.cursor()
mycursor.execute("CREATE DATABASE if not exists  mini_project3")
mycursor.execute("USE mini_project3")
mycursor.execute("CREATE TABLE IF NOT EXISTS user_data (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255), img_num VARCHAR(255),URL VARCHAR(255), description VARCHAR(255),description_num VARCHAR(255))")


def user_info(mycursor):
    screen_name =input("Enter a user name to know: ")
    mycursor.execute("SELECT * FROM user_data WHERE username='"+screen_name+"'")
    myresult = mycursor.fetchall()
    if (len(myresult)==0):
        print("No such user name")
    else:
        for user in myresult:
            print(user)

def search_word(mycursor):
    word = input("Please enter a word to search for: ")
    mycursor.execute(("SELECT * FROM user_data"))
    myresult = mycursor.fetchall()
    print("This user has the word",word,"you search in their description:")
    for user in myresult:
        descrip=user[3]
        descrip=descrip.split(',')
        if word in descrip:
            print(user[1])

def show_db(mycursor):
    mycursor.execute(("SELECT * FROM user_data"))
    myresult = mycursor.fetchall()
    print("There are ",len(myresult),"users at data base")
    avg_im=0
    desc=[]
    for user in myresult:
        avg_im=avg_im+int(user[2])
        curr_des=user[3].split(',')
        for j in curr_des:
            desc.append(j)
        print(user)
    if (len(myresult)>0):
        print("The most popular description is",(max(set(desc), key = desc.count)))
        print("There is an average of",str(avg_im/len(myresult)),"images per feed")
    return

def add_user(mycursor):
    screen_name = input("Enter a user name: ")
    mycursor.execute("SELECT * FROM user_data WHERE username='"+screen_name+"'")
    myresult = mycursor.fetchall()
    if (len(myresult)!=0):
        print("The name is used.")
        return
    print("downloading image from" + screen_name)
    imgs = getpics.get_all_tweets(screen_name)
    return  imgs

def delete_db(mycursor):
    mycursor.execute("truncate user_data;")
    return

# if __name__ == "__main__":
#     user_info(mycursor)
#     search_word(mycursor)
#     show_db(mycursor)
#     add_user(mycursor)
#     delete_db(mycursor)
