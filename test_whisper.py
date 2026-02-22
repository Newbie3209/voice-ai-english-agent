import sounddevice as sd
from scipy.io.wavfile import write
import whisper

# record audio
fs = 16000
duration = 5

print("Speak now...")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
write("input.wav", fs, audio)
print("Recording saved")

# LOAD WHISPER MODEL (this line was missing)
model = whisper.load_model("base")

print("\nTranscribing...")

result = model.transcribe("input.wav")

print("\nRAW RESULT:")
print(result)

print("\nYou said:", result["text"])