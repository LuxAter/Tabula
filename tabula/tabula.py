import sys
import clang.cindex


def main():
    sys.path.append('/usr/lib/llvm-4.0/lib/libclang-4.0.0.so')
    index = clang.cindex.Index.create()
    pass


if __name__ == "__main__":
    main()
