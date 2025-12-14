import pandas as pd
from tools.gemini_client import call_gemini

def execute(tasks, company):
    emissions = pd.read_csv("data/emissions.csv")
    incidents = pd.read_csv("data/incidents.csv")

    e = emissions[emissions.company == company]
    i = incidents[incidents.company == company]

    prompt = f"""Analyze ESG risk for {company}.
CO2 avg: {e.co2_tons.mean()}
Incidents avg: {i.incidents.mean()}
Provide risk level and recommendations."""

    analysis = call_gemini(prompt)
    return {"analysis": analysis}
