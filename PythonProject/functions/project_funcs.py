def show_menu():
    print('********************')
    print('1-add')
    print('2-show all')
    print('3-search')
    print('4-update')
    print('5-delete')
    print('6-exit')
    print('********************')



def fake_data(contacts):
    contacts['ali']='0912564873'
    contacts['alireza'] = '0913243876'
    contacts['hamid'] = '0917643974'


def add_new_contact(contacts):
    name=input('contact name?')
    mobile=input('contact mobile?')
    contacts[name]=mobile


def show_all_contacts(contacts):
    for contact in contacts:
        print(contact +'\t'+ contacts.get(contact))


def search_contacts(contacts,name):
    flag=False
    for contact in contacts:
        if contact==name:
            print(contact+'\t'+contacts.get(contact))
            flag=True
            break
    return flag


def update_contact(contacts,name):
    mobile=input('new mobile?')
    flag=False
    for contact in contacts:
        if contact==name:
            contacts[name]=mobile
            flag=True
            break
    return flag


def delete_contact(contacts,name):
    flag=False
    for contact in contacts:
        if contact==name:
            del contacts[name]
            flag=True
            break
    return flag


