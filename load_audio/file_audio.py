class FileAudio:
    def __init__(self,reference,created,size,name_file):
        self.reference = reference
        self.created = created
        self.size = size
        self.name_file = name_file
    def get_in_dict(self):
        arr_fild = {
            'reference': self.reference,
            'created': self.created,
            'size': self.size,
            'name_file': self.name_file
        }
        return arr_fild
