"""
-------------------------------------------------------
Morse Code Definitions and Functions
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""


# In order by letters.
data1 = (('A', '.-'), ('B', '-...'), ('C', '-.-.'),
         ('D', '-..'), ('E', '.'), ('F', '..-.'),
         ('G', '--.'), ('H', '....'), ('I', '..'),
         ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
         ('M', '--'), ('N', '-.'), ('O', '---'),
         ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'),
         ('S', '...'), ('T', '-'), ('U', '..--'),
         ('V', '...-'), ('W', '.--'), ('X', '-..-'),
         ('Y', '-.--'), ('Z', '--..'))

# In order by splitting.
data2 = (('M', '--'), ('F', '..-.'), ('T', '-'),
         ('C', '-.-.'), ('J', '.---'), ('P', '.--.'),
         ('W', '.--'), ('A', '.-'), ('D', '-..'),
         ('H', '....'), ('K', '-.-'), ('N', '-.'),
         ('R', '.-.'), ('U', '..--'), ('Y', '-.--'),
         ('B', '-...'), ('E', '.'), ('I', '..'),
         ('G', '--.'), ('L', '.-..'), ('O', '---'),
         ('Q', '--.-'), ('S', '...'), ('V', '...-'),
         ('X', '-..-'), ('Z', '--..'))

# In order by popularity.
data3 = (('E', '.'), ('T', '-'), ('A', '.-'),
         ('O', '---'), ('I', '..'), ('N', '-.'),
         ('S', '...'), ('H', '....'), ('R', '.-.'),
         ('D', '-..'), ('L', '.-..'), ('U', '..--'),
         ('C', '-.-.'), ('M', '--'), ('P', '.--.'),
         ('F', '..-.'), ('Y', '-.--'), ('W', '.--'),
         ('G', '--.'), ('B', '-...'), ('V', '...-'),
         ('K', '-.-'), ('J', '.---'), ('X', '-..-'),
         ('Z', '--..'), ('Q', '--.-'))


class ByLetter:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by letter attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByLetter object.
        Use: var = ByLetter(letter, code)
        -------------------------------------------------------
        Preconditions:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Postconditions:
            ByLetter values are set.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, rhs):
        """
        -------------------------------------------------------
        Compares this ByLetter against another ByLetter for equality.
        Object are equal if their letters match.
        Use: v1 == v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByLetter to compare to (ByLetter)
        Postconditions:
            returns
            result - True if letters match, False otherwise (boolean)
        -------------------------------------------------------
        """
        return self.letter == rhs.letter

    def __lt__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this ByLetter comes before another.
        Use: v1 < v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByLetter to compare to (ByLetter)
        Postconditions:
            returns
            result - True if this ByLetter precedes rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        return self.letter < rhs.letter

    def __le__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this ByLetter precedes or is or equal to another.
        Use: v1 <= v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByLetter to compare to (ByLetter)
        Postconditions:
            returns
            result - True if this ByLetter precedes or is equal to rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        return self.letter <= rhs.letter

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByLetter data.
        Use: print(v)
        Use: string = str(v)
        -------------------------------------------------------
        Postconditions:
            returns
            string - the formatted contents of ByLetter (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.letter, self.code)


class ByCode:
    """
    -------------------------------------------------------
    Stores letters and matching Morse codes. Compares
    elements by code attribute.
    -------------------------------------------------------
    """

    def __init__(self, letter, code):
        """
        -------------------------------------------------------
        Initialize a ByCode object.
        Use: var = ByCode(letter, code)
        -------------------------------------------------------
        Preconditions:
            letter - a letter of the alphabet (str)
            code - the Morse code matching letter (str)
        Postconditions:
            ByCode values are set.
        -------------------------------------------------------
        """
        self.letter = letter
        self.code = code
        return

    def __eq__(self, rhs):
        """
        -------------------------------------------------------
        Compares this ByCode against another ByCode for equality.
        Object are equal if their codes match.
        Use: v1 == v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByCode to compare to (ByCode)
        Postconditions:
            returns
            result - True if codes match, False otherwise (boolean)
        -------------------------------------------------------
        """
        return self.code == rhs.code

    def __lt__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this ByCode comes before another.
        Use: v1 < v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByCode to compare to (ByCode)
        Postconditions:
            returns
            result - True if this ByCode precedes rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        return self.code < rhs.code

    def __le__(self, rhs):
        """
        -------------------------------------------------------
        Determines if this ByCode precedes or is or equal to another.
        Use: v1 <= v2
        -------------------------------------------------------
        Preconditions:
            rs - [right side] ByCode to compare to (ByCode)
        Postconditions:
            returns
            result - True if this ByCode precedes or is equal to rs,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        return self.code <= rhs.code

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of ByCode data.
        Use: print(v)
        Use: string = str(v)
        -------------------------------------------------------
        Postconditions:
            returns
            string - the formatted contents of ByCode (str)
        -------------------------------------------------------
        """
        return "({}, {})".format(self.code, self.letter)



def fill_letter_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByLetter Morse code letter/code pairs
    (Function must convert contents of values to ByLetter objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    while i < len(values):
        x = ByLetter(values[i][0], values[i][1])
        bst.insert(x)
        i += 1
    return


def fill_code_bst(bst, values):
    """
    -------------------------------------------------------
    Fills a BST with ByCode Morse code letter/code pairs.
    (Function must convert contents of values to ByCode objects)
    Use: fill_letter(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a bst (BST)
        values - set of Morse code letter/code pairs (list of tuples)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    while i < len(values):
        x = ByCode(values[i][0], values[i][1])
        bst.insert(x)
        i += 1
    return


def encode_morse(bst, text):
    """
    -------------------------------------------------------
    Converts English text to Morse code
    Use: code = encode_morse(bst, text)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by letter (BST)
        text - English text to convert (str)
    Returns:
        result - Morse code version of text (str)
    -------------------------------------------------------
    """
    result = ""
    for i in text:
        
        if i !=" ":
            var = ByLetter(i.upper(), None)
            v = bst.retrieve(var)
            
            if v is not None:
                result += str(v.code)
                result += " "
        else:
            result += "\n"
    return result

def decode_morse(bst, code):
    """
    -------------------------------------------------------
    Converts Morse code to English text
    Use: text = decode_morse(bst, code)
    -------------------------------------------------------
    Parameters:
        bst - Morse code bst sorted by code (BST)
        code - Morse code to convert (str)
    Returns:
        result - English version of code (str)
    -------------------------------------------------------
    """
    result = ""
    code = code.split()
    for i in code:
        
        if i !=" ":
            var = ByCode(None, i)
            v = bst.retrieve(var)
            
            if v is not None:
                result += v.letter  
            else:
                result += " "
    return result

        
        
