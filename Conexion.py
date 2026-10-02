from pymongo import MongoClient

uri = "mongodb+srv://hector1985:Aime131985@karla.t5uvbw4.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

# Seleccionar (o crear) la base de datos 'ventas_db'
db = client["KARLA_FLORES"]

# Seleccionar (o crear) la colección 'ventas'
coleccion = db["Trabajos"]

# Al insertar un documento, MongoDB crea automáticamente la BD y la colección
coleccion.insert_one({"producto": "Laptop", "precio": 1200})
print("¡Base de datos y colección creadas exitosamente!")
