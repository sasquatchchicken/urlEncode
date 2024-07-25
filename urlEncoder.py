import urllib.parse

# Prompt the user to input the string they wish to URL encode
string = input("Enter the string to be URL encoded: ")

# URL encode the string
encoded_string = urllib.parse.quote(string)

print(f"URL encoded string: {encoded_string}")
