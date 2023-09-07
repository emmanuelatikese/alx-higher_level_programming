#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lr = len(argv) - 1
    ar = ''
    count = 1
    if lr == 0:
        ar = "arguments."
    elif lr == 1:
        ar = "argument:"
    else:
        ar = "arguments:"
    print("{} {}".format(lr, ar))

    for x in argv[1:]:
        print("{}: {}".format(count, x))
        count += 1
