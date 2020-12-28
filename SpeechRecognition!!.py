import speech_recognition as sr

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Now')
    audio=r3.listen(source)
    
if 'yes'in r1.recognize_google(audio):
    r1=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speech to Text!!')
        audio=r1.listen(source)
        
        try:
            get=r1.recognize_google(audio)
            print(get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))