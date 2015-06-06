import os
import string
import argparse


def char_in_filename(c, filename):
    # this checks to see if a character is in a filename but not the file
    # extension. file extension is are the characters after the last period in
    # the filename
    for s in filename.split('.')[:-1]:
        if c in s:
            return True
    return False

def rename_files(args):
    if len(args) == 2:
        target, replacement = args
        if len(target) > 1 or len(replacement) > 1:
            print 'Each argument must be one character long'
            return

    for root, subdirs, files in os.walk('.'):
        for f in files:
            if char_in_filename(target, f):
                cur = os.path.join(root, f)
                new = os.path.join(root, string.replace(f, target, replacement))
                print "Replacing '{}' with '{}'".format(cur, new)
                os.rename(cur, new)

def rename_folders(args):
    if len(args) == 2:
        target, replacement = args
        if len(target) > 1 or len(replacement) > 1:
            print 'Each argument must be one character long'
            return
    for root, subdirs, files in os.walk('.', topdown=False):
        for sb in subdirs:
            if target in sb:
                cur = os.path.join(root, sb)
                new = os.path.join(root, string.replace(sb, target,
                    replacement))
                print "Replacing '{}' with '{}'".format(cur, new)
                os.renames(cur, new)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename files or folders.')
    help_text = "type the target character followed by the replacement character"
    parser.add_argument('--files', nargs=2, help=help_text)
    parser.add_argument('--folders', nargs=2, help=help_text)
    args = parser.parse_args()

    if args.files:
        rename_files(args.files)
    if args.folders:
        rename_folders(args.folders)
