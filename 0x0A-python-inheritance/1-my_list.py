#!/usr/bin/python3
'''Defines MyList class.'''


class MyList(list):
    '''Custom class.'''
    def print_sorted(self):
        '''Method prints sorted list.'''
        print(sorted(self))
