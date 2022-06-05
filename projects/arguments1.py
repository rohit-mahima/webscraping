import argparse

def get_parse():
    parser=argparse.ArgumentParser(
        description='this is new parser',
        epilog='this is help'
    )

    group=parser.add_mutually_exclusive_group()

    group.add_argument('-x',action='store',help='this is for storing')
    group.add_argument('-y', type=int, help='integr')
    print(parser.parse_args())

if __name__=='__main__':
    get_parse()