import uuid
def unique_a_id(str_name):
    unique_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(str_name)))
    return unique_id