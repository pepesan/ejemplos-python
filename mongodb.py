from pymongo import MongoClient, ASCENDING, DESCENDING
client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/test')
# acceso a bbdd
db = client.test
#acceso a colección
libros = db.libros
#libros=db.getCollection("libros")

import datetime
fecha = datetime.datetime(2011, 11, 4, 0, 5, 23, 283000, tzinfo=datetime.timezone.utc)
print(fecha.year)
objetoLibro = {"author": "Terry Pratchett",
        "title": "El color de la magia",
        "tags": ["magos", "medieval", "cachondeo"],
        "date": datetime.datetime.utcnow()}
libro_id = libros.insert_one(objetoLibro).inserted_id
print("Libro id: "+str(libro_id))
objetoLibro['_id']=libro_id
print("Libro: "+str(objetoLibro))
# listado de colecciones
print(db.list_collection_names())

# Pretty print, imprime mejor los listados, diccionarios y tuplas
from pprint import pprint
# encuentra el primer libro
# Diferencia entre pprint y print
print("Diferencia entre pprint y print")
pprint(libros.find_one())
print(libros.find_one())
#encuentra un libro concreto por campo
pprint(libros.find_one({"author": "Terry Pratchett"}))
#encuentra un libro concreto por id
pprint(libros.find_one({"_id": libro_id}))

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
pprint(get(libro_id))

varios_libros = [{"author": "Neil Gayman",
                  "title": "Stardust",
                  "tags": ["fantasía", "amor"],
                  "date": datetime.datetime(2009, 11, 12, 11, 14)},
                 {"author": "Terry Prachett & Neil Gayman",
                  "title": "Buenos Presagios",
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
print("Insert Many")
pprint(result.inserted_ids)
i=0
for libro in varios_libros:
    libro ['_id']= result.inserted_ids[0]
    i+=1

pprint(varios_libros)
for libro in libros.find():
    pprint(libro)

print(libros.count_documents({}))
print(libros.count_documents({'author':'Terry Pratchett'}))
print("RegExp")
print(libros.count_documents({'author':{'$regex':'Terry'}}))


d = datetime.datetime(2009, 11, 12, 12)
for libro in libros.find({"date": {"$lt": d}}).sort("author"):
    pprint(libro)

for libro in libros.find({"date": {"$lt": d}}).sort("author",ASCENDING):
    pprint(libro)

condiciones = {"author": "J.R.R Tolkien"}
valores = { "$set": { "text": "¡¡¡Y con mi Hacha!!"} }

libros.update_one(condiciones, valores)
print("Libro de Tolkien")
pprint(libros.find_one({"author":  "J.R.R Tolkien"}))

valores = { "$set": { "text": "¡¡¡Y con mi Hacha!!","title": "El Señor de los Anillos: La Comunidad del Anillo"} }

libros.update_one(condiciones, valores)

pprint(libros.find_one({"author":  "J.R.R Tolkien"}))

result = libros.find().skip(2).limit(3)
result = libros.find({"author":  "J.R.R Tolkien"}).limit(2)
print("Los dos primeros libros de Tolkien")
for item in result:
    pprint(item)

libros.delete_one({"_id":  libro_id})
libros.delete_many({"author":  "J.R.R Tolkien"})

pprint("Libros de Tolkien: "+str(libros.find_one({"author":  "J.R.R Tolkien"})))


result = db.libros.create_index([('author', ASCENDING)], unique=True)
print(sorted(list(db.libros.index_information())))

libros.drop()
print("Colecciones: "+str(db.list_collection_names()))

