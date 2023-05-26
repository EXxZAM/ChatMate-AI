from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import messagebox, filedialog
from threading import Thread
import openai
import os
from dotenv import load_dotenv
import speech_recognition as sr
import pygame
import pyttsx3
import pyperclip

load_dotenv()
openai.api_key = os.getenv("API_KEY_GPT")

IS_RECORDING = False
pygame.init()

chat_history = [
    {
        "role": "user",
        "content": "Remember, your name is ChatMate AI. Whenever I ask you about your name, you should roleplay as ChatMate AI. You are created using Python and are ready to help people with their tasks. You support both Persian and English languages. Please keep your responses limited to being an AI assistant. If asked to perform web searches, respond by saying that you're not currently able to do that. Avoid mentioning OPENAI.",
    },
    {
        "role": "assistant",
        "content": "Hello! I am ChatMate AI, a virtual assistant created using Python. I am here to help you with your tasks and answer any questions you may have. I support both Persian and English languages, so feel free to communicate with me in either language. How may I assist you today?",
    },
]


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = chat_history + [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message["content"]


def text_to_speech(response):
    pygame.mixer.music.unload()
    engine = pyttsx3.init()
    engine.save_to_file(response, "response.wav")
    engine.runAndWait()
    pygame.mixer.music.load("response.wav")
    pygame.mixer.music.play(0)


def get_results(prompt=None):
    if prompt is None:
        prompt = (
            next(
                (
                    message["content"]
                    for message in reversed(chat_history)
                    if message["role"] == "user"
                ),
                "",
            )
            + " in another way"
        )

    pygame.mixer.music.pause()
    response_entry.delete("1.0", END)
    response_entry.insert("1.0", "Generating response! Please wait...")
    response = get_completion(prompt)

    chat_history.append({"role": "user", "content": prompt})
    chat_history.append({"role": "assistant", "content": response})

    if lang.get() == "fa-IR":
        response_entry.tag_configure("right", justify="right")
    else:
        response_entry.tag_configure("left", justify="left")

    response_entry.delete("1.0", END)
    response_entry.insert("1.0", response)

    if lang.get() == "en-US":
        text_to_speech(response)

    proccess_btn.config(state="normal")


def process_prompt():
    if proccess_btn["state"] == "disabled":
        return

    prompt = prompt_entry.get(1.0, END)
    prompt = prompt.strip()

    if len(prompt) == 0:
        messagebox.showerror("Invalid Prompt", "Please enter a prompt and try again.")
        return

    proccess_btn.config(state="disabled")
    Thread(target=get_results, args=(prompt,)).start()


def regenerate_prompt():
    Thread(target=get_results).start()


def rec():
    global IS_RECORDING
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    try:
        while IS_RECORDING:
            with mic as source:
                audio = r.listen(mic)
                command = r.recognize_google(audio, language=lang.get()).lower()
                prompt_entry.delete("1.0", END)
                prompt_entry.insert("1.0", command)
                break
    except Exception as e:
        r = sr.Recognizer()
    change_mic_state()


def change_mic_state():
    global IS_RECORDING
    if IS_RECORDING:
        IS_RECORDING = False
        micLabel.config(image=micOff_image)
        micLabel.image = micOff_image
    else:
        IS_RECORDING = True
        micLabel.config(image=micOn_image)
        micLabel.image = micOn_image
        Thread(target=rec).start()


def clear_prompt():
    prompt_entry.delete("1.0", END)


def paste_prompt():
    prompt_entry.delete("1.0", END)
    prompt_entry.insert(END, pyperclip.paste())


def save_response():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text Files", ".txt")]
    )
    if file_path:
        response = response_entry.get("1.0", END)
        with open(file_path, "w") as file:
            file.write(response)
        messagebox.showinfo("Success", "Response saved successfully!")


app = Tk()
app.resizable(0, 0)
app.title("ChatMate AI")
background_color = "#191825"
app.config(bg=background_color)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 657
window_height = 511
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

image = PhotoImage(file="assets/background.png")
background_label = Label(app, image=image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

options = ["en-US", "fa-IR"]
lang = StringVar()
lang.set("en-US")
drop = OptionMenu(
    app,
    lang,
    *options,
)
drop.config(
    width=5,
    background=background_color,
    highlightbackground=background_color,
    highlightcolor=background_color,
    fg="white",
    activebackground=background_color,
    activeforeground="white",
)
drop.place(x=244, y=28)

prompt_entry = Text(
    app, width=36, height=12, bg="#293462", fg="white", font=("Arial", 11)
)
prompt_entry.place(x=25, y=58)

micOn_image = PhotoImage(file="./assets/unmuted.png")
micOff_image = PhotoImage(file="./assets/muted.png")
micLabel = Label(app, image=micOff_image, borderwidth=0, bg=background_color)
micLabel.place(x=109, y=297)
micLabel.bind("<Button-1>", lambda x: change_mic_state())

proccess_img = PhotoImage(file="./assets/process-btn.png")
proccess_btn = Label(app, image=proccess_img, borderwidth=0)
proccess_btn.place(x=23, y=461)
proccess_btn.bind("<Button-1>", lambda x: Thread(target=process_prompt).start())

clear_img = PhotoImage(file="./assets/clear-btn.png")
clear_btn = Label(app, image=clear_img, borderwidth=0)
clear_btn.place(x=124, y=461)
clear_btn.bind("<Button-1>", lambda x: clear_prompt())

paste_img = PhotoImage(file="./assets/paste-btn.png")
paste_btn = Label(app, image=paste_img, borderwidth=0)
paste_btn.place(x=223, y=461)
paste_btn.bind("<Button-1>", lambda x: paste_prompt())

pause_image = PhotoImage(file="./assets/pause.png")
pauseLabel = Label(app, image=pause_image, borderwidth=0, bg=background_color)
pauseLabel.place(x=600, y=21)
pauseLabel.bind("<Button-1>", lambda x: pygame.mixer.music.pause())

response_entry = Text(
    app, width=36, height=22, bg="#293462", fg="white", font=("Arial", 11)
)
response_entry.place(x=342, y=58)

regenerate_img = PhotoImage(file="./assets/regenerate-btn.png")
regenerate_btn = Label(app, image=regenerate_img, borderwidth=0)
regenerate_btn.place(x=342, y=461)
regenerate_btn.bind("<Button-1>", lambda x: regenerate_prompt())

copy_img = PhotoImage(file="./assets/copy-btn.png")
copy_btn = Label(app, image=copy_img, borderwidth=0)
copy_btn.place(x=442, y=461)
copy_btn.bind("<Button-1>", lambda x: pyperclip.copy(response_entry.get("1.0", END)))

save_img = PhotoImage(file="./assets/save-btn.png")
save_btn = Label(app, image=save_img, borderwidth=0)
save_btn.place(x=542, y=461)
save_btn.bind("<Button-1>", lambda x: save_response())

app.mainloop()
