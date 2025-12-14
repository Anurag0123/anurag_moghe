## 2. `ARCHITECTURE.md`

```markdown
# Architecture Overview

The agent follows a sequential architecture for ESG risk assessment:

```
User Input (Company Name)
    |
    v
Planner (Uses Gemini to break down tasks)
    |
    v
Executor (For each task: Analyze datasets + Call Gemini)
    |   (Stores intermediate results in Memory)
    v
Memory (Persistent storage of task results and final report)
    |
    v
Final Risk Report (Compiled analysis and recommendations)
```

## Components

1. **User Interface**  
   - CLI input for company name  

2. **Agent Core**  
   - **Planner**: Uses Gemini AI to dynamically generate a list of tasks based on user goal  
   - **Executor**: Iterates through tasks, loads relevant datasets (emissions.csv, incidents.csv), and uses Gemini for analysis  
   - **Memory**: In-memory dictionary for storing task results and final reports  

3. **Tools / APIs**  
   - Google Gemini API for planning and analysis  
   - Pandas for data manipulation  

4. **Observability**  
   - Print statements for task progress  
   - Error handling in Gemini calls  

