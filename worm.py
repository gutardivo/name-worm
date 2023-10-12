import time

phrase = input("Phrase: ")

phrase_list = [k for k in phrase]

while True:
    for i in range(len(phrase)):
        time.sleep(1)
        phrase_wormed = phrase[0:i] + "\033[91m" + phrase_list[i].capitalize() + "\033[0m" + phrase[i+1:]
        print(phrase_wormed, end='\r')