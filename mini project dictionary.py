dictionary={}
while True:
    print("\n dictionary management system") 
    print("1. add word")
    print("2. search the meaning")
    print("3. display all words")
    print("4 delete word")
    print("5. exit")
    choice = int(input("Enter your choice: "))
    if choice == "1":
        word=input("enter the word: ")
        meaning=input("enter the meaning:")
        dictionary[word]=meaning
        print("word added successfully")
    elif choice == "2":
        word=input("enter the search for meaning:")
        if word in dictionary:
            print("meaning of the word is:",dictionary[word])
        else:
            print("word not found")
    elif choice == "3":
        print("all words in the dictionary:")
        for word, meaning in dictionary.items():
            print(f"{word}: {meaning}")
        else:
             print("dictionary is empty")
    elif choice == "4":
                   word=input("enter the word to update:")
                   if word in dictionary:
                        meaning=input("enter the new meaning:")
                        dictionary[word]=meaning
                        print("word updated successfully")
                   else:
                     print("word not found")
    elif choice == "5":
        word=input("enter the word to delete:")
        if word in dictionary:
            del dictionary[word]
            print("word deleted successfully")
        else:
            print("word not found")
    elif choice == "6":
        print("exiting the program")
        break