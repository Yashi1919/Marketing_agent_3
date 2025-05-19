from crewai import Crew, Process
from tasks import (
    diagnostic_technology_task,
    manufacturer_competition_task,
    supply_chain_task,
    diagnostics_research_task,
    market_pricing_task
)
from agents import (
    diagnostic_technology_analyst,
    manufacturer_competition_analyst,
    supply_chain_analyst,
    medical_diagnostics_researcher,
    market_pricing_analyst
)

# Forming the diagnostics-focused crew with enhanced configuration
crew = Crew(
    agents=[
        diagnostic_technology_analyst,
        manufacturer_competition_analyst,
        supply_chain_analyst,
        medical_diagnostics_researcher,
        market_pricing_analyst
    ],
    tasks=[
        diagnostic_technology_task,
        manufacturer_competition_task,
        supply_chain_task,
        diagnostics_research_task,
        market_pricing_task
    ],
    process=Process.sequential
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': 'blood-related tests done on pregnant women due to complications at different trimesters'})
print(result)