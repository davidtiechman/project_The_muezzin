from logger import Logger

logger = Logger.get_logger()
def convert_binary_to_audio(binary_file,audio_file):
    try:
        with open(audio_file, 'wb') as f:
            logger.info('convert binary file to audio')
            f.write(binary_file)
        return audio_file
    except:
        logger.error('cannot convert binary file to audio')
        return None


