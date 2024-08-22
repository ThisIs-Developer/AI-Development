# Write a Python program to check whether an alphabet is a vowel or consonant.
alpha= input("Enter the character: ")
if alpha.lower() in ('a', 'e', 'i', 'o', 'u'):
  print("Alphabet is Vowel")
elif alpha.upper() in ('A', 'E', 'I', 'O', 'U'):
  print("Alphabet is Vowel")
else:
  print("Alphabet is Consonant")