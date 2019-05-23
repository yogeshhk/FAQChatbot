# FAQs ChatBot

Finds most matching question for your query in the FAQs and retrieves corresponding answer.

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
