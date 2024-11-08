import re  # Import the regular expressions module for pattern matching

# Define token types with regex patterns
TOKEN_TYPES = {
    'KEYWORD': r'\b(?:int|float|double|char|return|if|else|for|while|namespace|template|include|define)\b',  # Match C++ keywords
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',  # Match identifiers (variable names, function names)
    'PREPROCESSOR': r'#\s*(?:include|define)\b',  # Match preprocessor directives
    'CONSTANT_FLOAT': r'\b\d+\.\d+\b',  # Match floating-point constants
    'CONSTANT_INT': r'\b\d+\b',  # Match integer constants
    'OPERATOR': r'[+\-*/=<>!&|%^~]',  # Match operators
    'PUNCTUATOR': r'[{}();,<>]',  # Match punctuators like braces and parentheses
    'STRING_LITERAL': r'"(?:\\.|[^"\\])*"',  # Match string literals, including escape sequences
    'COMMENT_SINGLE': r'//.*',  # Match single-line comments
    'COMMENT_MULTI': r'/\*[\s\S]*?\*/',  # Match multi-line comments
}

# Lexical analyzer class to tokenize the input code
class Lexer:
    def __init__(self, code):
        self.code = code  # Store the input code
        self.tokens = []  # Initialize an empty list to store tokens

    def tokenize(self):
        # Remove comments first to avoid overlapping patterns
        self.code = re.sub(TOKEN_TYPES['COMMENT_MULTI'], '', self.code)  # Remove multi-line comments
        self.code = re.sub(TOKEN_TYPES['COMMENT_SINGLE'], '', self.code)  # Remove single-line comments

        # Tokenize the code based on regex patterns
        while self.code:  # Continue until there is no more code to process
            self.code = self.code.lstrip()  # Strip leading whitespace from the code
            matched = False  # Flag to check if a match is found
            for token_type, pattern in TOKEN_TYPES.items():  # Iterate through all token types and patterns
                regex = re.compile(pattern)  # Compile the regex pattern for matching
                match = regex.match(self.code)  # Attempt to match the pattern at the start of the code
                if match:  # If a match is found
                    token_value = match.group(0)  # Get the matched token value
                    self.tokens.append((token_type, token_value))  # Append the token type and value to the tokens list
                    self.code = self.code[match.end():]  # Update the code to remove the matched part
                    matched = True  # Set the flag to indicate a match was found
                    break  # Exit the loop since a match was found
            if not matched:  # If no match was found
                if self.code:  # If there is still code remaining
                    print(f"Unrecognized token: {self.code[0]}")  # Print the first character of the unrecognized token
                    self.code = self.code[1:]  # Move to the next character in the code

    def print_tokens(self):
        # Print all the tokens found
        for token_type, token_value in self.tokens:
            print(f"Token Type: {token_type}, Token Value: {token_value}")

# Function to take block input from the user
def get_cpp_code():
    print("Enter your C++ code (end input with 'END'):")  # Prompt user to enter C++ code
    lines = []  # Initialize an empty list to store lines of code
    while True:  # Loop to collect lines of input
        line = input()  # Read a line of input from the user
        if line.strip() == "END":  # Check if the user entered the terminator 'END'
            break  # Exit the loop if 'END' is entered
        lines.append(line)  # Append the line to the list of lines
    return "\n".join(lines)  # Join the lines into a single string separated by newlines

# Example usage
cpp_code = get_cpp_code()  # Get C++ code input from the user
lexer = Lexer(cpp_code)  # Create a Lexer instance with the input code
lexer.tokenize()  # Tokenize the input code
lexer.print_tokens()  # Print the tokens found
