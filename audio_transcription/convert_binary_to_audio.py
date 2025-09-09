from logger import Logger

logger = Logger.get_logger()
def convert_binary_to_audio(doc,audio_file):
    try:
        audio_binary = doc["binary_data"]
        with open(audio_file, 'wb') as f:
            logger.info('convert binary file to audio')
            f.write(audio_binary)
        return audio_file
    except:
        logger.error('cannot convert binary file to audio')
        return None


