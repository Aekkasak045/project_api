import mysql.connector

def con():
    mydb = mysql.connector.connect(
    host="localhost",
    user="Work1",
    password="12345",
    database ="Work1"
    )
    return mydb

class Con:
    def getUS():
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getUS_ID(id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM users WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getUS_Add(StudentNumber,Name,LastName):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "INSERT INTO users (StudentNumber,Name,LastName,user_role_id) VALUES ('{}','{}','{}','Member')".format(StudentNumber,Name,LastName)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        ID = mycursor.lastrowid 
        return ID

    def updata_role_id(user_role_id,id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE users SET user_role_id = '{}' WHERE id = {}".format(user_role_id,id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()        
        return True

    def DeleteUS(id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "DELETE FROM users WHERE id = {}".format(id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

class con2:
    def login(user_login):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM user_login WHERE username = '{}' and user_password = '{}'".format(user_login.username,user_login.user_password)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getUser(id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM user_login WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def changePassword_and_Name(user_login):
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE user_login SET user_password = '{}', Name= '{}' WHERE id = {}".format(user_login.user_password,user_login.Name,user_login.id)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True

class con3():
    def get_hw_ID(id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "SELECT * FROM hardware WHERE id = {}".format(id)
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def updata_hardware(status,value,id):
        mydb = con()
        mycursor = mydb.cursor(dictionary=True)
        sql = "UPDATE hardware SET status = '{}' , value= {} WHERE id = {}".format(status,value,id)
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()        
        return True