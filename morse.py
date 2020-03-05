def toMorse(inputString):
    outputString = ""
    alphabetEnglish = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    alphabetMorse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "/"]
    for i in inputString.lower():
        for idx, j in enumerate(alphabetEnglish):
            if i == j:
                outputString += alphabetMorse[idx] + " "
                break
    return outputString


def fromMorse(inputString):
    outputString = ""
    alphabetEnglish = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    alphabetMorse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "/"]
    for i in slicer(inputString):
        for idx, j in enumerate(alphabetMorse):
            if i == j:
                outputString += alphabetEnglish[idx]
                break
    return outputString


def slicer(inputString):
    sliceBegin = 0
    sliceEnd = 0
    ouputArray = []
    inputString += " "
    # Loop through given string searching for spaces
    # If a space is reached, the previous segment is added to the output array.
    for idx, i in enumerate(inputString):
        if i == " ":
            segment = ""
            sliceBegin = sliceEnd
            sliceEnd = idx
            for i in range(sliceEnd - sliceBegin):
                segment += inputString[sliceBegin + i]
            # Some, but not all slices will contain spaces, this is to solve that issue:
            segment = segment.replace(" ", "")
            ouputArray.append(segment)
    return ouputArray


print(toMorse("here is a sentence in morse code"))
print(fromMorse(".... . .-. . / .. ... / .- / ... . -. - . -. -.-. . / .. -. / -- --- .-. ... . / -.-. --- -.. . "))