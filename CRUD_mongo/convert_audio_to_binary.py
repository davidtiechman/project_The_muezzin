from logger import Logger
logger = Logger.get_logger()
def convert_audio_to_binary(file):
    with open(file, 'rb') as f:
        binary_data = f.read()
        logger.info('convert audio file to binary file')
        logger.error('not cant convert audio file to binary file')
    return binary_data