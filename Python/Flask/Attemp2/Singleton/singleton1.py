class DBSingleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print('Creating the object')
            cls.__instance = super(DBSingleton, cls).__new__(cls)
        return cls.__instance

db1 = DBSingleton()
db2 = DBSingleton()
print(db1,db2)
print(db1==db2)