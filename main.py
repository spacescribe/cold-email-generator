import streamlit as st
from llm_helper import LLM
from portfolio import Portfolio
from web_loader import Loader
from email_generator import EmailGenerator
from utils import clean_text

def start_streamlit_app(llm, portfolio):
    st.title("Cold email generator")
    url_input = st.text_input("Enter a URL: ", value="https://jobs.nike.com/job/R-33460")
    submit_btn=st.button("Generate")

    if submit_btn:
        try:
            loader= Loader(url_input)
            job_desc=clean_text(loader.get_loaded_data())
            print(f"[DEBUG] start_streamlit_app: {job_desc}")
            email_gen=EmailGenerator(llm, portfolio, job_desc)
            email=email_gen.generate_email()
            st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__=="__main__":
    llm = LLM()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    start_streamlit_app(llm, portfolio)
