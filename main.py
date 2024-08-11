import tkinter as tk
from tkinter import filedialog
from tkinter import font , filedialog
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText
from markdown2 import Markdown
from tkhtmlview import HTMLLabel
from ttkbootstrap import Style


style = Style(theme='cyborg')
root = style.master
root.title("Sparkle Notes")


default_font = ("Ubuntu Light" ,12)
text =  tb.ScrolledText(root, wrap="word", undo=True, font=default_font)
text.pack(fill=tk.BOTH, side=tk.LEFT)


outputbox = HTMLLabel(root, width="1", background="white", html="<h1>Welcome</h1>")


def new_file():
    text.delete("1.0", tk.END)
    root.title("Sparkle Notes")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)
        root.title(file_path)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get("1.0", tk.END)
            file.write(content)
        root.title(file_path)

def change_theme(theme):
    if theme == 'ubuntu':
        text.config(background='#300924', foreground='white')
        outputbox.config(background='white')

    elif theme == 'light':
        text.config(background='white', foreground='black')
        outputbox.config(background='white')
    
    elif theme == 'dark':
        text.config(background='#26242f', foreground='white')
        outputbox.config(background='white')
        
    elif theme == 'superhero':
        Style(theme='superhero')
        outputbox.config(background='white')

    elif theme == 'solar':
        Style(theme='solar')
        outputbox.config(background='white')

    elif theme == 'cyborg':
        Style(theme='cyborg')
        outputbox.config(background='white')

    elif theme == 'darkly':
        Style(theme='darkly')
        outputbox.config(background='white')

    elif theme == 'vapor':
        Style(theme='vapor')
        outputbox.config(background='white')

    elif theme == 'pulse':
        Style(theme='pulse')
        outputbox.config(background='white')

def onInputChange(event):
    text.edit_modified(0)
    md2html = Markdown()
    outputbox.set_html(md2html.convert(text.get("1.0" , tk.END)))

def select(event=None):
    text.tag_add('sel', '1.0', 'end')
    return "break"

def setup_window():

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # File-menu
    file_menu = tk.Menu(menu_bar, tearoff=-1)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)

    # View-Menu
    view_menu = tk.Menu(menu_bar)
    menu_bar.add_cascade(label='View', menu=view_menu)

    # Appearance sub-menu

    appearance_menu = tk.Menu(view_menu)
    view_menu.add_cascade(label='Appearance', menu=appearance_menu)
    appearance_menu.add_command(label='Dark', command= lambda : change_theme('dark'))
    appearance_menu.add_command(label='Ubuntu', command= lambda : change_theme('ubuntu'))
    appearance_menu.add_command(label='Light', command= lambda : change_theme('light'))
    appearance_menu.add_command(label='Solar', command= lambda : change_theme('solar'))
    appearance_menu.add_command(label='Cyborg', command= lambda : change_theme('cyborg'))
    appearance_menu.add_command(label='Vapor', command= lambda : change_theme('vapor'))
    appearance_menu.add_command(label='Darkly', command= lambda : change_theme('darkly'))
    appearance_menu.add_command(label='Superhero', command= lambda : change_theme('superhero'))
    appearance_menu.add_command(label='Pulse', command= lambda : change_theme('pulse'))

    # Output window

    outputbox.pack(fill=tk.BOTH, expand=1, side=tk.RIGHT)
    outputbox.fit_height()
    outputbox.config(background='white')

    # Calling function whenever the text is modified

    text.bind("<Return>", onInputChange)
    text.bind('<Control-a>',select)

    

    root.mainloop()



if __name__ == '__main__':
    setup_window()
