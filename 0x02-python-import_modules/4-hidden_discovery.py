#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4 as H

    modules = dir(H)

    for module in modules:
        print("{}".format(module)) if module[:1] != "_" else None
