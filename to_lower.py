input_string = input("Input string:")
lower = ["and", "or", "of", "to"]
output = []
for w in input_string.split():
    w = w.lower()
    if w in lower:
        output.append(w.lower())
    else:
        output.append(w[0].upper() + w[1:].lower())
    
output_string = ""
for i in output:
    output_string += i + " "

print(output_string)