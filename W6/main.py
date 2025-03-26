import json

# Open and read the JSON file
with open('./data.json', 'r') as file:
    data = json.load(file)  

output_array = []
value = 0
state = data['initial_state']
print("Path: ", end="")
print(state, end=" -> ")
for da in data['input_sequence']:
    output = data['transitions'][state][da]['output']
    state = data['transitions'][state][da]['next_state']
    output_array.append(output)
    if value != len(data['input_sequence']) - 1:
        print(state, end=" -> ")
    else:
        print(state, end="")
    value += 1

print("\nOutput: ", end="")

for out in output_array:
    print(out, end="")

    
            
