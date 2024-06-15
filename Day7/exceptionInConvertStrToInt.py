def convert_to_integer(s):
    try:
        number = int(s)
        print("Integer value: ", number)

    except ValueError:
        print("Error! Invalid integer format !!!")
def main():
    s = input()
    convert_to_integer(s)

if __name__ == "__main__":
    main()