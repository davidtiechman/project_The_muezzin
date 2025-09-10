from logger import Logger

logger = Logger.get_logger()
def process_text(text):
    try:
        list_words = [word.lower() for word in text.split(' ')]
        logger.info('Divide the text into a list of words and convert to lowercase.')
    except:
        logger.error('not can convert text into lowercase')
        return None