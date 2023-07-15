# import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from transformers import pipeline
import pandas as pd

# initialize tkinter window
root = tk.Tk()
root.title("Table Q&A")
root.geometry("500x400")
root.iconbitmap('icon.ico')

# create model object
get_answer = pipeline(task='table-question-answering', model='google/tapas-base-finetuned-wtq')

# styling
style = ttk.Style()
style.configure("Treeview.Heading", font=("TkDefaultFont", 12, "bold"))
style.configure("Treeview", font=("TkDefaultFont", 12))
style.configure("TEntry", font=("TkDefaultFont", 12))

data = {
    'names':['Kamal', 'Saman', 'Nuwan', 'Gayan', 'Pawan'],
    'ages':[43, 54, 23, 23, 42],
    'results':['Pass', 'Fail', 'Fail', 'Pass', 'Pass']
}

# get model prediction
def handle_enter(event):
    df = pd.DataFrame(data)
    model_answer = get_answer(table=df.astype(str), query=question.get())
    answer.configure(text=model_answer['answer'])

# initialize table view
table = ttk.Treeview(root, columns=('name', 'age', 'result'), show='headings')
table.column('age', width=150, anchor='center')
table.column('result', width=150, anchor='center')
table.column('name',width=150, anchor='center')
table.heading('name', text='Name')
table.heading('age', text='Age')
table.heading('result', text='Result')
table.pack(pady=(10,0))

# insert data to table
for idx, value in enumerate(data['names']):
    table.insert('', index=idx, values=(data['names'][idx], data['ages'][idx], data['results'][idx]))

queston_label = ttk.Label(root, text='Question', font=Font(weight='bold'))
queston_label.pack(pady=(10,0))

# tkinter variable to store question
question = tk.StringVar(value = '')

question_entry = ttk.Entry(root, textvariable=question, font=("TkDefaultFont", 12), width=50)
question_entry.pack()

answer_label = ttk.Label(root, text='Answer', font=Font(weight='bold'))
answer_label.pack(pady=(10,0))

answer = ttk.Label(root, text='', font=("TkDefaultFont", 12))
answer.pack()

# event binding
root.bind("<Return>", handle_enter)

# run the window
root.mainloop()