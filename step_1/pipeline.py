from pathlib import Path
from load_audio.given_metadata import GetMetadata
from publicher_to_kafka.publicher_to_kafka import PublicherToKafka


def run():
    folder_path = Path("C:\hostile audio files\podcasts")
    for file in folder_path.iterdir():
        get = GetMetadata(file)
        meta = get.get_metadata()
        print(meta)
        kaf = PublicherToKafka()
        kaf.publishing_to_kafka(kaf.TOPIC,meta)


run()