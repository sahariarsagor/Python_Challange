import os

# This line finds the exact folder where main.py is saved
current_folder = os.path.dirname(os.path.abspath(__file__))

# This joins that folder path with the filename 'story.txt'
file_path = os.path.join(current_folder, "story.txt")

try:
    # We use 'file_path' instead of just "story.txt"
    with open(file_path, "r") as my_file:
        content = my_file.read()
        
        # Split text into a list of words
        words = content.split()
        
        # Count the items in the list
        total_words = len(words)
        
        print("-" * 30)
        print(f"File found at: {file_path}")
        print(f"Total Word Count: {total_words}")
        print("-" * 30)

except FileNotFoundError:
    print("-" * 30)
    print("ERROR: Could not find story.txt!")
    print(f"I was looking in: {current_folder}")
    print("Please make sure story.txt is in that exact folder.")
    print("-" * 30)