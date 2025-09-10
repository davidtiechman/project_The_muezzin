from logger import Logger
logger = Logger.get_logger()
def clean_list_word(text):
    try:
        list_words = [t.strip().lower() for t in text.split(",")]
        logger.info('cleaning list words:')
        return list_words
    except:
        logger.error('not can cleaning list words')


