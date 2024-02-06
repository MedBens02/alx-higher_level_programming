#!/usr/bin/python3
'''Defines MyInt class inherits from int.'''


class MyInt(int):
    '''Inverts the role of == and !=.'''

    def __eq__(self, compare):
        '''Switch result to !='''
        return int(self) != compare

    def __ne__(self, compare):
        '''Switch result to =='''
        return int(self) == compare
