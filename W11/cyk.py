import json

def load_grammar(json_path):
    with open(json_path, 'r') as file:
        grammar = json.load(file)

    reverse_grammar = {}
    for lhs, rhs_list in grammar.items():
        for rhs in rhs_list:
            key = tuple(rhs)
            if key not in reverse_grammar:
                reverse_grammar[key] = []
            reverse_grammar[key].append(lhs)
    return reverse_grammar

def cyk_parse(grammar, input_string):
    tokens = input_string.strip().split()
    n = len(tokens)
    if n == 0:
        return False, [], tokens

    table = [[set() for _ in range(n)] for _ in range(n)]

    for i, word in enumerate(tokens):
        key = (word,)
        if key in grammar:
            table[i][i].update(grammar[key])

    for l in range(2, n + 1): 
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                for B in table[i][k]:
                    for C in table[k + 1][j]:
                        key = (B, C)
                        if key in grammar:
                            table[i][j].update(grammar[key])

    accepted = 'S' in table[0][n - 1]
    return accepted, table, tokens

def display_table(table, tokens):
    print("\nCYK Table:")
    n = len(tokens)
    for row in range(n):
        for col in range(n):
            if col < row:
                print("".ljust(15), end="")
            else:
                cell = table[row][col]
                content = str(cell) if cell else "{}"
                print(content.ljust(15), end="")
        print()

def main():
    grammar_file = 'grammar.json'
    grammar = load_grammar(grammar_file)

    while True:
        input_string = input("\nEnter a space-separated string to parse (or type 'exit' to quit): ")
        if input_string.lower() == 'exit':
            break

        accepted, table, tokens = cyk_parse(grammar, input_string)
        print("Accepted by grammar?", "✅ Yes" if accepted else "❌ No")
        display_table(table, tokens)

if __name__ == "__main__":
    main()
