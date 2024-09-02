import re
from typing import List

def to_camel_case(string: str) -> str:
    """Convert a string to camelCase."""
    words = string.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])

def to_pascal_case(string: str) -> str:
    """Convert a string to PascalCase."""
    return ''.join(word.capitalize() for word in string.split('_'))

def to_snake_case(string: str) -> str:
    """Convert a string to snake_case."""
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('_', string).lower()

def to_kebab_case(string: str) -> str:
    """Convert a string to kebab-case."""
    return to_snake_case(string).replace('_', '-')

def pluralize(singular: str) -> str:
    """
    Return the plural form of a word.
    This is a very basic implementation and doesn't cover all English pluralization rules.
    For more accurate results, consider using a library like `inflect`.
    """
    if singular.endswith('y'):
        return singular[:-1] + 'ies'
    elif singular.endswith('s'):
        return singular + 'es'
    else:
        return singular + 's'

def singularize(plural: str) -> str:
    """
    Return the singular form of a word.
    This is a very basic implementation and doesn't cover all English singularization rules.
    For more accurate results, consider using a library like `inflect`.
    """
    if plural.endswith('ies'):
        return plural[:-3] + 'y'
    elif plural.endswith('es'):
        return plural[:-2]
    elif plural.endswith('s'):
        return plural[:-1]
    else:
        return plural

def capitalize_first(string: str) -> str:
    """Capitalize the first letter of a string."""
    return string[0].upper() + string[1:] if string else ''

def uncapitalize_first(string: str) -> str:
    """Uncapitalize the first letter of a string."""
    return string[0].lower() + string[1:] if string else ''

def split_words(string: str) -> List[str]:
    """Split a string into words based on camelCase, PascalCase, or snake_case."""
    pattern = re.compile(r'[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+')
    return pattern.findall(string)

def join_words(words: List[str], separator: str = ' ') -> str:
    """Join a list of words with a separator."""
    return separator.join(words)

def sanitize_filename(filename: str) -> str:
    """
    Sanitize a string to be used as a filename.
    Remove or replace characters that are not suitable for filenames.
    """
    # Replace spaces and other characters with underscores
    filename = re.sub(r'[^\w\-_\. ]', '_', filename)
    # Remove any leading or trailing periods or spaces
    return filename.strip('. ')