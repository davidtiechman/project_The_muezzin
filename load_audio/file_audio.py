class FileAudio:
    def __init__(self,reference,created,size,name_file):
        self.reference = reference
        self.created = created
        self.size = size
        self.name_file = name_file
    def get_in_dict(self):
        arr_fild = {
            'reference': str(self.reference),
            'created':str(self.created),
            'size': str(self.size),
            'name_file':str(self.name_file)
        }
        return arr_fild
