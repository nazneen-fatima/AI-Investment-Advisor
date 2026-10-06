from fastapi import FastAPI
from pydantic import BaseModel

from collector import collect_profile
from suggest import suggest_allocation
from rec import recommend_assets
from langgraph.graph import StateGraph , END

app = FastAPI()

graph=StateGraph(dict)
graph.add_node("profile",collect_profile)
graph.add_node("allocate",suggest_allocation)
graph.add_node("recommend",recommend_assets)

graph.set_entry_point("profile")
graph.add_edge("profile","allocate")
graph.add_edge("allocate", "recommend")
graph.set_finish_point("recommend")

graph_app = graph.compile()


# fastapi request

class InvestmentRequest(BaseModel):
    age: int
    goal: str
    horizon: int
    risk: str

# api endpoint 

@app.post("/invest")
def invest(request: InvestmentRequest):

    result = graph_app.invoke(request.model_dump())

    return {
        "profile": result["profile"],
        "allocation": result["allocation"].content,
        "recommendations": result["recommendations"].content
    }