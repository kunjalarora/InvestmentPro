
from langchain_openai import OpenAI
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_ticker_name(investment_type, currency_type):
    llm = OpenAI(temperature=0.7)

    prompt_template_ticker = PromptTemplate(
        input_variables=["investment_type", "currency_type"],
        template="I want invest {investment_type} in {currency_type} on wealthSimple. Suggest me five profit making tickers and their official names only."
    )
    
    ticker_name = LLMChain(llm=llm, prompt=prompt_template_ticker, output_key="ticker_name")
    response = ticker_name({'investment_type':investment_type, 'currency_type':currency_type})
    return response

if __name__ == "__main__":
    print(generate_ticker_name("long term", "CAD Dollar"))
