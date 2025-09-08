import uuid

from logger import Logger

logger = Logger.get_logger()
def unique_a_id(str_name):
    unique_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(str_name)))
    logger.info('create unique id')
    logger.error('not cant create unique id')

    return unique_id