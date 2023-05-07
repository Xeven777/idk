import tkinter as tk
import openai

openai.api_key = "OPENAPI KEY"

class ChatBot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat Bot")

        self.label = tk.Label(self.root, text="Hello! I am your chatbot. You can ask me any question!")
        self.label.pack(padx=20, pady=20)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=20, pady=20)

        self.button = tk.Button(self.root, text="Send", command=self.send_message)
        self.button.pack(padx=20, pady=20)

    def send_message(self):
        prompt = self.entry.get()
        if prompt.lower() == 'exit':
            self.root.quit()
        else:
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": prompt}]
        
            )
            reply = completion.choices[0]
            
            
            self.label.config(text=reply["message"]["content"])

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.run()
