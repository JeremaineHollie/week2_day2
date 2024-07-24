# Task 1

# python_reviews = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]

python_reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]


keywords = ["good", "excellent", "bad", "poor", "average"]

for review in python_reviews:
    highlighted_review = review
    for keyword in keywords:
        highlighted_review = highlighted_review.replace(keyword, keyword.upper())
    print(highlighted_review)

# Task 2

positive_count = 0
negative_count = 0

python_positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]

negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

for word in python_positive_words:
    for review in python_reviews:
        if word in review:
            positive_count += 1
            print(positive_count)
for word in negative_words:
    for review in python_reviews:
        if word in review:
            negative_count += 1
            print(negative_count)

# Task 3

first_stringa = python_reviews[0]
first30 = [first_stringa[0:32] + "..."]
print(first30)