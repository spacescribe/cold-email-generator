from langchain_community.document_loaders import WebBaseLoader

# loader = WebBaseLoader("https://careers.nike.com/lead-data-engineer-itc/job/R-61666?source=BY_Google_SEM&utm_source=BY_Google_SEM&utm_medium=employer_ad&utm_campaign=TACOE%20APLA_India%20&utm_content=NikeInc")

class Loader:
    def __init__(self, link):
        self.loader=WebBaseLoader(link)

    def get_loaded_data(self):
        return self.loader.load().pop().page_content