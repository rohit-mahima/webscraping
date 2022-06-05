import argparse

from tomlkit import integer #argument parsing
def get_args():
    parser=argparse.ArgumentParser(
        description='new parser',
        epilog='put example usage'
    )
    #reuired argument
    parser.add_argument('-x','--execute', action='store',required=True,help='help text for option x')

    #optional argument
    parser.add_argument('-y', help='help text for option y', default=False)
    parser.add_argument('-z', help='help text for z', type=integer)
    print(parser.parse_args())

if __name__=='__main__':
    get_args()