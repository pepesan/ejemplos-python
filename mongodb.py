from pymongo import MongoClient, ASCENDING, DESCENDING
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/test')
# acceso a bbdd
db = client.test
#acceso a colección
libros = db.libros

import datetime
objetoLibro = {"author": "Terry Pratchett",
        "title": "El color de la magia",
        "tags": ["magos", "medieval", "cachondeo"],
        "date": datetime.datetime.utcnow()}
libro_id = libros.insert_one(objetoLibro).inserted_id
print("Libro id: "+str(libro_id))
# listado de colecciones
print(db.list_collection_names())

import pprint
# encuentra el primer libro
pprint.pprint(libros.find_one())

#encuentra un libro concreto por campo
pprint.pprint(libros.find_one({"author": "Terry Pratchett"}))
#encuentra un libro concreto por id
pprint.pprint(libros.find_one({"_id": libro_id}))

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
pprint.pprint(get(libro_id))

varios_libros = [{"author": "Neil Gayman",
                  "title": "Stardust",
                  "tags": ["fantasía", "amor"],
                  "date": datetime.datetime(2009, 11, 12, 11, 14)},
                 {"author": "J.R.R Tolkien",
                  "title": "El señor de los anillos: la comunidad del anillo",
                  "text": "and pretty easy too!",
                  "date": datetime.datetime(2009, 11, 10, 10, 45)},
                 {"author": "J.R.R Tolkien",
                  "title": "El señor de los anillos: las dos torres",
                  "text": "caballitos y cargas!",
                  "date": datetime.datetime(2009, 11, 10, 10, 45)},
                {"author": "J.R.R Tolkien",
                  "title": "El señor de los anillos: el retorno del rey",
                  "text": "spoiler, frodo no muerte en mordor!",
                  "date": datetime.datetime(2009, 11, 10, 10, 45)}
                 ]
result = libros.insert_many(varios_libros)
pprint.pprint(result)

for libro in libros.find():
    pprint.pprint(libro)

print(libros.count_documents({}))
print(libros.count_documents({'author':'Terry Pratchett'}))


d = datetime.datetime(2009, 11, 12, 12)
for libro in libros.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(libro)


condiciones = {"author": "J.R.R Tolkien"}
valores = { "$set": { "text": "¡¡¡Y con mi Hacha!!"} }

libros.update_one(condiciones, valores)

pprint.pprint(libros.find_one({"author":  "J.R.R Tolkien"}))

valores = { "$set": { "text": "¡¡¡Y con mi Hacha!!","title": "El Señor de los Anillos: La Comunidad del Anillo"} }

libros.update_one(condiciones, valores)

pprint.pprint(libros.find_one({"author":  "J.R.R Tolkien"}))

result = libros.find({"author":  "J.R.R Tolkien"}).limit(2)
print("Los dos primeros libros de Tolkien")
for item in result:
    pprint.pprint(item)

libros.delete_many({"author":  "J.R.R Tolkien"})

pprint.pprint("Libros de Tolkien: "+str(libros.find_one({"author":  "J.R.R Tolkien"})))


result = db.profiles.create_index([('user_id', ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

libros.drop()
print("Colecciones: "+str(db.list_collection_names()))

