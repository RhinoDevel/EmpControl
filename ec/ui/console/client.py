
import collections
import ec.db.client
import ec.ui.console
import mt.help

menu_title = 'CLIENT'

def _print():
    l = ec.db.client.read_all()
    if not l:
        print('No entries.')
        return

    c = ec.db.company.read_all()

    print('ID      ' + ' | ' + 'Company ID' + ' | ' + 'Company Title' + ', ' + 'Lastname' + ', ' + 'Firstname')
    print('--------' + '---' + '----------' + '---')
    for v in l:
        i = mt.help.get_first_dict_index(c, 'id', v['company_id'])

        print(v['id'], end=' | ')
        print(v['company_id'], end='   | ')
        print(c[i]['title'], end=', ')
        print(v['lastname'], end=', ')
        print(v['firstname'])

def _create():
    ec.ui.console.create(
        {
            'title': menu_title,
            'entries': collections.OrderedDict([
                ('company_id', 'Company ID'),
                ('lastname', 'Lastname'),
                ('firstname', 'Firstname')]),
            'func': ec.db.client.create
        })

def _modify():
    ec.ui.console.modify(
        {
            'title': menu_title,
            'entries': collections.OrderedDict([
                ('company_id', 'Company ID'),
                ('lastname', 'Lastname'),
                ('firstname', 'Firstname')]),
            'read': ec.db.client.read_by_id,
            'modify': ec.db.client.update_by_id
        })

def _delete():
    ec.ui.console.delete(
        {
            'title': menu_title,
            'func': ec.db.client.delete_by_id
        })

def menu():
    ec.ui.console.enter_menu(
        {
            'title': menu_title,
            'entries': collections.OrderedDict([
                ('p',
                {
                    'title': 'Print',
                    'func': _print
                }),
                ('c',
                {
                    'title': 'Create',
                    'func': _create
                }),
                ('m',
                {
                    'title': 'Modify',
                    'func': _modify
                }),
                ('d',
                {
                    'title': 'Delete',
                    'func': _delete
                })])
        })
