
def open_file(filename):
    '''Opens the given filname and returns its file object, or None if not found'''
    try:
        file_object = open(filename, 'r')
        return file_object
    except FileNotFoundError:
        return None





