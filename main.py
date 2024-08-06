import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.title("Sparkle Notes")

text = tk.Text(root, wrap="word", undo=True)
text.pack(expand="yes", fill="both")


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
    root.mainloop()

if __name__ == '__main__':
    setup_window()
