import requests

class Hercai:
    def __init__(self, api_key=""):
        if api_key is None or api_key == "" or not isinstance(api_key, str):
            self.api_key = ""
        else:
            self.api_key = api_key
 
    def question(self, model="v3", content=None, personality=""):
        if model not in ["v3", "gemini", "v3-32k", "turbo", "turbo-16k"]:
            model = "v3"
        if not content:
            raise ValueError("Please specify a question!")

        try:
            api = requests.get(
                f"https://hercai.onrender.com/{model}/hercai?question=" + requests.utils.quote(content),
                headers={"content-type": "application/json","Authorization": self.api_key},
                data={"personality":personality}
            )
            return api.json()
        except Exception as err:
            raise ValueError("Error: " + str(err))
  
    def draw_image(self, model="v3", prompt=None, negative_prompt=None):
        if model not in ["v1", "v2", "v2-beta", "v3", "lexica", "prodia", "simurg", "animefy", "raava", "shonin"]:
            model = "prodia"
        if not prompt:
            raise ValueError("Please specify a prompt!")
        if not negative_prompt:
            negative_prompt = ""

        try:
            api = requests.get(
                f"https://hercai.onrender.com/{model}/text2image?prompt="
                + requests.utils.quote(prompt)
                + "&negative_prompt="
                + requests.utils.quote(negative_prompt),
                headers={"content-type": "application/json","Authorization": self.api_key},
                data={"key": self.api_key},
            )
            return api.json()
        except Exception as err:
            raise ValueError("Error: " + str(err))
