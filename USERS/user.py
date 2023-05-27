import USERS.conection_db as conec_db
import datetime
import hashlib

conect = conec_db.conection()
database = conect[0]
cursor = conect[1]



class user:

    def __init__(self, name, last_name, email, passwd):

        self.name = name
        self.last_name = last_name
        self.email = email
        self.passwd = passwd


    def log_in(self):
        sql = "SELECT * FROM users WHERE email = %s AND passwd = %s"

        #encrypt password
        encrypt = hashlib.sha256()
        encrypt.update(self.passwd.encode('utf8'))

        user = (self.email, encrypt.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result  


    def sign_in(self):
        
        #encrypt password
        encrypt = hashlib.sha256()
        encrypt.update(self.passwd.encode('utf8'))

        date = datetime.datetime.now()

        sql = "INSERT INTO users VALUES (null, %s, %s, %s, %s, %s)"
        user = (self.name, self.last_name, self.email, encrypt.hexdigest(), date)


        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result   
