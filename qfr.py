import argparse
from os import listdir, path, walk


def removeFiles(directory, argString):
    """ Remove files from the directory that contain the string passed to
     the program. """
    print('Removing files...')
    print(listdir(directory))


def removeFilesRecursive(directory, argString):
    """ Remove files recursively from the directory that contain the string
     passed to the program recursively. """
    print('Removing files...')
    for (dirpath, dirname, filenames) in walk(directory):
        print(filenames)


def removeString(directory, argString):
    """ Remove string from the files on the directory passed to
     the program. """
    print('Removing string from files...')
    print(listdir(directory))


def removeStringRecursive(directory, argString):
    """ Remove string from the files on the directory passed to
     the program recursively. """
    print('Removing string from files...')
    for (dirpath, dirname, filenames) in walk(directory):
        print(filenames)


def replaceString(directory, argString):
    """ Replaces a string in the filenames passed as an argument
     to the program. """
    print('Renaming files...')
    print(listdir(directory))


def replaceStringRecursive(directory, argString):
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
    argGroup.add_argument('-rp', '--replacestring', dest='rpstr', nargs=1,
                          metavar='string',
                          help='Replaces a string in the filename based on ' +
                          'a string search')

    args = parser.parse_args()

    absdir = path.abspath(args.directory)

    if(args.rmfile is True):
        if (args.recursive is True):
            removeFilesRecursive(absdir, args.searchstr)
        else:
            removeFiles(absdir, args.searchstr)
    elif(args.rmstr is True):
        if(args.recursive is True):
            removeStringRecursive(absdir, args.searchstr)
        else:
            removeString(absdir, args.searchstr)
    elif(args.rpstr is True):
        if(args.recursive is True):
            replaceStringRecursive(absdir, args.searchstr)
        else:
            replaceString(absdir, args.searchstr)


main()
