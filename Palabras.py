def count_words(text):
    words = text.split()  # Split the text into words using spaces as separators
    return len(words)

# Request a text string from the user
text = input("Enter a text string: ")

# Count the number of words in the text
word_count = count_words(text)

# Print the result in Spanish
print(f"Número de palabras: {word_count}")
