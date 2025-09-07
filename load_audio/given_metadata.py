import os
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
    def get_metadata(self):
        self.created = Path(self.reference).stat().st_ctime
        # self.created = datetime.fromtimestamp(self.created)
        self.size = Path(self.reference).stat().st_size
        name_file = self.reference.split("\\")[-1]
        self.name_file = name_file
        file = FileAudio(self.reference,self.created,self.size,self.name_file)
        file = file.get_in_dict()
        return file





get = GetMetadata("C:\hostile audio files\podcasts\download (1).wav")
meta = get.get_metadata()





