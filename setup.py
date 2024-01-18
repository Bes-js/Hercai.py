from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hercai",
    version="3.1.0",
    author="fivesobes",
    description="A powerful Python Package for interacting with the Herc.ai API.",
    fullname="hercai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bes-js/Hercai.py",
    packages=find_packages(),
    license="GPL-3.0",
    keywords=["ai","chatbot","chatgpt","gpt","API","web","arc","smart","smartestchatbot","api","dalle","dall-e","text2image","texttoimage","text2img","texttoimg","image","image-generator","midjourney","diffusion","dall-e2","ai-images","ai-images-generator","gpt",
    "discord","chat","chatbot","chatgpt4","chatgpt-4","openai","open-ai","hercai","herc","herc.ai","smartest","bot","robot","axios",
    "canvafy","streamed-chatgpt-api","dart-openai-sdk","completions","cli","bin","command","console","cmd","bing","bing-chat","openaiapi","open.ai","openai-api","luppux","fivesobes","gemini","gemini-api","gemini-pro","google","five","bes","discord-ai","discordai","free","lodash","react","next","chalk","free","lodash","stable","anime","bes","fivesobes","five"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    requires=["requests"],
    zip=False,
)
