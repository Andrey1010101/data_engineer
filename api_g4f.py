from g4f.client import Client
from g4f.gui import run_gui

client = Client()

def chat(client):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": "я планирую сделать это один"
            }
        ],
        web_search = False
    )

    print(response.choices[0].message.content)

def immage(client):

    response = client.images.generate(
        model="flux",
        prompt="beer",
        response_format="url"
    )

    print(f"Generated image URL: {response.data[0].url}")

def gui_gpt():
    # * Running on http://127.0.0.1:8080
    #* Running on http://192.168.1.66:8080

    #Run via CLI (To start the Flask Server):
    #python -m g4f.cli gui --port 8080 --debug
    #Or, start the FastAPI Server:
    #python -m g4f --port 8080 --debug
    run_gui()

#immage(client)
#chat(client)
gui_gpt()