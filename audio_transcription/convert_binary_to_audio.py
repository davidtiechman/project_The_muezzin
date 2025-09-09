from logger import Logger

logger = Logger.get_logger()
def convert_binary_to_audio(binary_file):
    with open(binary_file, 'rb') as f:
        audio_file = f.read()
    return audio_file
