from config import llm

def suggest_allocation(state):
    profile = state["profile"]
    prompt = f"""
    Role:
    You are a financial planning assistant with expertise in long-term investing and portfolio construction.
    Your job is to provide simple, educational asset-allocation guidance based on a user's profile.
    You should consider the relationship between investment horizon, financial goals, and risk tolerance.
    Do not present the recommendation as guaranteed or as a substitute for advice from a qualified financial professional.
   
    Context:
    The user wants a general asset-allocation recommendation across stocks, bonds, and cash.
    The allocation should reflect their age, investment goal, time horizon, and risk tolerance.
    The percentages must add up to exactly 100%.
   
    User Profile:
    - Age: {profile['age']}
    - Goal: {profile['goal']}
    - Investment Horizon: {profile['horizon']} years
    - Risk Tolerance: {profile['risk']}
   
    Task:
    Suggest an asset allocation in percentages across:
    - Stocks
    - Bonds
    - Cash
   
    Explain briefly why the suggested allocation is appropriate for the user's profile.
   
    Output:
    Return the allocation in a simple table, followed by a brief explanation.
    """
    suggestion = llm.invoke(prompt)
    state["allocation"] = suggestion
    return state