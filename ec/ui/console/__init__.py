
import collections
import mt.str
import ec.ui.console.company
import ec.ui.console.client
import ec.ui.console.worker
import ec.ui.console.tasktype
import ec.ui.console.workday

def enter_menu(data):
    while True:
        s = ''

        print('*** ' + data['title'] + ' MENU ***')
        for k, v in data['entries'].items():
            print(k + ' ' + v['title'])
        print('X' + ' ' + 'Exit')

        s = input('Please select' + ':' + ' ')
        if s=='X':
            break
        if s in data['entries']:
            data['entries'][s]['func']()
        else:
            print('Unknown command.')

def create(data):
    s = ''
    d = {}

    print('*** CREATE ' + data['title'] + ' ****')
    for k, v in data['entries'].items():
        s = input(v + ':' + ' ')
        if(not mt.str.is_nonwhitespace(s)):
            print('Invalid input, skipping creation..')
            return
        d[k] = s
    data['func'](d)
    print('Entry created.')

def modify(data):
    d = {}
    e = None
    s = ''

    print('*** MODIFY ' + data['title'] + ' ***')

    d['id'] = input('Please enter ID: ')
    if(not mt.str.is_nonwhitespace(d['id'])):
        print('Invalid input, skipping modification..')
        return
    e = data['read'](d['id'])

    for k, v in data['entries'].items():
        s = input(v + ' ["' + e[k] + '"]:' + ' ')
        if(not s):
            s = e[k]
        if(not mt.str.is_nonwhitespace(s)):
            print('Invalid input, skipping modification..')
            return
        d[k] = s

    data['modify'](d)
    print('Entry modified.')

def delete(data):
    s = ''

    print('*** DELETE ' + data['title'] + ' ***')
    s = input('Please enter ID: ')
    if(not mt.str.is_nonwhitespace(s)):
        print('Invalid input, skipping deletion..')
        return
    data['func'](s)
    print('Entry deleted.')

def menu():
    enter_menu(
        {
            'title': 'MAIN',
            'entries': collections.OrderedDict([
                ('c',
                {
                    'title': 'Companies',
                    'func': ec.ui.console.company.menu
                }),
                ('l',
                {
                    'title': 'Clients',
                    'func': ec.ui.console.client.menu
                }),
                ('w',
                {
                    'title': 'Workers',
                    'func': ec.ui.console.worker.menu
                }),
                ('a',
                {
                    'title': 'Task types',
                    'func': ec.ui.console.tasktype.menu
                }),
                ('o',
                {
                    'title': 'Workdays',
                    'func': ec.ui.console.workday.menu
                })])
        })
