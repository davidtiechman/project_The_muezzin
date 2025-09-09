from pathlib import Path
from load_audio.given_metadata import GetMetadata
from pub_and_sub_to_KAFKA.publicher_to_kafka import PublicherToKafka

# starting step 1
def run():
    folder_path = Path("C:\hostile audio files\podcasts")  # rot directory
    for file in folder_path.iterdir():
        get = GetMetadata(file)
        meta = get.get_metadata()
        kaf = PublicherToKafka()
        kaf.publishing_to_kafka(kaf.TOPIC,meta)


run()