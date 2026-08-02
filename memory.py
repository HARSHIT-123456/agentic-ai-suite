from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
from agno.tools.duckduckgo import DuckDuckGoTools
# Load environment variables
load_dotenv()


db = SqliteDb(db_file="agno.db")
db.create()
db.clear_memories()
def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3-32b"),
        
        markdown=True,
        add_history_to_context=True,
        enable_user_memories=True
        
        
    )


agent = build_agent()

user_id="rahul@gmail.com"
agent.print_response("What is the best time to visit it?",user_id=user_id)
agent.print_response(
    "What is the capital of Australia?",user_id=user_id
)





memories = agent.get_user_memories(user_id=user_id)
print("MEMORIES: ")
pprint(memories)