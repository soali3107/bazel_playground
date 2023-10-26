import sys
import subprocess

def main(argv = sys.argv):
    args = [
        sys.executable
    ] + sys.argv[1:]

    exit(subprocess.call(args))

if __name__ == "__main__":
    main()