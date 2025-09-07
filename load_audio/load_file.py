import logging
class LoadFileAudio:
    def __init__(self,reference):
        self.file = None
        self.reference = reference

    def load_file(self):
        self.file = open(self.reference, 'r')
        logging.info('the file has been loaded')
        print('the file has been loaded')
        return self.file

    def get_file(self):
        return self.file
    def get_reference(self):
        return self.reference


# load = LoadFileAudio("C:\hostile audio files\podcasts\download (1).wav")
# load.load_file()
