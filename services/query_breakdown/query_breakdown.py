from utils.file import FileHandler
from utils.output import OutputHadler
from core import Prompts
from core import LLMInitializer
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

try:
    llm_initializer = LLMInitializer() #instantiate the class
    llm = llm_initializer.set_llm()  # Call the set_llm method
    #print("LLM initialized successfully!")
except Exception as e:
        print(f"Couldn't initialize LLM: {e}")

class QueryProcessor:
    def __init__(self, query: str):
        self.file_handler = FileHandler()
        self.output_handler = OutputHadler()
        self.model = llm
        self.output_dir = "data/query/query.json"
        self.query = query
    
    def break_query(self):
        print("🧠 Understanding your Query")
        system_prompt = Prompts.query_breakdown
        human_prompt = "{query}"

        prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

        chain = prompt | self.model

        response = chain.invoke({
            "query": self.query,
        })

        breakdown = self.output_handler.clean_llm_output(response.content)
        self.file_handler.save_json(breakdown, self.output_dir)

        classified_intent = self.file_handler.load_json(self.output_dir)
        self.intent = classified_intent["intent"]


    def verify_intent(self):
        user_input = input(f"Is this the correct intent?: {self.intent} \nPress Y for yes or N for no: ")
        if user_input.lower() == "y":
            print("Intent classified successfully!")
        elif user_input.lower() == "n":
            print("🧠 Deeply analyzing your query")
            self.query = f"{self.query} The intent cannot be {self.intent}"
        else:
            print("Invalid input. Please enter Y or N.")

        return self.intent