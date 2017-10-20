import parser

def main():
    com = parser.Comment()
    com.read(" * @brief Enum to specify additional format information for scan.")
    print(com)
    print(com.data["brief"])
    pass


if __name__ == "__main__":
    main()
