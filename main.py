import sys
import q1

def main(args):
    qlst = ['q1']
    if not len(args) or args[0] not in qlst:
        print(f'Use one of these arguments: {", ".join(qlst)}')
        exit(0)
    eval(args[0]).main(args[1:])

main(sys.argv[1:])