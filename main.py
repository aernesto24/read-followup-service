authors = 'Stephen King, '

def create_lecture_entry(authors_name):
    global authors
    if author_name not in authors:
        authors += author_name
        _add_coma()
    else:
        print("This author is already in the authors list")


def _add_coma():
    global authors 
    authors += ','


def list_authors():
    global authors
    print(authors)


def _print_welcome():
    print("WELCOME TO LECTURE REGISTRY")
    print('*'*50)
    print("What do you want to do today?")


if __name__ == '__main__':

    _print_welcome()
    
    lecture_option = int(input("""Select your option:
        1. Add lecture
        2. delete lecture
        : """))

    if lecture_option == 1:
        author_name = str(input("what is the name of the author? "))
        create_lecture_entry(author_name)
        list_authors()
    elif lecture_option == 2:
        print("Print option WIP")
    else:
        print("Nothing else to do")
    