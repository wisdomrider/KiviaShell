import sqlite3, os

PRIMARY = " PRIMARY KEY "
TEXT = " TEXT "
INTEGER = " INTEGER "
REAL = " REAL "
INTEGER_NOT_NULL = " INTEGER NOT NULL "
INTEGER_NOT_NULL_AUTOINCREMENT = " INTEGER NOT NULL AUTOINCREMENT "
INTEGER_UNIQUE = " INTEGER UNIQUE "
TEXT_UNIQUE = " TEXT UNIQUE "
TEXT_NOT_NULL = " TEXT NOT NULL "
TEXT_PRIMARY = " TEXT PRIMARY "
INTEGER_PRIMARY = " INTEGER PRIMARY "
INTEGER_PRIMARY_AUTOINCREMENT = " INTEGER PRIMARY AUTOINCREMENT "


class DB:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(dir_path.replace("/codes", "") + "/db/kivia.db")

    def createTable(self, tablename, fields):
        fieldtype = ""
        for x in fields:
            fieldtype += x + " " + fields[x] + ","
        fieldtype = fieldtype[:-1]
        self.conn.execute("CREATE  TABLE if not exists  " + tablename + " (" + fieldtype + ")")
        self.conn.commit()

    def insert(self, tablename, data):
        fieldnames = ""
        values = ""
        fields = [x[1] for x in tuple(self.conn.execute("PRAGMA table_info(" + tablename + ")").fetchall())]
        for x in fields:
            fieldnames += x + ","
        fieldnames = fieldnames[:-1]
        if type(data) is tuple:
            for y in data:
                y = "'" + y + "'" if type(y) is str else y
                values += str(y) + ","
            values = values[:-1]
        else:
            values = "'" + data + "'" if type(data) is str else data
        self.conn.execute("INSERT INTO " + tablename + " (" + fieldnames + ") VALUES (" + values + ");")
        self.conn.commit()

    def update(self, tablename, data, **params):
        fieldnames = ""
        fields = [x[1] for x in self.conn.execute("PRAGMA table_info(" + tablename + ")").fetchall()]
        for x, y in zip(fields, data):
            y = "'" + y + "'" if type(y) is str else y
            fieldnames += str(x) + " = " + str(y) + ","
        fieldnames = fieldnames[:-1]
        where = params["where"]
        if 'where' in params:
            where1 = ""
            for x in where:
                where[x] = "'" + where[x] + "'" if type(where[x]) is str else where[x]
                where1 += str(x) + " = " + str(where[x])
            where = where1
        else:
            where = fieldnames.split(",")[0]
        self.conn.execute("UPDATE " + tablename + " SET " + fieldnames + " WHERE " + where)
        self.conn.commit()

    def updateIntent(self, parse, msg, type):
        has = self.get('parser', {'parse': parse})
        if has:
            self.update('parser', (parse, msg, type), where={'parse': parse})
        else:
            self.insert('parser', (parse, msg, type))

    def deleteAll(self, tablename):
        self.conn.execute("delete from " + tablename)
        self.conn.commit()

    def getAll(self, tablename):
        return self.conn.execute("select * from " + tablename).fetchall()

    def get(self, tablename, where, **params):
        orand = " " + params['what'] + " " if 'what' in params else " OR "
        where1 = ""
        for x in where:
            where[x] = "'" + where[x] + "'" if type(where[x]) is str else where[x]
            where1 += str(x) + " = " + str(where[x]) + orand
        where1 = where1[:-3] if orand is " OR " else where1[:-4]
        return self.conn.execute("SELECT * FROM " + tablename + " WHERE " + where1).fetchall()

    def delete(self, tablename, where, **params):
        orand = " " + params['what'] + " " if 'what' in params else " OR "
        where1 = ""
        for x in where:
            where[x] = "'" + where[x] + "'" if type(where[x]) is str else where[x]
            where1 += str(x) + " = " + str(where[x]) + orand
        where1 = where1[:-3] if orand is " OR " else where1[:-4]
        self.conn.execute("DELETE FROM " + tablename + " WHERE " + where1).fetchall()
        self.conn.commit()

# db = DB()
# db.deleteAll('kivia')
# db.delete('kivia', {'kola': 1, 'hola': 'okay1'}, what="AND")
# db.createTable('kivia', {'hola': 'text primary key', 'kola': 'integer'})
# db.insert('kivia', ('okay', 1))
# db.update('kivia', ('okay1', 1), where={'kola': 1})
# print(db.get('kivia', {'kola': 1, 'hola': 'okay1'}, what="AND"))
# db.getAll('kivia')
