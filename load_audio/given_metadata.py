import os
from logger import Logger
from pathlib import Path
from datetime import datetime
import json

from load_audio.file_audio import FileAudio
class GetMetadata:
    def __init__(self,reference):
        self.reference = reference
        self.created = None
        self.size = None
        self.name_file = None
        self.logger = Logger.get_logger()
    def get_metadata(self):
        try:
            self.created = Path(self.reference).stat().st_ctime
            self.logger.info('find the date with created = {}'.format(self.created))
        except:
            self.logger.error('not can find the date with created')
        try:
            self.created = datetime.fromtimestamp(self.created)
            self.logger.info('swittshing the date to this format = {}'.format(self.created))
        except:
            self.logger.error('not can swithshing the date with this format = {}'.format(self.created))
        try:
            self.size = Path(self.reference).stat().st_size
            self.logger.info('find the size that file'.format(self.size))
        except:
            self.logger.error('not can find the size that file')
        try:
            self.name_file = Path(self.reference).name
            self.logger.info('find the name file')
        except:
            self.logger.error('not can find the name file')
        file = FileAudio(self.reference,self.created,self.size,self.name_file)
        file = file.get_in_dict()
        return file





# get = GetMetadata("C:\hostile audio files\podcasts\download (1).wav")
# meta = get.get_metadata()





