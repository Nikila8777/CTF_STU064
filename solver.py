import pandas as pd
import hashlib

# Load datasets
books = pd.read_csv("data/books.csv")
reviews = pd.read_csv("data/reviews.csv")

# ---------- FLAG 2 ----------
STUDENT_ID = "STU064"
HASH = hashlib.sha256(STUDENT_ID.encode()).hexdigest()[:8].upper()
print("Computed FLAG2:", HASH)

fake_review = reviews[reviews["text"].str.contains(HASH, na=False, case=False)]
print("\nFake Review Located:\n", fake_review[["asin", "parent_asin", "text"]])

# ---------- FLAG 1 ----------
asin = fake_review.iloc[0]["asin"]
book = books[
    (books["isbn_10"].astype(str) == str(asin)) |
    (books["isbn_13"].astype(str) == str(asin)) |
    (books["parent_asin"].astype(str) == str(asin))
].iloc[0]

title = book["title"]
clean = "".join(title.split())[:8]
FLAG1 = hashlib.sha256(clean.encode()).hexdigest()

print("\nBook Title:", title)
print("Cleaned 8 chars:", clean)
print("FLAG1:", FLAG1)

print("\nPut this in flags.txt:")
print(f"FLAG1{{{FLAG1}}}")
print(f"FLAG2{{{HASH}}}")
