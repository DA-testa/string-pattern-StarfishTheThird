class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0 
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

        self.window_start = 0
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabin_karp(word, text):
    if word == "" or text == "":
        return []

    matches = []
    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                matches.append(i)
        rolling_hash.move_window()

    return matches

choice, pattern, text = input().split()

if choice == "I":
    pass
elif choice == "F":
    with open("test.txt", "r") as f:
        lines = f.readlines()
        pattern, text = lines[0].strip(), lines[1].strip()

result = rabin_karp(pattern, text)

if result:
    print(*result)
else:
    print("Pattern not found in the text")

