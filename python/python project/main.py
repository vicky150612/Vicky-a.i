from datetime import datetime
import pyttsx3
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
count = 0


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


name = speak('your name '), input('your name ? ')
while count < 3:
    count = count + 1
    print('            ')
    command = input("what's your command ? ")
    now = datetime.today()

    def query():
        if command == 'time':
            speak('time is')
            print(now)
        elif command == 'my self':
            speak(f'your name is {name}')
            speak(f'{name} is so smart ')
        elif command == 'name':
            speak(name)
        elif command == 'search':
            ans = input('what do you want to search ? ')
            result = kit.search(ans)
            print(result), speak(result)
        elif command == 'youtube':
            video = input('which video ')
            kit.playonyt(video)
        elif command == 'google':
            search = input('which website ? ')
            kit.search(search)
        elif command == 'whatsapp':
            num = input('number of the person ')
            msg = input('type your message ')
            time_hor = int(input('type the hour of the message (in 24 ) : '))
            time_min = int(input('type the min of the message at which you want to send : '))
            kit.sendwhatmsg(num, msg, time_hor, time_min)
        elif command == 'day':
            c = int(input('year :'))
            d = int(input('month :'))
            f = int(input('date :'))
            given_date = datetime(c, d, f)
            print(given_date.strftime('%A'))
        else:
            speak('provide correct input ')
            print('provide correct input ')
    if __name__ == '__main__':
        query()
