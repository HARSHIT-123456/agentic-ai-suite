from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv


from agno.tools.duckduckgo import DuckDuckGoTools
# Load environment variables
load_dotenv()


def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )


agent = build_agent()

agent.print_response(
    "What is the difference between state and country"
)