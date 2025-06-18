from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from llm_helper import llm
from web_loader import loader
from db_helper import collection

page_data = loader.load().pop().page_content
parser = JsonOutputParser()

prompt = PromptTemplate.from_template(
    """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skills` and `description`. Just give a single json object and not an unnecessary list of json.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
    """
)

chain = prompt | llm
res=chain.invoke(input={'page_data': page_data})
job = parser.parse(res.content)
print(job)


