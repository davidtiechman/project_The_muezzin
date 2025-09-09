from logger import Logger

import speech_recognition as sr
# Initialize the recognizer
recognizer = sr.Recognizer()
class Transcription:
    def __init__(self,audio_file):
        self.audio_file = audio_file
        self.logger = Logger.get_logger()
# Path to your audio file
    def transcribe(self):
        try:
            # Load the audio file
            with sr.AudioFile(self.audio_file) as source:
                self.logger.info("Processing audio...")
                audio_data_file = recognizer.record(source)  # Read the entire audio file


            # Recognize speech using Google's Web Speech API
            text = recognizer.recognize_google(audio_data_file)

            return text

        except sr.UnknownValueError:
            self.logger.error("Sorry, the audio could not be understood.")
        except sr.RequestError as e:
            self.logger.error("Could not request results;")
        except FileNotFoundError:
            self.logger.error("Audio file could not be found.")
            return None

