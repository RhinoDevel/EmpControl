
import collections
import mt.str
import ec.ui.console.company

def enter_menu(data):
    while True:
        s = ''

        print('*** '+data['title']+' MENU ***')
        for k, v in data['entries'].items():
            print(k+' '+v['title'])
        print('X'+' '+'Exit')

        s = input('Please select'+':'+' ')
        if s=='X':
            break
        if s in data['entries']:
            data['entries'][s]['func']()
        else:
            print('Unknown command.')

def create(data):
    s = ''
    d = {}
    print('*** CREATE '+data['title']+' ****')
    for k, v in data['entries'].items():
        s = input(v+':'+' ')
        if(not mt.str.is_nonwhitespace(s)):
            print('Invalid input, skipping creation..')
            return
        d[k] = s
    data['func'](d)
    print('Entry created.')

def menu():
    enter_menu(
        {
            'title': 'MAIN',
            'entries': collections.OrderedDict([
                ('c',
                {
                    'title': 'Companies',
                    'func': ec.ui.console.company.menu
                })])
        })
