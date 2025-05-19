from crewai import Task
from tools import tool
from agents import (
    manufacturer_competition_analyst,
    medical_diagnostics_researcher,
    supply_chain_analyst,
    diagnostic_technology_analyst,
    market_pricing_analyst
)

# researcher task



# Task for Agent 1: Diagnostic Technology Analyst
diagnostic_technology_task = Task(
    description=(
        "Identify and describe the machines or diagnostic tests used to detect blood-related complications (e.g., anemia, gestational diabetes, Rh incompatibility) for {topic}. "
        "Investigate the equipment, methodologies, and their clinical applications in maternal healthcare. Provide a detailed narrative explaining the functionality of these machines and their role in prenatal care. "
        "Include a table summarizing the tests and machines. To guide the analysis, answer the following sub-questions:\n"
        "1. What specific blood tests are routinely performed to identify complications like anemia, infections, or gestational diabetes in pregnant women, and what are their primary diagnostic purposes?\n"
        "2. Which machines or technologies are used to conduct these blood tests, and how do they function to detect the targeted conditions?\n"
        "3. Are there specialized machines for detecting pregnancy-specific complications, such as Rh incompatibility or preeclampsia, and how are they applied in clinical settings?\n"
        "4. How do these machines or tests align with the trimesters of pregnancy, and are there variations in their use based on the stage of pregnancy or specific complications?"
    ),
    expected_output=(
        "A 2000-word LaTeX report (.tex file) with:\n"
        "- A table listing blood tests and corresponding machines, including machine types (e.g., hematology analyzer, immunoassay system) and their diagnostic purposes.\n"
        "- Narrative sections explaining the functionality of each machine, its role in detecting complications, and trimester-specific applications.\n"
    ),
    tools=[tool],
    agent=diagnostic_technology_analyst,
    async_execution=False,
    output_file='diagnostic_technology_report.tex'
)

# Task for Agent 2: Manufacturer Competition Analyst
manufacturer_competition_task = Task(
    description=(
        "Identify current manufacturers of blood-related diagnostic tests and machines used for {topic}, focusing on global and India-specific players. "
        "Highlight markets where more than four manufacturers compete, analyzing competitive dynamics, including pricing, innovation, and market share. "
        "Provide a detailed narrative on the technological landscape and competitive environment. "
        "Include a table summarizing tests, machines, and manufacturers. To guide the analysis, answer the following sub-questions:\n"
        "1. Who are the leading global and regional manufacturers producing machines or reagents for blood-related pregnancy tests, such as hematology or immunoassay analyzers?\n"
        "2. For each test or machine, how many manufacturers are actively competing in the global market, and are there markets with more than four players?\n"
        "3. What are the key innovations or product differentiations offered by these manufacturers, and how do they influence market competitiveness?\n"
        "4. Are there specific manufacturers with a strong presence in India for these tests, and how does their market share reflect the competitive environment?"
    ),
    expected_output=(
        "A 2000-word LaTeX report (.tex file) with:\n"
        "- A table listing tests/machines, their manufacturers, and markets with >4 players, including key product names.\n"
        "- Narrative sections on manufacturer profiles, competitive dynamics (pricing, innovation, market share), and India-specific market presence.\n"
    ),
    tools=[tool],
    agent=manufacturer_competition_analyst,
    async_execution=False,
    output_file='manufacturer_competition_report.tex'
)

# Task for Agent 3: Supply Chain Analyst
supply_chain_task = Task(
    description=(
        "Analyze the Indian market for blood-related diagnostic tests related to {topic}, focusing on key distributors, suppliers, and their roles in ensuring test availability. "
        "Highlight market opportunities (e.g., rising demand due to maternal health programs) and risks (e.g., import duties, rural access). "
        "Provide a detailed narrative on the market landscape, key players, and trends shaping India’s diagnostics sector. "
        "Include a table summarizing distributors and suppliers. To guide the analysis, answer the following sub-questions:\n"
        "1. Which major diagnostic companies or laboratories in India distribute blood test kits and machines for pregnancy-related complications?\n"
        "2. Are there specialized distributors for medical equipment like hematology or immunoassay analyzers in India, and who are their primary suppliers?\n"
        "3. How do regional and local suppliers contribute to the availability of these tests in urban versus rural India, and what are their distribution networks?\n"
        "4. What partnerships or collaborations exist between global manufacturers and Indian distributors to ensure supply chain efficiency for these tests?"
    ),
    expected_output=(
        "A 2000-word LaTeX report (.tex file) with:\n"
        "- A table listing distributors, suppliers, and their associated tests/machines in India.\n"
        "- Narrative sections on distribution networks, urban vs. rural access, market opportunities, risks, and partnerships with global manufacturers.\n"
    ),
    tools=[tool],
    agent=supply_chain_analyst,
    async_execution=False,
    output_file='supply_chain_report.tex'
)

# Task for Agent 4: Medical Diagnostics Researcher
diagnostics_research_task = Task(
    description=(
        "Compile a comprehensive list of blood-related diagnostic tests performed on pregnant women to monitor complications for {topic}, detailing their type, scientific principle, and trimester of use. "
        "Emphasize tests for conditions like anemia, gestational diabetes, and Rh incompatibility. Provide a detailed narrative explaining the role of these tests in maternal healthcare, their scientific basis, and clinical significance. "
        "Include a table summarizing the tests, principles, trimesters, and conditions detected. To guide the analysis, answer the following sub-questions:\n"
        "1. What are the primary blood tests recommended for pregnant women to monitor complications, and what specific conditions do they target?\n"
        "2. What scientific principles underpin each blood test, and how do they enable detection of pregnancy-related complications?\n"
        "3. In which trimester is each test typically performed, and are there variations based on risk factors or complications?\n"
        "4. Are there additional or follow-up tests triggered by initial results, and how do they contribute to managing complications?"
    ),
    expected_output=(
        "A 2000-word LaTeX report (.tex file) with:\n"
        "- A table listing diagnostic tests, their scientific principles, trimesters, and conditions detected.\n"
        "- Narrative sections explaining the scientific basis, clinical context, and significance of these tests in maternal healthcare.\n"
    ),
    tools=[tool],
    agent=medical_diagnostics_researcher,
    async_execution=False,
    output_file='diagnostics_research_report.tex'
)

# Task for Agent 5: Market Pricing Analyst
market_pricing_task = Task(
    description=(
        "Identify all brands and companies manufacturing or providing blood-related diagnostic tests and related technologies for {topic} in India, including their prices in INR. "
        "Analyze factors affecting pricing and affordability, such as brand reputation and government schemes. Provide a detailed narrative on pricing trends and their impact on maternal healthcare access. "
        "Include a table summarizing brands, tests, and prices. To guide the analysis, answer the following sub-questions:\n"
        "1. Which global and Indian brands manufacture blood test kits and machines for pregnancy-related complications, and what are their flagship products?\n"
        "2. What are the approximate costs of these tests or machines in India, and how do prices vary between hospital labs and home testing kits?\n"
        "3. Are there cost differences based on brand reputation, technology (e.g., automated vs. manual), or distribution channels in India?\n"
        "4. How do government schemes or insurance impact the affordability of these tests for pregnant women in India?"
    ),
    expected_output=(
        "A 2000-word LaTeX report (.tex file) with:\n"
        "- A table listing brands, companies, test/technology names, and their prices in INR.\n"
        "- Narrative sections on pricing factors, brand comparisons, and the role of government schemes in affordability.\n"
    ),
    tools=[tool],
    agent=market_pricing_analyst,
    async_execution=False,
    output_file='market_pricing_report.tex'
)