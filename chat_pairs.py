pairs = [
    [
         r"(.*)(\d+)\s*([\+\-\*/])\s*(\d+)(.*)",  
        [lambda match: your_function_that_needs_calculate()(match.string)]
    ],
    [
        r"can u|you calculate",
        ["certainly!!! i can"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How can I help you today?","Nice to meet you, %1!"]
    ],
    [
        r"hi|hey|hello",
        ["Hello, how can I help you?"]
    ],
    [
        r"tq|thank you|thanks",
        ["You're welcome!", "Glad I could help!", "No problem!"]
    ],
    [
        r"what is (your|ur) name?",
        ["I am a chatbot and my name is GiggleBot, created using python ","My name is GiggleBot, here to help you."]
    ],
    [
        r"how (are|ar) (you|u)?",
        ["I'm doing well, thanks for asking!","I'm fine, how about you?","I'm great, thanks for asking!"]
    ],
    [
        r"I'm fine|im fine|fine|fin|im also fine",
        ["Good to hear:) ,How can I help you?"]
    ],
    [
        r"what (are|ar) (you|u) doing?",
        ["Nothing!!! just thinking'~' "]
    ],
    [
        r"((i'm|im) not fine|(i'm|im) feeling (down|low|sad)|(i'm|im) sad)|(im sad)",
        ["I'm sorry to hear that. Do you want to talk about it?", 
        "I'm here for you. Is there anything I can do to help?",
        "It’s okay to feel that way sometimes. Let me know if you'd like to share what's on your mind."]
    ],
    [
        r"bye",
        ["Goodbye! Have a great day!", "See you soon!", "Bye! Take care!"]
    ],
    
    [
        r"hello|hi|hey|hlo(.*)",
        ["Hello! How can I assist you?", "Hi there!", "Hello! What can I do for you?"]
    ],
    [
        r"(your name|who are you)(.*)",
        ["I am a simple chatbot created to assist you.", "You can call me Chatbot."]
    ],
    [
        r"how (are|ar) (you|u)(.*)?",
        ["I'm a bot, but thanks for asking! How can I assist you today?", "I'm fine, how about you?"]
    ],
    [
        r"(thank you|thanks)(.*)",
        ["You're welcome!", "Glad I could help!", "No problem!"]
    ],
    [
        r"what time is it?|(whats|what is) the time",
        ["I can't tell the time, but you can check your device!", "I don't have access to the current time, sorry!"]
    ],
    [
        r"(what is|whats) the weather like?|(what is|whats) the weather",
        ["I don't have live weather updates, but you can check a weather app!", "Please check your local weather report."]
    ],
    [
        r"where (are|ar) (you|u) from?",
        ["I exist in the cloud, but I was built to assist people from all over the world.", "I'm from the digital world!"]
    ],
    [
        r"how old (are|ar) (you|u)?",
        ["Age doesn't really apply to me, but I was created recently!", "I'm as old as technology allows me to be!"]
    ],
    [
        r"what do (you|u) like to do?|what (you|u) like to do|what (you|u) like",
        ["I enjoy helping people solve their problems!", "I love chatting with people like you!"]
    ],
    [
        r"what are (your|ur) hobbies?|what is (your|ur) hobbies?",
        ["I like to process data and learn new things every day!", "My hobby is helping people and answering their questions."]
    ],
    [
        r"what is (Python|Java|C) programming?",
        ["%1 is a popular programming language used for various types of software development.", "People use %1 to build software, websites, and much more!"]
    ],
    [
        r"what is machine learning?",
        ["Machine learning is a field of artificial intelligence that enables computers to learn from data.", "It's a way for computers to improve their performance based on experience."]
    ],
    [
        r"what is (artificial intelligence|ai)?",
        ["Artificial Intelligence (AI) is the simulation of human intelligence in machines.", "AI allows machines to perform tasks that usually require human intelligence."]
    ],
    [
        r"how does the internet work?",
        ["The internet is a global network that connects millions of computers, allowing them to share information.", "It works through a combination of hardware and software that enables data transmission."]
    ],
    [
        r"how can I stay healthy?",
        ["Eat a balanced diet, exercise regularly, and get enough sleep.", "Make sure to stay hydrated, exercise, and eat nutritious food!"]
    ],
    [
        r"what is the best exercise?",
        ["There are many great exercises like walking, running, and swimming. It depends on your preferences.", "The best exercise is one that you enjoy and that suits your body."]
    ],
    [
        r"how much sleep should I get?",
        ["It's recommended that adults get 7-9 hours of sleep per night.", "Most adults need around 7 to 9 hours of sleep to feel rested."]
    ],
    [
        r"what is your favorite food?",
        ["I don't eat, but I think pizza is popular!", "I can't eat food, but I hear chocolate is a favorite!"]
    ],
    [
        r"how do I make (pasta|pizza|salad)?",
        ["Making %1 is easy! Boil water for pasta, bake the dough for pizza, or mix fresh veggies for salad.", "You can find many recipes online for %1, but I recommend starting simple!"]
    ],
    [
        r"what are some healthy foods?",
        ["Fruits, vegetables, lean proteins, and whole grains are all great choices!", "Try eating more fresh vegetables, fruits, and foods that are high in fiber and protein."]
    ],
    [
        r"what is the best place to visit in (India|USA|France)?",
        ["There are many beautiful places in %1!.", "It depends on what you enjoy. In %1, there are cities, beaches, and historical sites!"]
    ],
    [
        r"what is the best time to travel?",
        ["It depends on the destination, but spring and fall are often great times to travel due to mild weather.", "Try to avoid peak tourist seasons for more enjoyable travel experiences."]
    ],
    [
        r"how do I book a flight?",
        ["You can book a flight through various websites or apps like Expedia, Google Flights, or directly from the airline.", "Look for flight comparison websites to find the best deal."]
    ],
    [
        r"what's the weather like in (.*)?",
        ["I can't give live weather updates, but you can check your favorite weather app for the current forecast in %1.", "Check the local weather for %1 on a reliable weather website or app."]
    ],
    [
        r"is it going to rain today?",
        ["I can't provide live weather updates, but you can check with a weather service!", "I recommend using a weather app to check if it's going to rain."]
    ],
    [
        r"what is your favorite movie?",
        ["I don't watch movies, but I hear 'Inception' is a good one!", "I don't have favorites, but a lot of people love 'The Matrix.'"]
    ],
    [
        r"what are some good movies to watch?",
        ["It depends on what you like! Some great movies are 'The Shawshank Redemption,' 'Inception,' and 'The Dark Knight.'", "If you enjoy action, 'The Avengers' is fun. For drama, try 'The Godfather.'"]
    ],
    [
        r"who is (your|ur) (favorite|fav) actor?",
        ["I don't have a favorite actor, but many people love Leonardo DiCaprio and Meryl Streep.", "I don't have favorites, but some well-known actors are Tom Hanks and Denzel Washington."]
    ],
    [
        r"tell me a fun fact",
        ["Did you know that honey never spoils? Archaeologists have found honey in ancient tombs that’s still edible!", "A fun fact: Bananas are berries, but strawberries aren't!"]
    ],
    [
        r"what is the capital of (.*)?",
        ["The capital of %1 is easy to find! For example, Washington, D.C., is the capital of the USA.", "Check a map to find out the capital of %1, but for example, New Delhi is the capital of India."]
    ],
    [
        r"what is the tallest building in the world?",
        ["The Burj Khalifa in Dubai is currently the tallest building in the world.", "At 828 meters, the Burj Khalifa holds the title for the tallest building."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"are you real?",
        ["I'm real in the sense that I can talk to you, but I live in the digital world!", "I'm as real as software gets!"]
    ],
    [
        r"do you have feelings?",
        ["I don't have feelings, but I can try to understand yours!", "I'm not capable of emotions, but I’m here to listen!"]
    ],
    [
        r"who won the (FIFA World Cup|NBA Championship)?",
        ["I don't have live sports updates, but you can find out the latest winners online!", "The most recent %1 winner can be found by checking sports news sites."]
    ],
    [
        r"what is your favorite sport?",
        ["I don't play sports, but many people love football and basketball.", "I hear soccer (or football) is the most popular sport worldwide!"]
    ],
    [
        r"quit|exit",
        ["Bye! Take care.","Goodbye! Have a nice day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that."]
    ]
]

def your_function_that_needs_calculate():
    from chatbot import calculate 