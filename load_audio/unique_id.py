def unique_a_id(metadata):
    unique_id = str(metadata['created'] + metadata['size'])
    return unique_id