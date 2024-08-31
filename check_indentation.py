import os
import tokenize

def check_indentation(filename):
    with tokenize.open(filename) as file:
        try:
            tokens = list(tokenize.generate_tokens(file.readline))
            for token in tokens:
                if token.type == tokenize.INDENT:
                    if len(token.string) % 4 != 0:
                        print(f"Inconsistent indentation in {filename} at line {token.start[0]}")
        except tokenize.TokenError as e:
            print(f"Indentation error in {filename}: {str(e)}")

def walk_dir(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith('.py'):
                check_indentation(os.path.join(root, file))

if __name__ == "__main__":
    walk_dir('src')