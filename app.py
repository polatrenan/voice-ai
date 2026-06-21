import tkinter as tk
import webbrowser
import os

root = tk.Tk()
root.title('Voice Assistant')
root.geometry('600x400')
root.configure(bg='#2c3e50')

label = tk.Label(root, text='Voice AI Assistant', font=('Arial', 20, 'bold'), bg='#2c3e50', fg='white')
label.pack(pady=10)

def open_github():
    webbrowser.open('https://github.com')

def open_roblox():
    webbrowser.open('https://www.roblox.com')

def open_youtube():
    webbrowser.open('https://www.youtube.com')

def open_google():
    webbrowser.open('https://www.google.com')

def open_notepad():
    os.startfile('notepad.exe')

def open_paint():
    os.startfile('mspaint.exe')

def open_verkenner():
    os.startfile('explorer.exe')

btn_frame = tk.Frame(root, bg='#2c3e50')
btn_frame.pack(pady=20)

tk.Button(btn_frame, text='GitHub', command=open_github, width=15, font=('Arial', 12), bg='#3498db', fg='white').pack(pady=5)
tk.Button(btn_frame, text='Roblox', command=open_roblox, width=15, font=('Arial', 12), bg='#3498db', fg='white').pack(pady=5)
tk.Button(btn_frame, text='YouTube', command=open_youtube, width=15, font=('Arial', 12), bg='#3498db', fg='white').pack(pady=5)
tk.Button(btn_frame, text='Google', command=open_google, width=15, font=('Arial', 12), bg='#3498db', fg='white').pack(pady=5)
tk.Button(btn_frame, text='Notepad', command=open_notepad, width=15, font=('Arial', 12), bg='#27ae60', fg='white').pack(pady=5)
tk.Button(btn_frame, text='Paint', command=open_paint, width=15, font=('Arial', 12), bg='#27ae60', fg='white').pack(pady=5)
tk.Button(btn_frame, text='Verkenner', command=open_verkenner, width=15, font=('Arial', 12), bg='#27ae60', fg='white').pack(pady=5)

root.mainloop()
