

from langchain import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.tools import tool



str_parser = StrOutputParser()

template_cook = PromptTemplate.from_template(
    '''
    Câu hỏi:
    {question}
    Bạn hãy trả lời theo bố cục sau:
    - chi tiết nguyên liệu
    - chi tiết cách làm
    - 
    - Kết luận, và gợi ý cách làm


    '''
)

llm = OllamaLLM(
    model = "qwen3-coder:480b-cloud"

)
# AI sẽ đọc hiểu nội dung template muốn làm cái gì -> llm để phân tích xử lý
llm_chain = template_cook | llm | str_parser
llm_chain_cook = template_cook
def chat_stream(question:str):
    for work in llm_chain.stream({
        'question':question
        
        }):
        print(work, end="")

chat_stream()