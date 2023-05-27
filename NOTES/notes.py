import USERS.conection_db as c_db

connect = c_db.conection()
database = connect[0]
cursor = connect[1]



class note:

    def __init__(self, user_id, title="", note_txt=""):

        self.user_id = user_id
        self.title = title
        self.note_txt = note_txt

    def save(self):
        sql = "INSERT INTO notes VALUES (null, %s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.note_txt)

        cursor.execute(sql, note)
        database.commit()

        return cursor.rowcount, self

    
    def show(self):

        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result

    def delete(self):
        sql = f"DELETE FROM notes WHERE user_id = {self.user_id} AND title LIKE '%{self.title}%' "
        
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]

