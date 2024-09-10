def main():
    book_path = "books/frankenstein.txt"
    book = getBookText(book_path)
    wordCount = getWordCount(book)
    charList = getCharacterCount(book)
    print(f"Begin of report for {book_path}")
    print(f"{wordCount} words found in document")
    for item in charList:
        print(f"'{item["character"]}' was found {item["count"]} times.")

def getWordCount(message):
    return len(message.split())

def getBookText(path):
    with open(path) as f:
        return f.read()

def getCharacterCount(bookText):
    workingSet = bookText.lower()
    charDic = {}
    for character in workingSet:
        if character.isalpha():
            if character not in charDic:
                charDic[character] = 1
            else:
                charDic[character] += 1
    charList = []
    for element in charDic:
        charList.append({"character": element, "count": charDic[element]})
    charList.sort(reverse=True, key=sort_on)
    return charList
def sort_on(dict):
    return dict["count"]

main()


