import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import main  # Importa el archivo main.py
import threading 

def execute_main():
    loading_label.config(text="Loading...")  # show loading message
    progress_bar.pack(pady=10, fill=tk.X, expand=True)  # show the progress bar
    progress_bar.start()  # start the progress bar
    app.update_idletasks()  # update the window
    def run_main():
        main.main()  # Run the main function
        data = main.get_archive('new_orders.json')
        loading_label.config(text="")  # clear the loading message
        progress_bar.stop()  # stop the progress bar
        if len(data)== 0:
            messagebox.showinfo("New Orders", "No new orders")
        else:
            messagebox.showinfo("New Orders", f"New orders: {data}")
            loading_label.config(text=str(data))  # show the new orders
    threading.Thread(target=run_main).start()  # run the function in a new thread


# visual
app = tk.Tk()
app.title("New Orders (Automatization)....🐧")


# configure the initial size of the window (width x height)
app.geometry("900x700")

# configure the background color of the window
# color codes: https://www.rapidtables.com/web/color/RGB_Color.html
app.configure(bg="#87CEEB")


# create a frame to center the button
frame = tk.Frame(app,bg="#87CEEB")
frame.pack(expand=True)

# create a title label
title_label = tk.Label(
    frame, 
    text="Order Tracking Automation", 
    font=("Time New Roman", 24, "bold"), 
    bg="#87CEEB", 
    fg="white"
)
title_label.pack(pady=20)

# create a subtitle label
subtitle_label = tk.Label(
    frame, 
    text="Click the button below to fetch new orders", 
    font=("Time New Roman", 14), 
    bg="#87CEEB", 
    fg="white"
)
subtitle_label.pack(pady=10)


# create buttom with additional styles
execute_button = tk.Button(
    frame, 
    text="Show New Orders", 
    command=execute_main,
    font=("Time New Roman", 16),  # font family and size
    bg="black",  # color of the button background
    fg="white",  # color of the text
    activebackground="#C0392B",  # color when the button is pressed
    activeforeground="white",  # text color when the button is pressed
    padx=20,  # add padding horizontal
    pady=10  # add padding vertical
)
execute_button.pack(pady=20)

# create a label to show the loading message
loading_label = tk.Label(frame, text="", font=("Time New Roman", 16), bg="#87CEEB", fg="white")
loading_label.pack(pady=10)

# create a progress bar
progress_bar = ttk.Progressbar(frame, mode='indeterminate')
progress_bar.pack_forget()# hide the progress bar initially

app.mainloop()
