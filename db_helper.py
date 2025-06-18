import uuid
import chromadb
import pandas as pd

client=chromadb.PersistentClient('vectorstore')
collection = client.get_or_create_collection(name='portfolio')
df=pd.read_csv("portfolio.csv")
print(df)

if not collection.count():
    for _, row in df.iterrows():
        collection.add(
            documents=[row['TechStack']],
            metadatas={"links": row['Links']},
            ids=[str(uuid.uuid4())]
        )

if collection.count():
    data = collection.get()
    
    for doc, meta in zip(data['documents'], data['metadatas']):
        print("Document:", doc)
        print("Metadata:", meta)
        print("-" * 40)