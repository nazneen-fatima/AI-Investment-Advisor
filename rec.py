from config import llm
def recommend_assets(state):
    allocation = state["allocation"]

    prompt = f"""
Role:
You are an investment research assistant specializing in low-cost, diversified ETFs.
Your job is to map a user's target asset allocation to suitable ETF options.
Prioritize broad diversification, low expense ratios, liquidity, and simplicity.

Context:
The user has already been given the following target asset allocation:
{allocation}

The allocation may contain categories such as stocks, bonds, and cash.
Recommend ETFs that closely match each category rather than changing the
target allocation.

Task:
For each asset category in the allocation:
1. Recommend one or two suitable low-cost ETFs.
2. Include the ETF ticker and fund name.
3. Briefly explain what the ETF provides.
4. Mention the approximate expense ratio when known.
5. Keep the recommendations diversified and suitable for long-term investing.
6. Do not recommend individual stocks.

Output:
Return the results in a simple table with these columns:
- Asset Category
- Target Allocation
- ETF
- Fund Name
- Expense Ratio
- Reason

Keep the response concise and educational. Do not present the ETF choices
as guaranteed or as personalized financial advice.
"""

    result = llm.invoke(prompt)
    state["recommendations"] = result
    return state