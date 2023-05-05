import requests
import json
import tkinter as tk

def get_definition():
    try:
        word = entry_word.get().strip()
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        data = json.loads(response.text)

        text_definition.delete('1.0', tk.END)
        if 'title' in data:
            text_definition.insert(tk.END, f"No definition found for '{word}'")
        else:
            for meaning in data[0]['meanings']:
                part_of_speech = meaning['partOfSpeech']
                text_definition.insert(tk.END, f"{part_of_speech.capitalize()}:\n", 'bold')
                for definition in meaning['definitions']:
                    text_definition.insert(tk.END, u'\u2022' + definition['definition'] + '\n', 'bullet')

    except Exception as e:
        text_definition.delete('1.0', tk.END)
        text_definition.insert(tk.END, f"An error occurred: {str(e)}")

# Create the GUI
root = tk.Tk()
root.title("Mini Dictionary :) ")

# Create the widgets
label_word = tk.Label(root, text="Enter Word:", font=("Arial", 14))
entry_word = tk.Entry(root, width=30)
button_search = tk.Button(root, text="Search!", command=get_definition)
text_definition = tk.Text(root, wrap=tk.WORD)
text_definition.tag_configure('bold', font=('Verdana', 10, 'bold'))
text_definition.tag_configure('bullet', lmargin1=20, lmargin2=40)

# Add the widgets to the layout
label_word.grid(row=0, column=0, padx=10, pady=10)
entry_word.grid(row=0, column=1, padx=10, pady=10)
button_search.grid(row=0, column=2, padx=10, pady=10)
text_definition.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI
root.mainloop()
