#!/usr/bin/python3

import argparse
import os
from os import access, listdir, path, remove, rename, walk


def removeFiles(directory, argString, verbose=False):
    """ Remove files from the directory that contain the string passed to
     the program. """
    if verbose:
        print('Removing files from ', directory)

    filelist = listdir(directory)
    for file in filelist:
        if(argString in file):
            fullfilepath = path.join(directory, file)
            if(verbose):
                print("Removing ", fullfilepath)

            remove(fullfilepath)


def removeFilesRecursive(directory, argString, verbose=False):
    """ Remove files recursively from the directory that contain the string
     passed to the program recursively. """

    if verbose:
        print('Removing files...')

    for (dirpath, dirname, filenames) in walk(directory):
        for file in filenames:
            if(argString in file):
                fullfilepath = path.join(dirpath, file)

                if verbose:
                    print(fullfilepath)
                # finally, removes
                remove(fullfilepath)


def removeString(directory, argString, verbose=False):
    """ Remove string from the files on the directory passed to
     the program. """
    if verbose:
        print('Removing string from files from ', directory)

    filelist = listdir(directory)
    for file in filelist:
        if(argString in file):
            fullfilepath = path.join(directory, file)
            if(verbose):
                print("Renaming ", fullfilepath)

            newfilename = file.replace(argString, '')
            if newfilename is '':
                newfilename = 'untitled'

            newfullpath = path.join(directory, newfilename)
            rename(fullfilepath, newfullpath)


def removeStringRecursive(directory, argString, verbose=False):
    """ Remove string from the files on the directory passed to
     the program recursively. """
    if verbose:
        print('Removing string from files...')

    for (dirpath, dirname, filenames) in walk(directory):
        for file in filenames:
            # finally, removes string
            if(argString in file):
                fullfilepath = path.join(dirpath, file)

                if(verbose):
                    print("Renaming ", fullfilepath)

                # replaces string for an empty character
                newfilename = file.replace(argString, '')

                # if filename is empty, add 'untitled' to it
                if newfilename is '':
                    newfilename = 'untitled'

                # gets the new full path of the file, and then, renames it
                newfullpath = path.join(dirpath, newfilename)
                rename(fullfilepath, newfullpath)


def replaceString(directory, argString, replaceString, verbose=False):
    """ Replaces a string in the filenames passed as an argument
     to the program. """
    if verbose:
        print('Removing string from files from ', directory)

    filelist = listdir(directory)
    for file in filelist:
        if(argString in file):
            fullfilepath = path.join(directory, file)
            if(verbose):
                print("Renaming ", fullfilepath)

            newfilename = file.replace(argString, replaceString)
            if newfilename is '':
                newfilename = 'untitled'

            newfullpath = path.join(directory, newfilename)
            rename(fullfilepath, newfullpath)


def replaceStringRecursive(directory, argString, replaceString, verbose=False):
    """ Replaces a string in the filenames passed as an argument
     to the program recursively. """
    if verbose:
        print('Replacing string in files...')

    for (dirpath, dirname, filenames) in walk(directory):
        for file in filenames:
            # finally, removes string
            if(argString in file):
                fullfilepath = path.join(dirpath, file)

                if(verbose):
                    print("Renaming ", fullfilepath)

                # replaces string for an empty character
                newfilename = file.replace(argString, replaceString)

                # if filename is empty, add 'untitled' to it
                if newfilename is '':
                    newfilename = 'untitled'

                # gets the new full path of the file, and then, renames it
                newfullpath = path.join(dirpath, newfilename)
                rename(fullfilepath, newfullpath)


def main():
    """ Main function, used to parse arguments and execute actions """

    parser = argparse.ArgumentParser(description='Renames or removes files' +
                                     ' by searching for bits of strings.')

    # main arguments
    parser.add_argument('directory', metavar='dir',
                        help='Directory to search for files.')

    # optional arguments
    parser.add_argument('-R', '--recursive', action='store_true',
                        dest='recursive',
                        help='Operates recursively into the directory tree.')
    parser.add_argument('-F', '--folder', action='store_true',
                        dest='folder',
                        help='Operates on folders as well.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        dest='verbose',
                        help='Verbose mode.')

    # Add mutually exclusive arguments into a group
    argGroup = parser.add_mutually_exclusive_group()
    argGroup.required = True
    argGroup.add_argument('-rm', '--removefile', dest='rmfile', nargs=1,
                          metavar='string',
                          help='Removes a file based on a string search.',)
    argGroup.add_argument('-rs', '--removestring', dest='rmstr', nargs=1,
                          metavar='string',
                          help='Removes a string from the filename based on ' +
                          'a string search')
    argGroup.add_argument('-rp', '--replacestring', dest='rpstr', nargs=2,
                          metavar='string',
                          help='Replaces a string in the filename based on ' +
                          'a string search')

    # parses arguments from cli
    args = parser.parse_args()

    # gets full path to the directory
    absdir = path.abspath(args.directory)
    if not access(absdir, os.W_OK):
        print('Error, unable to access directory "{0}" for writing.'
              .format(absdir), 'Try running as an administrator.')
        exit()

    # executes actions for each option
    if(args.rmfile is not None):
        if (args.recursive is True):
            removeFilesRecursive(absdir, args.rmfile[0], args.verbose)
        else:
            removeFiles(absdir, args.rmfile[0], args.verbose)
    elif(args.rmstr is not None):
        if(args.recursive is True):
            removeStringRecursive(absdir, args.rmstr[0], args.verbose)
        else:
            removeString(absdir, args.rmstr[0], args.verbose)
    elif(args.rpstr is not None):
        if(args.recursive is True):
            replaceStringRecursive(absdir, args.rpstr[0], args.rpstr[1],
                                   args.verbose)
        else:
            replaceString(absdir, args.rpstr[0], args.rpstr[1], args.verbose)


# runs main program
main()
