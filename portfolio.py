import uuid
import chromadb
import pandas as pd

class Portfolio:
    def __init__(self, file_path='portfolio.csv', output_path='vectorstore'):
        self.file_path=file_path
        self.data=pd.read_csv(self.file_path)
        self.chroma_client=chromadb.PersistentClient(output_path)
        self.collection=self.chroma_client.get_or_create_collection(name='portfolio')
    
    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                documents=[row['TechStack']],
                metadatas={"links": row['Links']},
                ids=[str(uuid.uuid4())]
            )
                
    def get_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])