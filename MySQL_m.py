# /usr/bin/env python3
import MySQL_DB as MySQL_DB
import pymysql


def get_input_num():
    num = int(input("Enter a number: "))
    return num

def main():
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="Gary", charset="utf8")
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE if not exists  mini_project3")
    mycursor.execute("USE mini_project3")
    mycursor.execute("CREATE TABLE IF NOT EXISTS user_data (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(255), img_num VARCHAR(255),URL VARCHAR(255), description VARCHAR(255),description_num VARCHAR(255))")
    print("Menu:\n1.Search for a username\n2.Search for a word\n3.Show databases \n4.Adder a new user\n5.Delete database\n6.Exit")
    data=get_input_num();
    if (data==1):
        MySQL_DB.user_info(mycursor)
    elif (data==2):
        MySQL_DB.search_word(mycursor)
    elif (data==3):
        MySQL_DB.show_db(mycursor)
    elif (data==4):
        MySQL_DB.add_user(mycursor)
    elif (data==5):
        MySQL_DB.delete_db(mycursor)
    elif (data==6):
        return


if __name__ == "__main__":
  main()
