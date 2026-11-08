

# Import Ollama integration for LangChain
from langchain_ollama import ChatOllama

# Import prompt template
from langchain_core.prompts import PromptTemplate

# Configure Llama 3.2 model parameters
parameters = {
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 1.0,
    "num_predict": 512,
}

# Set the model name
model_id = "llama3.2"

# Initialize Llama 3.2 using Ollama
llama_llm = ChatOllama(
    model=model_id,
    temperature=parameters["temperature"],
    top_k=parameters["top_k"],
    top_p=parameters["top_p"],
    num_predict=parameters["num_predict"],
)

# Define a prompt
prompt = PromptTemplate.from_template(
    "How to read a book effectively?"
)

# Create a LangChain chain
chain = prompt | llama_llm

# Invoke the model
response = chain.invoke({})

# Display the response text
print(response.content)
