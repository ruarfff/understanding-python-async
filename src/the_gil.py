import sys


def main():
    a_thing = "a thing"
    print(sys.getrefcount(a_thing))
    another_thing = a_thing
    print(sys.getrefcount(another_thing))
    del a_thing
    print(sys.getrefcount(another_thing))


if __name__ == "__main__":
    main()
