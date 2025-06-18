# cold-email-generator

A GenAI-powered tool that generates personalized cold emails for job applications by scraping career pages, extracting job details, and crafting tailored emails based on your portfolio.

---

## 🚀 Features

- 🔍 **Job Extraction**: Automatically scrapes and extracts job listings (role, skills, description, etc.) from raw text or URLs.
- ✍️ **AI-Powered Email Writing**: Uses LLM (LLaMA3 via Groq) to generate personalized cold emails with a professional tone.
- 💼 **Smart Portfolio Matching**: Matches your portfolio projects to required skills using vector search with ChromaDB.
- ⚙️ **Modular Design**: Clean and extensible class-based Python structure.
- 🖥️ **Streamlit UI**: Easy-to-use web interface to generate emails by just entering a URL or job text.

---

## 🧠 Tech Stack

- [LangChain](https://www.langchain.com/)
- [Groq + LLaMA3](https://groq.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Streamlit](https://streamlit.io/)
- `pandas`, `uuid`, `dotenv`

---

## 📄 Sample Portfolio CSV

| TechStack                         | Links                        |
|----------------------------------|------------------------------|
| Python, FastAPI, LLM Integration | https://github.com/yourrepo1 |
| JavaScript, React, Tailwind      | https://github.com/yourrepo2 |

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/spacescribe/cold-email-generator.git
cd cold-email-generator

```

2. **Install dependencies**
```
pip install -r requirements.txt
```

3. **Set your API Key**

Create .env file and add the API key:
```
GROQ_API_KEY=your_groq_api_key
```

4. **Add your portfolio**

Edit `portfolio.csv`to include your projects, tech stack, and links.

5. **Run the Streamlit app**
```
streamlit run main.py
```

