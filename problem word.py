word = "Establish"
chunk_size = 3
chunks = [word[i:i+chunk_size] for i in range(0, len(word), chunk_size)]
print(chunks)

