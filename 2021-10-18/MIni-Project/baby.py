import sys

list_sentence = []
if (len(sys.argv) <= 1):
    print(f"Usage: python {sys.argv[0]} filename")
    exit(1)
with open(sys.argv[1], "r") as file:
    for line in file:
        list_sentence.append(line)
    result = sorted(list_sentence, key=lambda string1: len(string1))
    '''print(result)'''
    n = len(result)

    print(f"Shortest line {result[0]}  of lenght: {len(result[0])}")
    print(f"Longest line {result[n - 1]}  of lenght: {len(result[n - 1])}")
