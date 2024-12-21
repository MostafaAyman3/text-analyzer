class TopDownParser:
    def __init__(self):
        self.grammar = {}
        self.simple = False

    def input_grammar(self):
        """ Input the grammar rules for exactly 2 non-terminals with 4 rules """
        self.grammar = {}
        print("\n👇 Grammars 👇")
        non_terminals = ['S', 'B']  # Fixed non-terminals: S and B
        for nt in non_terminals:
            rules = []
            print(f"For non-terminal '{nt}':")
            for i in range(2):  # Each non-terminal must have exactly 2 rules
                rule = input(f"Enter rule {i + 1} for '{nt}': ").strip()
                rules.append(rule)
            self.grammar[nt] = rules

    def is_simple(self):
        """ Check if the grammar is simple and disjoint """
        # Check for left recursion (simple grammar condition)
        for nt, rules in self.grammar.items():
            for rule in rules:
                if len(rule) > 1 and rule[0] in self.grammar:
                    return False

        # Check for disjoint rules (no overlapping starts)
        for nt, rules in self.grammar.items():
            starts = set()
            for rule in rules:
                if rule[0] in starts:  # If a start symbol is repeated, grammar is not disjoint
                    return False
                starts.add(rule[0])
        return True

    def check_string(self, sequence, start_symbol):
        """ Validate a string based on the grammar rules """
        def parse(symbol, index):
            if index == len(sequence):
                return []

            if symbol not in self.grammar:  # Terminal symbol
                return [index + 1] if index < len(sequence) and sequence[index] == symbol else []

            results = []
            for rule in self.grammar[symbol]:
                temp = [index]
                for r in rule:
                    new_temp = []
                    for pos in temp:
                        new_temp.extend(parse(r, pos))
                    temp = new_temp
                results.extend(temp)

            return results

        result = parse(start_symbol, 0)
        return len(sequence) in result

    def run(self):
        """ Infinite loop for user interaction """
        while True:
            self.input_grammar()

            # Check if grammar is simple and disjoint
            self.simple = self.is_simple()
            if not self.simple:
                print("The Grammar isn't simple or disjoint.\nTry again.")
                continue

            print("\nThe Grammar is Simple and Disjoint ✅")
            while True:
                print("\n==========================================")
                print("1 - Enter Another Grammar")
                print("2 - Check a String")
                print("3 - Exit")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    break
                elif choice == 2:
                    sequence = list(input("Enter the string to be checked: ").strip())
                    start_symbol = 'S'  # Always start with 'S'
                    if self.check_string(sequence, start_symbol):
                        print("Your input String is Accepted.")
                    else:
                        print("Your input String is Rejected.")
                elif choice == 3:
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice. Try again!")


if __name__ == "__main__":
    parser = TopDownParser()
    parser.run()
