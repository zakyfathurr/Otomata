import json

# Open and read the JSON file
with open('./accepted.json', 'r') as file:
    data = json.load(file)  

state_array = []
value = 0
state = data['start_state']
print("Path: ", end="")
print(state, end=" -> ")
for te in data['test_string']:
    state = data['transitions'][state][te]
    if value != len(data['test_string']) - 1:
        print(state, end=" -> ")
    else:
        print(state, end="")
    value += 1

if state in data['accept_states']:
    print("\nStatus: Accepted")
else:
    print("\nStatus: Rejected")

    
            
