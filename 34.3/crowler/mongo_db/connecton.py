from pymongo import MongoClient

URI = "mongodb://localhost:27017/"
client = MongoClient(URI) # client = MongoClient("mongodb://localhost:27017/")
db = client.catalogue # o banco de dados catalogue será criado se não existir

# Code
book = {
  "title": "Vinicius",
  "price": 10000
}

books = [
    {
        "title": "Outro",
        "price": 1,
    },
    {
        "title": "Outro2",
        "price": 2,
    },
]

# Inserindo um unico documento na tabela book
document_id = db.books.insert_one(book).inserted_id
print(document_id)

opetation = db.books.insert_many(books)
print(opetation)

# Busca um documento da coleção, sem filtros
print(db.books.find_one())

# busca utilizando filtros
for book in db.books.find({"title": {"$regex": "t"}}):
    print(book["title"])
#

client.close() # fecha a conexão com o banco de dados