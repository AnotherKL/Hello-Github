#! python3
# -*- coding: utf-8-*-
# A simple password manager
# TODO: 1. make it more safe

import optparse
import pyperclip

ACCOUNTS = {
    'email-126':'akldsjflksjg24e23wj',
    'blog-csdn':'das87f6789sdfs'
}

def search_pw(uname):
    if (uname in ACCOUNTS):
        pyperclip.copy(ACCOUNTS[uname])
        print('%s\'s pw has been copied to the clipboard successfully.' % uname)
        return 0
    else:
        if_addAccount(uname)

def if_addAccount(uname):
        print('Pw for %s hasn\'t been stored.' % uname)
        print('Would you like to add this account(%s) ?' % uname)
        if_add = input('Type y for yes or n for no:').lower()
        if (if_add == 'y'):
            pw = input('Please enter pw: ')
            ACCOUNTS[uname] = pw
            print('%s\'s pw has been storged successfully.' % uname)
            return 0
        else:
            print('Bye!')
            return 0

def main():
    parser = optparse.OptionParser("usage%prog " +\
    "-u <username>")
    parser.add_option('-u', dest='uname', type='string',\
    help='specify user account')
    (options, args) = parser.parse_args()
    if (options.uname == None):
        print(parser.usage)
        exit(0)
    else:
        uname = options.uname
    search_pw(uname)


if __name__ == '__main__':
    main()
