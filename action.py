from conDb import Con,con2, con3

class Action:
    def getUS():
        data = Con.getUS()
        return data

    def getUSID(id):
        data = Con.getUS_ID(id)
        return data

    def addUS(StudentNumber,Name,LastName):
        ID = Con.getUS_Add(StudentNumber,Name,LastName)
        return ID

    def updataUS(user_role_id,id):
        boolean = Con.updata_role_id(user_role_id,id)
        if(boolean):
            data = Con.getUS_ID
        else:
            data = {"error":True}
        return data
    
    def DeleteUS(id):
        boolean = Con.DeleteUS(id)
        if boolean:
            data = {"error": False, "Delete": "Succeses"}
        else:
            data = {"error": True}
        return data

    def login(user_login):
        user = con2.login(user_login)
        if user:
            data = {"error": False, "user": user}
            return data
        else:
            data = {"error": True}
            return data
            
    def get_hwID(id):
        data = con3.get_hw_ID(id)
        return data

    def updata_hw(status,value,id):
        boolean = con3.updata_hardware(status,value,id)
        if(boolean):
            data = con3.get_hw_ID(id)
        else:
            data = {"error":True}
        return data

    def changePasswordAndName(user_login):
        boolean = con2.changePassword_and_Name(user_login)
        if(boolean):
            data = con2.getUser(user_login.id)
            return data
        else:
            data = {"error": True,}
            return data
