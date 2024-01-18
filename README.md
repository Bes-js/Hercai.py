<p align="center"> <a href="#"> <img width=500 src="https://raw.githubusercontent.com/Bes-js/herc.ai/main/hercai-logo.png"></a></p> 
<p align="center"> <a href="https://render.com?ref=hercai"> <img width=200 height=90 src="https://raw.githubusercontent.com/Bes-js/herc.ai/main/render-logo.png"></a> </p>
<p align="center"> <img src="https://img.shields.io/github/repo-size/Bes-js/Hercai.py?style=for-the-badge"> <img src="https://img.shields.io/github/contributors/Bes-js/Hercai.py?style=for-the-badge"> <a href="https://discord.gg/luppux" target="_blank"> <img alt="Discord" src="https://img.shields.io/badge/Support-Click%20here-7289d9?style=for-the-badge&logo=discord"></p>

# [Herc.ai](https://discord.gg/luppux)

> **A powerful Python Package for interacting with the [Herc.ai](https://discord.gg/luppux) API.**

> **We Offer It To You For Free.**
> **[Herc.ai](https://discord.gg/luppux) Answers Your Question According To The Language, And It Supports All Languages.**

> **[✨ How about a one-time subscription to benefit from Hercai's features unlimitedly?](https://hercai-shop.onrender.com)**
**[✨ Use Hercai Unlimited with API Key!](https://hercai-shop.onrender.com)**
#
### ❔ [Support](https://discord.gg/luppux)
### 📖 [Document's](https://fivesobes.gitbook.io/hercai/)
### 📝 [Github](https://github.com/Bes-js/Hercai.py)
#
**📂 Installation**
```lua
pip install hercai
```
#
# Quick Example

**Exampe Construction;**
```py
 from hercai import Hercai
 herc = Hercai("") # If you have a Hercai API Key, please define it in this section. 
```
 
 > **Question API; [https://hercai.onrender.com/v3/hercai?question=](https://hercai.onrender.com/v3/hercai?question=)**

**Example Question For Python;**
```py
# Available Models 
# "v3" , "v3-32k" , "turbo" , "turbo-16k" , "gemini" 
# Default Model; "v3" 
# Premium Parameter; personality => Optional
question_result = herc.question(model="v3", content="hi, how are you?")
print(question_result)
# print(question_result["reply"]) For Reply
```
#

> **Text To Image API; [https://hercai.onrender.com/v3/text2image?prompt=](https://hercai.onrender.com/v3/text2image?prompt=)**

**Example Draw Image For Python;**
```py
# Available Models 
# "v1" , "v2" , "v2-beta" , "v3" (DALL-E) , "lexica" , "prodia", "simurg", "animefy", "raava", "shonin" 
# Default Model; "v3" 
image_result = herc.draw_image(model="simurg", prompt="A beautiful landscape", negative_prompt="Dark and gloomy")
print(image_result)
# print(image_result["url"]) For Image URL        
```

#
# Credits
 
**[NPM Package For JavaScript & TypeScript](https://www.npmjs.com/package/hercai)**
#
**Made by [FiveSoBes](https://github.com/Bes-js) And [Luppux Development](https://github.com/Luppux)**


# Contact & Support

[![Discord Banner](https://api.weblutions.com/discord/invite/luppux/)](https://discord.gg/luppux)
