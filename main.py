writers = 'Stephen King, '

def create_book_entry(writer_name):
    global writers 
    writers += writer_name
    _add_coma()


def _add_coma():
    global writers 
    writers += ','


def list_writers():
    global writers
    print(writers)


if __name__ == '__main__':
    list_writers()
    
    create_book_entry('Joe Hill')

    list_writers()