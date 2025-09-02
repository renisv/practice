sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ' '.join(words[::-1])
print(f"Reversed sentence:{reversed_sentence}")