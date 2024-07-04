import requests

class Hercai:
    def __init__(self, api_key=""):
        if api_key is None or api_key == "" or not isinstance(api_key, str):
            self.api_key = ""
        else:
            self.api_key = api_key
 
    def question(self, model="v3", content=None):
        if model not in ["v3", "gemini", "v3-32k", "turbo", "turbo-16k", "llama3-70b","llama3-8b","mixtral-8x7b","gemma-7b","gemma2-9b"]:
            model = "v3"
        if not content:
            raise ValueError("Please specify a question!")

        try:
            api = requests.get(
                f"https://hercai.onrender.com/{model}/hercai?question=" + requests.utils.quote(content),
                headers={"content-type": "application/json","Authorization": self.api_key},
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
        

    def beta_question(self,content=None,user=None):
        if not user:
            user = ""
        if not content:
            raise ValueError("Please specify a question!")

        try:
            api = requests.get(
                f"https://hercai.onrender.com/beta/hercai?question=" + requests.utils.quote(content)+"&user="+requests.utils.quote(user),
                headers={"content-type": "application/json","Authorization": self.api_key},
            )
            return api.json()
        except Exception as err:
            raise ValueError("Error: " + str(err))



    def beta_draw_image(self,prompt=None, negative_prompt=None,sampler="DPM-Solver",image_style="Null",width=1024,height=1024,steps=20,scale=5):
        if sampler not in ["DPM-Solver","SA-Solver"]:
            sampler = "DPM-Solver"
        if image_style not in ["Cinematic" , "Photographic" , "Anime" , "Manga" , "Digital Art" , "Pixel art" , "Fantasy art" , "Neonpunk" , "3D Model" , "Null"]:
            image_style = "Null"
        if not prompt:
            raise ValueError("Please specify a prompt!")
        if not negative_prompt:
            negative_prompt = ""

        try:
            api = requests.get(
                f"https://hercai.onrender.com/beta/text2image?prompt="
                + requests.utils.quote(prompt)
                + "&negative_prompt="
                + requests.utils.quote(negative_prompt)
                + "&sampler="
                + requests.utils.quote(sampler)
                + "&image_style="
                + requests.utils.quote(image_style)
                + "&width="
                + width
                + "&height="
                + height
                + "&steps="
                + steps
                + "&scale="
                + scale,
                headers={"content-type": "application/json","Authorization": self.api_key},
                data={"key": self.api_key},
            )
            return api.json()
        except Exception as err:
            raise ValueError("Error: " + str(err))
