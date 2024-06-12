import sys
import subprocess

def main(argv = sys.argv):
    args = [
        sys.executable
    ] + sys.argv[1:]

    print(args)

if __name__ == "__main__":
    main()