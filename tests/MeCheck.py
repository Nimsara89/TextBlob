from textblob import TextBlob

# Get user input
text = input("Enter the text you want to correct: ")

# Create a TextBlob object with the input text
blob = TextBlob(text)

# Perform spelling correction
corrected_text = blob.correct()

# Display the original and corrected text with newlines
print("\nOriginal Text:\n", text)
print("\nCorrected Text:\n", corrected_text)

