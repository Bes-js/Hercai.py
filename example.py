from Hercai import Hercai
import requests

herc = Hercai()

question_result = herc.question(model="v3", content="How are you?")
print(question_result)

image_result = herc.draw_image(model="simurg", prompt="4k formula1")
print(image_result)
