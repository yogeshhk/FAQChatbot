# Notes on FAQs ChatBot

## Thoughts
* Fun: getting answer automatically is magic!! its a strong AI
* 3-word mission: For the Future
* Principles
	* Be Different and Better, if you do the same as others you will be the same as others 
	* Be rare, be valuable

## To Do
*	Make beamer 3hr hands-on course, make ipynb for demo, do meetup/seminars
*	Build full FAQ chatbot (a retrieval-based atomic question answering bot)
    * Like QnA maker, feed FAQs/Database
    * Options: 
        * RASA NLU based, with auto training file preparation
        * Retrieval based on Word2Vec of sentences and cosine similarity
    * Deploy it on Heroku and give link from Yati.io with documentation and disclaimer
    * Use this as demo PoC to get better chatbot projects
*	Build State machine (or pre-defined dialog tree) based chatbaot with Rasa NLU and Core
*	Research: SIG IR: entity extraction, Answer selection is part of Information retrieval 

## Queries Posted on Rasa/Stack Overflow Forums
*	https://forum.rasa.com/t/building-faq-chatbot-like-qna-maker/3791 I am building a QnA chatbot, say for College admissions. FAQs related to this are already available in form of pairs of Questions and Answers. For ready frameworks such as “QnA Maker”, I believe, one must supply the faqs and it builds the rest. ...
* 	https://forum.rasa.com/t/rasa-core-sdk-not-working/9228  for rasa_core_sdk not working
* 	https://forum.rasa.com/t/mapping-faq-with-rasa-for-large-dataset-2000/2406
* 	https://forum.rasa.com/t/faq-bot-knowledge-base/742

## Rasa Experts
*	Ishwar Sawale, Pune https://www.linkedin.com/in/ishwarsawale/ (“robot” on rasa forum)
*	Shailesh S Sarda, Pune https://www.linkedin.com/in/shailesh-s-sarda-85a8a2124/ 
*	Jitesh Gaikwad, Mumbai https://www.linkedin.com/in/jitesh-gaikwad-4b4047b8/
*	Ajinkya Pathak, Pune https://www.linkedin.com/in/ajinkyanpathak/
*	Peeyush Kumar, Bengaluru https://www.linkedin.com/in/peeyushk/

## Frameworks
*	ChatScript: open-source, written in C and C++, and publicly available on GitHub for everyone to study and adopt.
*	Pandorabots: allows businesses to create and host their own chat bots that can have human-like text or voice chats with customers. Parts of this bot platform are licensed under GPL. Pandorabots supports AIML, an XML dialect for creating natural language software agents. Pandorabots provides the base bot Rosie as a template for creating your own. Rosie is available on Github, and is a set of AIML and AIML 2.0 files which can form the base for any chatbot project.
*	IBM Watson: The first choice as a bot-building platform for 61% of businesses. Python SDK. Free plan.
*	Microsoft Bot Framework: own Bot Builder SDK that includes .NET SDK and Node.js SDK.  It is possible to incorporate LUIS for natural language understanding, Cortana for voice, and the Bing APIs for search.
*	Wit.ai: Free. Python.
*	Api.ai: Google. Python.
*	Chatfuel: More than 360,000 chatbots have been created using Chatfuel, serving more than 17 million users globally. Free.
*	ChatterBot: Python.
*	Chatscript: A rule-based engine. Rules are created in program scripts through a process called dialog flow scripting.
*	Rasa NLU has HTTP API and Python support, intent classification, and entity extraction [19]; it is an open source tool that runs locally.
Platforms like IBM Watson, Microsoft Bot Framework, Api.ai, ChatScript and Pandorabots were developed ten or more years ago. Therefore, their experience provides the most advanced tools and offers the most flexible solutions for businesses.

## A chat with Subham Mahanta
*	Basic chatbot is of Question Answers type.
*	AIML is too old, 15-year-old technology, is also like similarity based fetching of answers.
*	Newer approach is database or dictionary based similarity fetching.
*	Dictionary with Question as key and its answer as value. Build such databases, pickle it.
*	Users sentences is matched (cosine similarity) with keys ie questions and the one with most, its answer is given back.
*	Front end can be html css etc
*	For encoding sentences, sklearn’s count vectorizer is good.
*	If the match is below some threshold then say, “Could not understand!!”
*	RASA-NLU type chatbots are call-back based.
*	Its local engine is trained manually for intent and entities identification
*	For each identified intent, a call-back function is programmed with entities as its arguments.
*	Call-back can do processing, call database or API, get the answer, which can be pasted as is.


## References to update the Training Material
*	Dialogs stats , Slot tutorial https://medium.com/datadriveninvestor/build-a-flight-search-chatbot-from-scratch-using-rasa-part-1-47370cf1e53b 
*	The talk would be about Rasa, an open-source chatbots platform - Nathan Zylbersztejn https://www.youtube.com/watch?v=0hZay4KSLFw
*	Conversational AI with Rasa Core & NLU - Tom Bocklisch https://www.youtube.com/watch?v=zRqjH7fT0G0 
*	Start contributing to Rasa https://rasa.com/community/contribute/
*	Rasa NLU+dialog->tex course
*	Full GST chatbot on Heroku w disclaimer then link from Yati.io
*	Rasa Blog https://blog.rasa.com/?_ga=2.169818913.1472851714.1538279040-209190406.1538279040   https://medium.com/rasa-blog  https://medium.com/rasa-blog/tagged/tutorial 
*	Put on your robot costume and be the Minimum Viable Bot yourself ! https://blog.rasa.com/put-on-your-robot-costume-and-be-the-minimum-viable-bot-yourself/ 
*	Datacamp course https://campus.datacamp.com/courses/building-chatbots-in-python/chatbots-101?ex=1 
*	Building a chatbot with Rasa NLU and Rasa Core https://vimeo.com/254777331
*	How to Build a Chatbot with RASA : Complete Guide https://www.datasciencelearner.com/how-to-build-a-chatbot-rasa-complete-guide/
*	Building a chatbot with Rasa https://itnext.io/building-a-chatbot-with-rasa-9c3f3c6ad64d 
*	Rasa Python Weather Chatbot https://medium.com/coinmonks/rasa-python-weather-chatbot-51fc218d346d
*	Supervised Word Vectors from Scratch in Rasa NLU https://medium.com/rasa-blog/supervised-word-vectors-from-scratch-in-rasa-nlu-6daf794efcd8 
*	Building with Rasa: eLearning chatbot https://medium.com/rasa-blog/building-with-rasa-elearning-chatbot-2212399a9b8b 
*	https://github.com/GetStoryline/awesome-bots 
*	Chatbots with Machine Learning: Building Neural Conversational Agents https://blog.statsbot.co/chatbots-machine-learning-e83698b1a91e
