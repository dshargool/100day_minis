from PyDictionary import PyDictionary


def main():
    userInput = ""
    dictionary = PyDictionary
    while userInput != "q":
        print("Enter a word to check:")
        try:
            userInput = str(input())
            if userInput == reverse(userInput) and len(userInput) > 1:
                print("It's a pallindrome!")
            else:
                print("It's not a pallindrome")
            print("Number of vowels: {}".format(countVowels(userInput)))
            print("Pig Latin Translation: {}".format(pigLatin(userInput)))
            print("Dictionary Definition: {}".format(
                getDictionaryDef(userInput, dictionary)))
        except Exception as err:
            print(err)
            print("Please enter an string!")


def reverse(revString):
    # This uses a slice.  array[start:stop:step] If not specified it is all elements.  -1 for reverse steps.
    return revString[::-1]


def countVowels(vowString):
    vowels = "aeiou"
    count = 0
    for letters in vowString:
        if letters in vowels:
            count += 1
    return count


def pigLatin(inString):
    if len(inString) > 2 and countVowels(inString[0]) == 0:
        pigString = inString[1:] + inString[:1] + 'ay'
    else:
        pigString = inString + 'yay'
    return pigString


def getDictionaryDef(inString, dictionary):
    return dictionary.meaning(inString)


if __name__ == "__main__":
    main()
