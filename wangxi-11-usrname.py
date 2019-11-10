database = [
    ['albert', '1234'],
    ['smith', '2222'],
    ['jones', '3333']
]

username = input('Use name:')
pinnum = input('Pin number:')

if [username, pinnum] in database: print('Access granted')