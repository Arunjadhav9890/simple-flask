import os
from dotenv import load_dotenv
from openai import OpenAI
# import response
load_dotenv()

client = OpenAI()
def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()
    
    

# api call to openai 

def summarize_tasks(tasks):
    prompt = f""" my mummy
            you sare a small list of task, catageoris 
            
            task:
            {tasks}
    """
    
    client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt}
            
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("\n task summary")
    print("-"*30)
    print(summary)
    