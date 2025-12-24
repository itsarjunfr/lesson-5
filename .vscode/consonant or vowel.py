strs = input('Enter any letter of the alphabet:')
strs = strs.lower()
if strs == 'a' or strs == 'e' or strs == 'i' or strs == 'o' or strs == 'u':
    print(strs, 'is a vowel.')
else:
    print(strs, 'is a consonant.')