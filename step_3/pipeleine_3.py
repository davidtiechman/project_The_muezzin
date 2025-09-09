from elasticsearch import Elasticsearch

from CRUD_elasticsarch.index_documents import IndexElasticsearch
from CRUD_mongo.find_mongodb import GetCollection
from audio_transcription.convert_binary_to_audio import convert_binary_to_audio
from audio_transcription.transcription_audio_to_text import Transcription

mongo = GetCollection()
trna = Transcription()
el = IndexElasticsearch()


def run():
    collect = mongo.get_collection()
    for doc in collect:
        file_audio = convert_binary_to_audio(doc,f'{doc["unique_id"]}.wav')
        if not file_audio:
            continue
        file_text = trna.transcribe(file_audio)
        el.update_doc(doc["unique_id"],"text_audio",file_text)


# trna.transcribe()


run()