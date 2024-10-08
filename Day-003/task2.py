Book = {
    "Treasure Island": "Robert Louis Stevenson",
    "Wuthering Height": "Emily Bronte",
    "13 Things Mentally Strong People Don't Do": "Amy Morin",
    "Atomic Habits": "James Clear",
    "Eat That Frog!": "Brian Tracy"
}

for key, value in Book.items():
    print(key, ":", value)


Book["How to Talk to Anyone"] = "Leil Lowndes"

print(Book)