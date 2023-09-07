#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    list_dir = dir(hidden_4)
    for x in list_dir:
        if "__" in x:
            continue
        else:
            print(x)
