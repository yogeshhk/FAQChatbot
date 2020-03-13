# FAQs ChatBot

Simple Question-Answer (atomic query) based chatbot framework. 
Uses similarity based on different vectorizers, to find the matching question then responds with its corresponding answer.

NLP is real AI, the Turing test.

Scope: 
- Huge demand to take care of mundane queries
- Scales (leverage, automation, passive)
- Not much work in vernacular chatbot (serve humanity)

Different than the popular open source chatbot framework, Rasa, where NLU is based on intent and entities, whereas dialog management is based on sequence/LSTM prediction. 

This chatbot is solely based on similarity.

Conceptually it is similar to Microsoft's QnA Maker. But the big difference is that, if you get whole code-base, your models would be local. Nothing on Server. So better security especially for sensitive data chatbots like HR or Finance.

Copyright (C) 2019 Yogesh H Kulkarni

## License:
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or any later version.

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

<img src="faqchatbot.png" alt="chatwindow" width="400"/>

## Dependencies:
* Needs Python 3.6, numpy, scipy, sklearn

## ToDos
* Add more training data


## References
* Bhavani Ravi’s event-bot [code](https://github.com/bhavaniravi/rasa-site-bot), Youtube [Video](https://www.youtube.com/watch?v=ojuq0vBIA-g)
* Banking FAQ Bot [code](https://github.com/MrJay10/banking-faq-bot)

## Disclaimer:
* Author (yogeshkulkarni@yahoo.com) gives no guarantee of the results of the program. It is just a fun script. Lot of improvements are still to be made. So, don’t depend on it at all.
