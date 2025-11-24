# package imports
import tkinter as tk
import tkinter.ttk as ttk
import socket
import requests

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
submit_flag = False

# create root window
root = tk.Tk()

# create style
# styles: alt, default, classic, clam
style = ttk.Style()
style.theme_use('clam')

# creates a custom style under the widgets class
style.configure(
    "Exit.TButton", font=("Helvetica",14),
    background="red",foreground="white"
)

style.configure(
    "Submit.TButton", font=("Helvetica",14),
    background="green",foreground="white"
)

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

style.map(
    "Exit.TButton",
    background=[('active', '#cf4036'), ('pressed', '#1e7e34')],
    font=[("active",("Helvetica",14,"bold"))]
)

style.map(
    "Submit.TButton", background=[('active', '#5ebd4f'), ('pressed', '#1e7e34')],
    font=[("active",("Helvetica",14,"bold"))]
)

# edit size
root.geometry("500x500")

# window title
root.title("Hello Form")

label = tk.Label(root, text="Enter your name :)", font=("Arial", 20))
entry = ttk.Entry(root, font=("Arial", 20), style="Default.TEntry")
exit_button = ttk.Button(root, text="Close", command=root.destroy, style="Exit.TButton")


def Submit():

    global submit_flag
    submit_flag = True

    # IPV6 used to find accurate information, ipv4's tend to be restrictive for some reason
    IP6 = requests.get("https://api6.ipify.org?format=json").json()
    IP6 = IP6["ip"]

    # fetch location data from IPV6
    response = requests.get(f"http://ipwho.is/{IP6}").json()

    # create variables for label text
    lat = response["latitude"]
    long = response["longitude"]
    city = response["city"]
    isp = response["connection"]["isp"]

    # create labels including text variables
    ip_label = tk.Label(root, text=f"Hi {entry.get()}, your IP is {IP}")
    isp_label = tk.Label(root, text=f"ISP: {isp}")
    city_label = tk.Label(root, text=f"City is {city}")
    lat_long_label = tk.Label(root, text=f"Latitude: {lat}, Longitude: {long}")
    threat_label = tk.Label(root, text=f"Dispatching drone strike to {city}, {lat}, {long}", font=("Arial",12))

    # pack and show variables
    ip_label.pack(pady=2)
    isp_label.pack()
    city_label.pack()
    lat_long_label.pack()
    threat_label.pack()
    return

# fetch ip information including name on click
submit_button = ttk.Button(root, text="Submit", style="Submit.TButton", command=Submit)

# pack static widgets
label.pack(padx=20, pady=20)
entry.pack(padx=20, pady=20)
exit_button.pack(pady=5)
submit_button.pack(pady=5)


root.mainloop()