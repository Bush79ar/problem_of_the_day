sentence = input("Enter sentence:")

words = sentence.split()
if "CodeAcademy" in words:
    pos = words.index("CodeAcademy")
    print("I found CodeAcademy at",pos+1)

else:
    print("I didnt find CodeAcademy ")
