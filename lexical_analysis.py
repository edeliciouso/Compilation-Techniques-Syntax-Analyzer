import ply.lex as lex

# List of token names
tokens = (
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA', 'IF', 'ELSE', 'WHILE', 'RETURN',
    'INT', 'FLOAT', 'CHAR', 'GT', 'LT'
)

# Regular expressions for simple tokens
t_PLUS     = r'\+'
t_MINUS    = r'-'
t_TIMES    = r'\*'
t_DIVIDE   = r'/'
t_EQUALS   = r'='
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACE   = r'\{'
t_RBRACE   = r'\}'
t_SEMICOLON = r';'
t_COMMA    = r','
t_GT       = r'>'
t_LT       = r'<'

# Keywords
keywords = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
    'int': 'INT',
    'float': 'FLOAT',
    'char': 'CHAR'
}

# Identifiers and numbers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value, 'ID')  # Check for keywords
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it
data = """
int x = 10;
if (x > 5) {
    return x;
}
"""

# Tokenize the input
lexer.input(data)

# Adjust the print output to display only token type and value
for tok in lexer:
    print(f'({tok.type}, {tok.value})')
