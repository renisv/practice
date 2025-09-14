"""phone_book = {}
phone_book.update({"kleoma": 35568})
phone_book.update({"xhonsi": 35567})
phone_book.update({"dumani": 35569})
print(phone_book)
phone_book.update({"dumani": 35566})
print(phone_book)
x = phone_book.get("renis")
if x is None:
    print("friend not found")
else:
    print(x)"""

text = "the quick brown fox jumps over the lazy dog the fox was quick"
words = text.lower().split()
freq_dict = {}
for word in words:
    current_count = freq_dict.get(word, 0)
    freq_dict[word] = current_count + 1
print(freq_dict)

# Exercise 3: Merging Dictionaries

# Given dictionaries
default_settings = {"theme": "light", "language": "en", "notifications": True}
user_settings = {"theme": "dark", "timezone": "EST"}

print("Original Dictionaries:")
print(f"default_settings: {default_settings}")
print(f"user_settings: {user_settings}")

default_settings = {"theme": "light", "language": "en", "notifications": True}
user_settings = {"theme": "dark", "timezone": "EST"}
final_settings = default_settings.copy()

for key, value in user_settings.items():
    final_settings[key] = value

print(final_settings)