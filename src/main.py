from planner import plan
from executor import execute
from memory import Memory

def main():
    memory = Memory()
    company = input("Enter company name: ")
    tasks = plan(company)
    result = execute(tasks, company, memory)
    memory.save(company, result)
    print("\n--- ESG RISK REPORT ---\n")
    print(result["analysis"])

if __name__ == "__main__":
    main()
