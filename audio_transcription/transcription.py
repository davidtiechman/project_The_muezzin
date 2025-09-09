from pymongo import MongoClient
import speech_recognition as sr

# חיבור ל-MongoDB
client = MongoClient("localhost:27018/")
db = client['project_IDF']
collection = db["reference"]

# שליפת קובץ שמע לפי ID
doc = collection.find_one({"_id": 1})
binary_audio = doc["audio_data"]

# שמירה זמנית כקובץ WAV
with open("temp.wav", "wb") as f:
    f.write(binary_audio)
recognizer = sr.Recognizer()

with sr.AudioFile("temp.wav") as source:
    audio_data = recognizer.record(source)  # קורא את כל הקובץ

try:
    # שימוש ב-Google Web Speech API
    text = recognizer.recognize_google(audio_data, language="he-IL")
    print("תמלול:", text)

except sr.UnknownValueError:
    print("❌ לא הצלחתי להבין את הדיבור")
except sr.RequestError as e:
    print(f"❌ בעיה עם שירות התמלול: {e}")
