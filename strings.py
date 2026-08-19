"""
You are given a string  sentence . Print the characters at even indices.
"""
# Output: "Pto saaig"
# sentence = "Python is amazing"
# for i in range(0,len(sentence),2):
#     print(sentence[i],end="")

# sentence = "python is amazing"
# # Takes index 1, 3, etc. for each word -> 'pto', 's', 'aaig' -> joined
# output = " ".join([word[0::2] for word in sentence.split()])
# print(output)

"""
You are given a string  s . Replace all spaces in the string with underscores ( _ ) 
and print the modified string.
"""
# s = "Python is fun and powerful"
# # Output: "Python_is_fun_and_powerful"
# str=s.replace(" ","_")
# print(str)

"""
You are given a string  s . Check if the string contains only digits
"""
# s = "1235"

# print(s.isnumeric())

# print(s.isdigit())

"""
You are given a string  s . Print the string in reverse order
"""

s = "Python is amazing"
# # Output: "gnizama si nohtyP"
# str="".join(reversed(s))
# print(str)

# str=s[::-1]
# print(str)

"""
You are given a string  s . Capitalize the first letter of each word in the string 
and print the modified string.
"""

text = "python programming is fun"
# for word in text.split(" "):
#     capitalized_text = word[0].upper() + word[1:]
#     print(capitalized_text,end=" ")
    
# for word in text.split(" "):
#     capitalized_text = word.capitalize()
#     print(capitalized_text,end=" ")

# print(text.title())