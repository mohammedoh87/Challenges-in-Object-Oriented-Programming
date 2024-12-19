class flashcards:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + "(" +  self.meaning + ")"

flash = []
print("Welcome to the flashcards application")

while True:
    word = input("Enter a word:")
    meaning = input("Enter a meaning: ")

    flash.append(flashcards(word, meaning))
    option = int(input("Enter 0 to continue or 1 to exit "))
    if option:
        break
print("Your flashcards")
for i in flash:
    print(i)