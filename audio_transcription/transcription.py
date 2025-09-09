from pymongo import MongoClient
import speech_recognition as sr

from CRUD_mongo.find_mongodb import GetCollection

mongo = GetCollection()
doc = mongo.get_doc("4745e1a6-94be-5b93-9f92-3f9b066d9945")
binary_audio = doc['binary_data']
# #
# # # שמירה זמנית כקובץ WAV
with open("temp.wav", "wb") as f:
    f.write(binary_audio)
recognizer = sr.Recognizer()

with sr.AudioFile("temp.wav") as source:
    audio_data = recognizer.record(source)  # קורא את כל הקובץ
#
try:
    # שימוש ב-Google Web Speech API
    text = recognizer.recognize_google(audio_data, language="he-IL")
    print("תמלול:", text)

except sr.UnknownValueError:
    print("❌ לא הצלחתי להבין את הדיבור")
except sr.RequestError as e:
    print(f"❌ בעיה עם שירות התמלול: {e}")
