from langchain_ollama.llms import OllamaLLM
from langchain_core.tools import tool
import os
from langchain.agents.output_parsers import ReActSingleInputOutputParser

@tool
def read_file(file_path: str) -> str:
    """Read a file when the AI calls this function in the MCP."""
    try:
        with open(file_path.replace("file_path=", ""), 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as error:
        return f"Error: {str(error)}"
    
@tool
def list_files(directory: str = "./") -> str:
    """List all files and folders in the specified directory."""
    try:
        files = os.listdir(directory.replace("directory=", ""))
        return "\n".join(files)
    except Exception as error:
        return f"Error: {str(error)}"
    
@tool
def tong(a, b) -> str:
    """A sample tool that adds two numbers."""
    return str(int(a) + int(b))
    
tools = [
    read_file,
    list_files,
    tong
]

llm = OllamaLLM(model="qwen3-coder:480b-cloud")

# Define the agent
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate

prompt_instruction = PromptTemplate.from_template(
'''
You are an AI assistant using the ReAct framework.

Available tools:
{tools}

Tool names:
{tool_names}

Required procedure:
Thought: Reflect on the task and plan the next steps.
Action: Choose a tool (or Final).
Action Input: Provide the required input for the tool, without parameter names, only values.
Observation: Result from the tool.
... (repeat as necessary)
Final: Provide the final answer to the user.

Task: {input}
{agent_scratchpad}
'''
)

agent = create_react_agent(llm, tools, prompt_instruction, output_parser=ReActSingleInputOutputParser())
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({
    "input": '''
    Calculate the sum of 15 and 27 using the tong tool, dont use any other tool.
'''
})

print(result['output'])