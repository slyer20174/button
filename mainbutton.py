from tkinter import *  
window = Tk()
window.title("Event Handler")
window.geometry("300x500")
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nThe Button was clicked!")
button = Button(text="Click me!")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()