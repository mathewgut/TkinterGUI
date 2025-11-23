# package imports
import tkinter as tk
import tkinter.ttk as ttk

def NameSubmit():
    print("lol")

# create root window
root = tk.Tk()

# create style
# styles: alt, default, classic, clam
style = ttk.Style()
style.theme_use('clam')

# creates a custom style under the widgets class
style.configure(
    "Exit.TButton", font=("Helvetica",14),
background="red",foreground="white")

style.configure(
    "Default.TEntry",
)

# use map to configure styles based on state

style.map(
    "Default.TEntry",
    relief=[("focus","raised"),("!focus","sunken")],
    borderwidth=[("focus",4),("!focus",2)],
    bordercolor=[("focus","red"),("!focus","black")]
)

style.map("Exit.TButton",
          background=[('active', '#cf4036'), ('pressed', '#1e7e34')],
          font=[("active",("Helvetica",14,"bold"))]
          )

# edit size
root.geometry("500x500")

# window title
root.title("Hello Form")

label = tk.Label(root, text="Enter your name :)", font=("Arial", 20))
entry = ttk.Entry(root, font=("Arial", 20), style="Default.TEntry")
button = ttk.Button(root, text="Close", command=root.destroy, style="Exit.TButton")

label.pack(padx=20, pady=20)
entry.pack(padx=20, pady=20)
button.pack(padx=20, pady=20)

root.mainloop()