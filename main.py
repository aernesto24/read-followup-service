authors = 'Stephen King, joe, '

def create_lecture_entry(author_name):
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


def update_author(author_name, updated_author_name):
    global authors
    if author_name in authors:
        authors = authors.replace(author_name + ',', updated_author_name + ',')
    else:
        print("author is not in the list")


def delete_author(author_name):
    global authors 

    if author_name in authors:
        authors = authors.replace(author_name + ',', "")
    else:
        print("CLient is not in client list")


def _print_welcome():
    print("WELCOME TO LECTURE REGISTRY")
    print('*'*50)
    print("What do you want to do today?")


def _get_author_name():
    return str(input("what is the name of the author? "))


if __name__ == '__main__':

    _print_welcome()
    
    lecture_option = int(input("""Select your option:
        1. Add lecture
        2. delete lecture
        3. Update lecture
        : """))

    if lecture_option == 1:
        author_name = _get_author_name()
        create_lecture_entry(author_name)
        list_authors()
    elif lecture_option == 2:
        list_authors()
        author_name = _get_author_name()
        delete_author(author_name)
        list_authors()
    elif lecture_option == 3:
        list_authors()
        author_name = _get_author_name()
        updated_author_name = str(input("what is the updated name of the author? "))
        update_author(author_name, updated_author_name)
        list_authors()
    else:
        print("Nothing else to do")
    