from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

class EmailGenerator:
    def __init__(self, llm, portfolio, job_description):
        self.llm=llm.get_llm()
        self.portfolio=portfolio
        self.portfolio.load_portfolio()
        self.job_desc=job_description
        self.parser=JsonOutputParser()

    def extract_jobs(self, loaded_data):
        prompt_extract = PromptTemplate.from_template(
        """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the 
            following keys: `role`, `experience`, `skills` and `description`. Just give a single json object and not an unnecessary list of json.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):   
            Make sure:
            - The JSON is not inside a list or string.
            - There are no trailing commas or missing braces.
            - No extra explanations or text.
            Return ONLY the JSON object. Nothing else.
        """
        )

        chain_extract = prompt_extract | self.llm
        res=chain_extract.invoke(input={'page_data': loaded_data})
        print("[DEBUG] extract_jobs: LLM response content (before parse):", res.content)
        try:
            job=self.parser.parse(res.content)
        except OutputParserException as e:
            print("[ERROR] extract_jobs: Error in parsing json. LLM response(before parse):", res.content)
            print("[ERROR] extract_jobs: Error in parsing json. Error:", e)
            raise OutputParserException("Error parsing: ", e)
        print(f"[DEBUG] extract_jobs: Parsed job is: {job}")
        return job if isinstance(job, list) else [job]
    
    def get_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Aurora, a passionate and skilled job seeker with hands-on experience in software development, AI integration, and building scalable solutions. 
            You’re writing a cold email to the hiring manager to express your interest in the role mentioned above.

            Briefly highlight how your background aligns with the job requirements, mention your relevant skills, and express enthusiasm for contributing to their team. 
            Also, include links to the most relevant projects from your portfolio to demonstrate your experience: {link_list}

            Keep the tone professional, concise, and personalized. Avoid generic buzzwords. Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
        """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        print(f"[DEBUG] get_email: Generated email: {res.content}")
        return res.content
    
    def generate_email(self):
        # job = self.extract_jobs(self.job_desc)
        job = self.extract_jobs(self.job_desc)[0]
        skills = job.get('skills', [])
        links=self.portfolio.get_links(skills)
        email = self.get_email(self.job_desc, links)
        print(f"[DEBUG] generate_email: Generated email: {email}")
        return email
