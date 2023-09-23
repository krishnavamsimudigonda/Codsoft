from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Durgesh',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
    'In which language you talk?',
    ' I mostly talk in english'
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = tkinter.Tk()

main.geometry("500x650")

main.title("My Chat bot")
img = tkinter.PhotoImage(file="bot1.png")

photoL = tkinter.Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, tkinter.END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(tkinter.END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(tkinter.END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, tkinter.END)
    msgs.yview(tkinter.END)


frame = tkinter.Frame(main)

sc = tkinter.Scrollbar(frame)
msgs = tkinter.Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)

msgs.pack(side=tkinter.LEFT, fill=tkinter.BOTH, pady=10)

frame.pack()

# creating text field

textF = tkinter.Entry(main, font=("Verdana", 20))
textF.pack(fill=tkinter.X, pady=10)

btn = tkinter.Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()