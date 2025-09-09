from CRUD_mongo.find_mongodb import GetCollection
from audio_transcription.transcription_audio_to_text import Transcription

mongo = GetCollection()
trna = Transcription()


def run():
    collect = mongo.get_collection()
    for doc in collect:

        # trna.transcribe()


run()