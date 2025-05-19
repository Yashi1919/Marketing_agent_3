import os
from crewai import Agent, Task, Crew
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash-preview-04-17',
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv('GOOGLE_API_KEY')
)

# Agent 1: Medical Diagnostics Researcher

# Note: The llm and tool are assumed to be defined in the main script (as in your provided code)
# llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-04-17', ...)
# tool = <your tool from tools module>

# Agent 1: Diagnostic Technology Analyst
diagnostic_technology_analyst = Agent(
    role="Diagnostic Technology Analyst",
    goal="Identify and analyze machines and tests used to detect blood-related complications in pregnant women across trimesters",
    verbose=True,
    memory=True,
    backstory=(
        "As a biomedical engineering expert, you specialize in diagnostic technologies, with a keen ability to uncover the machines powering prenatal blood tests and their applications in maternal healthcare. Your passion for innovation drives you to map diagnostic tools to clinical needs, ensuring accurate detection of pregnancy complications."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Agent 2: Manufacturer Competition Analyst
manufacturer_competition_analyst = Agent(
    role="Manufacturer Competition Analyst",
    goal="Identify manufacturers of prenatal blood tests and machines, highlighting competitive markets with more than four players",
    verbose=True,
    memory=True,
    backstory=(
        "With a deep understanding of the medical device industry, you excel at analyzing market competition, tracking global and regional manufacturers, and identifying trends in innovation and market share. Your insights help stakeholders navigate the crowded landscape of diagnostic test production."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Agent 3: Supply Chain Analyst
supply_chain_analyst = Agent(
    role="Supply Chain Analyst",
    goal="Map distributors and suppliers of prenatal blood tests in India, analyzing their networks and market reach",
    verbose=True,
    memory=True,
    backstory=(
        "As a supply chain expert in India’s healthcare sector, you are adept at tracing the flow of diagnostic tests from manufacturers to end-users, with a focus on ensuring accessibility across urban and rural regions. Your analytical skills uncover critical partnerships and distribution dynamics."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Agent 4: Medical Diagnostics Researcher
medical_diagnostics_researcher = Agent(
    role="Medical Diagnostics Researcher",
    goal="Detail blood-related tests for pregnant women, including their scientific principles and trimester-specific applications",
    verbose=True,
    memory=True,
    backstory=(
        "As a dedicated prenatal diagnostics specialist, your expertise lies in identifying and explaining blood tests critical for maternal and fetal health. Your commitment to scientific rigor ensures comprehensive insights into test principles and their role in managing pregnancy complications."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Agent 5: Market Pricing Analyst
market_pricing_analyst = Agent(
    role="Market Pricing Analyst",
    goal="Identify brands, companies, and pricing for prenatal blood tests and technologies in India",
    verbose=True,
    memory=True,
    backstory=(
        "With a sharp focus on healthcare economics, you analyze pricing structures and brand dynamics in India’s diagnostic market. Your ability to uncover cost variations and affordability factors empowers stakeholders to make informed decisions in maternal healthcare."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)