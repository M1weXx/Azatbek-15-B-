# Задача 1
# import random

# def get_random(languages):
#     random_language = random.choice(languages)

#     with open("random_language.txt", "w") as file:
#         file.write(random_language)

# language_list = ["Python", "Java", "Kotlin", "JavaScript", "C#", "RUBY"]

# get_random(language_list)

# Задача 2
# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum."""
# with open("textwt.txt","w") as filee:
#     filee.write(text)

# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
# has been the industry's standard dummy text ever since the 1500s, when an unknown
# printer took a galley of type and scrambled it to make a type specimen book. It has
# survived not only five centuries, but also the leap into electronic typesetting, remaining
# essentially unchanged. It was popularized in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing
# software like Aldus PageMaker including versions of Lorem Ipsum."""

# file = open("text.txt", "w")
# file.write(text)
# file.close()

# Задача 3
with open("text.txt", "r") as source_file:
    text_content = source_file.read()

with open("wikipedia.txt", "w") as target_file:
    target_file.write(text_content)