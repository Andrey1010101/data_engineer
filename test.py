from g4f.client import Client
from g4f.Provider import OpenaiChat

client = Client(
    image_provider=OpenaiChat
)

response = client.images.create_variation(
    image=open("C:/Users/Dexter/Downloads/121.jpg", "rb"),
    model="dall-e-3",
    #parameters="сделай в стиле аниме"
    # Add any other necessary parameters
)

image_url = response.data[0].url

print(f"Generated image URL: {image_url}")