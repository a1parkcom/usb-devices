import pyuac

import os


def dc_service(path):
    print(path)


def driver(path):
    print(path)


def install():
    if not pyuac.isUserAdmin():
        print("Do stuff here that requires being run as an admin.")
        input("Press enter to close the window. >")
        exit()

    print('run install')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if input('install Driver?[y/n]') == 'y':
        dc_service(dir_path+'/software/dc_service')

    if input('install DC Service?[y/n]') == 'y':
        print(dir_path+'/software/driver')
