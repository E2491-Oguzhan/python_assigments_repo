sentence = input('Enter a sentence : ')
frequencies = {} 
  
for char in sentence: 
    if char in frequencies: 
        frequencies[char] += 1
    else: 
        frequencies[char] = 1
        
print (f"Per char frequency in '{sentence}' is :\n{frequencies}")
