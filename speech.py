import speech_recognition as speech_rog

def speech_it():
    mic = speech_rog.Microphone()
    recog = speech_rog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="it-IT")