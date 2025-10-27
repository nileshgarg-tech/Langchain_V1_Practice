from agent import build_agent
from tools import Context

def main():
    agent = build_agent()

    config = {"configurable": {"thread_id": "1"}}

    response = agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
        config=config,
        context=Context(user_id="1")
    )
    print(response["structured_response"])

    # Continue the same conversation
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "thank you!"}]},
        config=config,
        context=Context(user_id="1")
    )
    print(response["structured_response"])

if __name__ == "__main__":
    main()
 