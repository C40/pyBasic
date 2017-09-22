__author__ = 'C40'

import sys


def comments():
    print((">"*10) + " Python Comments: " + ("<"*10) + "\n")
    print(" Use [ # ] for simple comments\n")
    print(" Use [\"\"\"] for multiline comments\n")
    return None


def modules():
    print((">"*10) + " Python Modules: " + ("<"*10) + "\n")
    print(" Use [import] for load modules\n")
    return None


def operators():
    print((">"*10) + " Python Calculator: " + ("<"*10) + "\n")

    print("\n >Simple Sum:\n 1 + 1 = " + str(1+1))
    print("\n >Sum Int with Float:\n 1 + 1.0 = " + str(1+1.0))
    print("\n >Simple Sub:\n 1 - 1 = " + str(1-1))
    print("\n >Simple Multiplication:\n 2 * 2 = " + str(2*2))
    print("\n >Square: \n 2 ** 3 = " + str(2**3))
    print("\n >Simple Division: 17 / 3.0 = " + str(17/3.0))
    print("\n >Discards the fractional part:\n 17 // 3.0 = " + str(17//3.0))
    print("\n >Remainder of division: \n 1 % 1 = " + str(1 % 1))
    print("\n >Round: \n round(20.555) = " + str(round(20.555)))
    return None


def strings():
    print((">"*10) + " Python Strings: " + ("<"*10) + "\n")

    print(" >Concatenate just two string(enclosed by quotes) next each other:\n \"Test\" \"1\" = " + "Test" "1")
    print(" >For Print Raw mode just add [r] before string:\n print(r\"Testing\") " + r"Testing")
    print(" >Use [char]:\n\"Michel\"[0] = " + "Michel"[0])
    print(" >Use [\"start\" : \" to less 1\" ]:\n \"Michel\"[1:5] = " + "Michel"[1:5])
    print(" >Use [\"first\" : \" to less 1\" ]:\n \"Michel\"[:5] = " + "Michel"[:5])
    print(" >Use [\"start\" : \"end\" ]:\n \"Michel\"[3:] = " + "Michel"[3:])
    print(" >Use [\"start\" : \"end\" ] return all:\n \"Michel\"[:] = " + "Michel"[:])
    print(" >Use [len(string)] to return size string:\n len(\"Michel\") = " + str(len("Michel")))

    return None

def charset():
    print(" >Use [u] before string for UNICODE:\n print(u\"Test½\") = " + u"Test½")
    print(" >Use [r] before string for RAW:\n print(r\"Test½\") = " + r"Test½")
    print(" >Use [encode] method and charset to encode a string: u\"äöü\".encode('utf-8') = ")
    print(u"äöü".encode("utf-8"))

    return None

def start():

    print(("|"*10) + " Michel Gutardo Ramos de Lima (C40) " + ("|" * 10) + "\n" + (">" * 10) + " Testing Python 2.7 " +
          ("<" * 10) + "\n")

    print("Choose an option:")
    print("""
    Python Comments  [1]
    Python Operators [2]
    Python Strings   [3]
    Python Unicode   [4]
    Python Modules   [9]""")

    option = int(input("Option:"))

    choose = {1: comments, 2: operators, 3: strings, 4: charset, 9: exit}

    try:
        if option == 9:
            sys.exit(1)
        else:
            choose[option]()
            input()

    except Exception:
        pass

    return option


while start() < 9:
    print("\n"*5)
    start()



