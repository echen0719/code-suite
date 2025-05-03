import tkinter

frame = tkinter.Tk()
frame.geometry('250x150') # like setSize() for Swing

label = tkinter.Label(frame, text = 'I am Steve! Don\'t press the button!', font = 'Arial -12 bold')
# label with 12 point bolded Arial font saying ridiculous things

button = tkinter.Button(frame, text = 'Don\'t do it!', command = frame.quit, bg = 'black', fg = 'white')
# black button with white text

scale = tkinter.Scale(frame, from_ = 0, to = 100, orient = tkinter.HORIZONTAL)
scale.set(50)

# tkinter calls them scale. In Swing, it is Slider

label.pack()
scale.pack(fill=tkinter.X)
button.pack(fill=tkinter.X)

# like add() for Swing

tkinter.mainloop()