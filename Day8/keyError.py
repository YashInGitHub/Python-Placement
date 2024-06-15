def access_dictionary_value(dictionary, key):
    try:
        value = dictionary[key]
        print("Value of key: ", key, "is: ", value)
    except:
        print("Error: Key not found !!!")

access_dictionary_value({'a':1, 'b':2, 'c':3}, 'd')