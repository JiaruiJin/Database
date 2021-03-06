import pymongo

def user_info():
    screen_name =input("Enter a user name to know: ")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]

    if (mycol.count()==0):
        print("No such user name")
    else:
        for user in mycol.find():
            if (user.get('username')==screen_name):
                print(user)

def search_word():
    word=input("Please enter a word to search for: ")
    print("This user has the word",word,"you search in their description:")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]
    for user in mycol.find():
        descrip=user.get('description')
        descrip=descrip.split(',')
        if word in descrip:
            print(user.get('username'))

def show_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]
    print("There are ",mycol.count(),"users at data base")
    avg_im=0
    desc=[]
    for user in mycol.find():
        print(user)
        avg_im=avg_im+user.get('img_num')
        curr_des=user.get('description').split(',')
        for j in curr_des:
            desc.append(j)
    # if (mycol.count()>0):
    #     print("Some statistics:")
    #     print("The most popular description is",(max(set(desc), key = desc.count)))
    #     print("There is an average of",str(avg_im/mycol.count()),"images per feed")
    return

def delete_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["users"]
    x = mycol.delete_many({})
    return

if __name__ == "__main__":
   user_info()
   search_word()
   show_db()
   delete_db()
