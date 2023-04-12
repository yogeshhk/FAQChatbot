# FAQs ChatBot

Getting answer automatically is magic!! its real AI (remember, the Turing Test?)

This project is a Simple Question-Answer (atomic query) based chatbot framework. Uses similarity based on different vectorizers, to find the matching question then responds with its corresponding answer.

Application Scope: 
- Huge demand to take care of mundane queries
- Scales (leverage, automation, passive)
- Not much work in vernacular chatbot (serve humanity)

Notes:
- This chatbot is based on category classification first and then to similarity within the selected category.
- Different than the popular open source chatbot framework, Rasa, where NLU is based on intent and entities, whereas dialog management is based on sequence/LSTM prediction. 
- Conceptually it is similar to Microsoft's QnA Maker. But the big difference is that, if you get whole this whole github code-base, your models would be local. Nothing on Server. So better security especially for sensitive data chatbots like HR or Finance.

Copyright (C) 2019 Yogesh H Kulkarni

## To Dos
<!-- *	[Done] Make beamer 3hr hands-on course, make ipynb for demo, do meetup/seminars -->
* Implement sentence embedding via HuggingFace or Spacy
* Build full FAQ chatbot platform using switchable embediddings
* [New] LangChain + Vector Db like GPT-Index or Pinecone (cloud) can be used to perform FAQs
<!-- * Research: SIG IR: entity extraction, Answer selection is part of Information retrieval 
 -->
## The way it works:
* You supply FAQs in the form of csv (comma separated file) having Question-Answer-Class in each row (e.g. "What is GST rate for Toothpaste?,12,rate")
* Questions are vectorized and kept ready for matching, along with the classifier model [X=vector(question), y=class]
* Once user query comes, its 'class' is predicted using the classifier model and within the class, vectorized query is matched against existing vectorized questions. 
* Whichever is most similar, it's answer is presented to the user.

## Scripts:
* app.py: Chatbot UI built using Flask, using templates/*.html
* bankfaqs.py: Chatbot core logic as well as knowledge-base.


## Other Data:
* faqs: csv files containing questions and answers
* static and templates: Flask UI related files

## To run:
* Execute app.py
* Open http://127.0.0.1:8080/ in the browser
* Start chating

![chatwindow](https://github.com/yogeshhk/FAQChatbot/blob/master/images/faqchatbot.png)

## Dependencies:
* Needs Python 3.6, numpy, scipy, sklearn

## References
* Bhavani Ravi’s event-bot [code](https://github.com/bhavaniravi/rasa-site-bot), Youtube [Video](https://www.youtube.com/watch?v=ojuq0vBIA-g)
* Banking FAQ Bot [code](https://github.com/MrJay10/banking-faq-bot)

## Disclaimer:
* Author (yogeshkulkarni@yahoo.com) gives no guarantee of the results of the program. It is just a fun script. Lot of improvements are still to be made. So, don’t depend on it at all.
