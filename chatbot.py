import customtkinter as ctk
import tkinter as tk 
from nltk.chat.util import Chat, reflections
from chat_pairs import pairs  
import re
chatbot = Chat(pairs, reflections) 

def calculate(userinput):
    match = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", userinput)
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))

        if operator == '+':
            result = num1 + num2
            operation = "Addition"
        elif operator == '-':
            result = num1 - num2
            operation = "Subtraction"
        elif operator == '*':
            result = num1 * num2
            operation = "Multiplication"
        elif operator == '/':
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2
            operation = "Division"
        
        return f"{operation} of {num1} and {num2} is {result}"
    else:
        return None 
        

def send_message():
    userinput = userentry.get()
    if userinput.lower() == "quit":
        window.quit()
    else:
        chatarea.config(state=tk.NORMAL)
        chatarea.insert(tk.END, "\n")
        chatarea.insert(tk.END, f"{userinput}\n\n", "right")
        userentry.delete(0, tk.END)
       
        bot_response = calculate(userinput)
        
        if bot_response is None:
            bot_response = chatbot.respond(userinput)

        chatarea.insert(tk.END, f"{bot_response}\n", "left")
        chatarea.config(state=tk.DISABLED)
        chatarea.yview(tk.END)


ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

window = ctk.CTk()  
window.title("Chatbot")
window.geometry("500x500")

chatarea = tk.Text(window, wrap="word", state=tk.DISABLED, height=20)
chatarea.tag_configure("right", justify="right")  
chatarea.tag_configure("left", justify="left")    
chatarea.pack(pady=10, padx=10, fill="both", expand=True)

userentry = ctk.CTkEntry(window, width=400, height=30)
userentry.pack(pady=10, padx=10)
userentry.bind("<Return>", lambda event: send_message()) 

button = ctk.CTkButton(window, text="Send", width=150, command=send_message)
button.pack(pady=5)
window.mainloop()
