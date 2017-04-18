import argparse
from os import listdir, path, walk, remove, rename


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
    print('Removing files...')
    for (dirpath, dirname, filenames) in walk(directory):
        print(filenames)


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
    print('Removing string from files...')
    for (dirpath, dirname, filenames) in walk(directory):
        print(filenames)


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
    print('Renaming files...')
    for (dirpath, dirname, filenames) in walk(directory):
        print(filenames)


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

    args = parser.parse_args()

    absdir = path.abspath(args.directory)
    print(args)

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


main()
