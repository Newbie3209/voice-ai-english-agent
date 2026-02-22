import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import ollama
import pyttsx3

print("Loading Whisper model...")
model = whisper.load_model("base")

def record_audio(filename="input.wav", duration=3, fs=16000):
    print("\nSpeak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("Recording complete.")

def speech_to_text():
    print("Transcribing...")
    result = model.transcribe("input.wav")
    return result["text"]

def get_ai_response(user_text):
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": "You are a friendly English conversation partner."},
            {"role": "user", "content": user_text}
        ]
    )
    return response["message"]["content"]

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def run_agent():
    print("\nVoice AI Agent Started. Press Ctrl+C to stop.\n")

    while True:
        record_audio()
        user_text = speech_to_text()

        if user_text.strip() == "":
            print("Didn't catch that. Try again.")
            continue

        print("\nYou:", user_text)

        reply = get_ai_response(user_text)

        print("\nAI:", reply)

        speak(reply)

run_agent()