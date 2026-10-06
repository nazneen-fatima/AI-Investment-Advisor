

def collect_profile(state):
    state["profile"]={ "age": state["age"],
                       "goal": state["goal"],
                       "horizon": state["horizon"],
                       "risk": state["risk"]}
    return state
