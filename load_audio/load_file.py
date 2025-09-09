from logger import Logger


class LoadFileAudio:
    def __init__(self,reference):
        self.file = None
        self.reference = reference
        self.logger = Logger.get_logger()

    def load_file(self):
        self.file = open(self.reference, 'r')
        self.logger.info('the file has been loaded')
        self.logger.error('the file has not been loaded')
        print('the file has been loaded')
        return self.file

    def get_file(self):
        return self.file
    def get_reference(self):
        return self.reference

#
# load = LoadFileAudio("C:\hostile audio files\podcasts\download (1).wav")
# load.load_file()
