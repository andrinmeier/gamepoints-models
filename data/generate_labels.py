numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
types = ["Red_Heart", "Red_Diamond", "Black_Club", "Black_Spade"]
labels = []
for number in numbers:
    for type in types:
        labels.append(f"{type}_{number}")
labels.append("Joker")
labels.sort()
print(labels)
with open("labels.txt", "w") as labels_file:
    for label in labels:
        labels_file.write(f"{label}\n")

