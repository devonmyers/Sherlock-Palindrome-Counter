def file_reader(file_name):
    '''Opens a text file and returns a list of strings, where each list
    element corresponds to one sentence/line contained in the text file'''

    with open(file_name, 'r') as file:
        contents = file.readlines()
        file.close()
    return contents

def clean_contents(dirty_contents):
    '''Cleans contents by removing special characters, removing new lines and
    blank elements of list, and ultimately splits input string into individual
    words'''

    cleaned_contents = []
    if type(dirty_contents) == list:
        for i in range(len(dirty_contents)):
            if dirty_contents[i] != 'n':
                dirty_contents[i] = dirty_contents[i].strip()
                split_words = dirty_contents[i].split()
                for j in range(len(split_words)):
                    split_words[j] = specialchar_replace(split_words[j])
                    if split_words[j] != '': cleaned_contents.append(split_words[j])
        return cleaned_contents
    else: return 'Invalid argument type!'

def palindrome_counter(data, distinct=False):
    '''Counts the number of palindromes in given input.  Palindromes are counted
    by individual words, and also phrases of each length up to the phrase_length
    argument.  The distinct argument, which defaults to False, determines wheter
    or not the number of different palindromes is returned (distinct=True) or
    the total number of all palindromes is returned (distinct=False)'''

    if type(data) != list : return None
    palindromes = {} # Empty dictionary of palindromes.
    # Keys will be the text that makes the palindrome, value will the count of that palindrome

    for i in range(len(data)):
        data[i] = data[i].lower()   # make all text lower case
        if isPalindrome(data[i]):   # current text is a palindrome
            if data[i] not in palindromes: # update dictionary of previously seen palindromes
                palindromes[data[i]] = 1
            else: # current text is a previously seen palindrome, update its value
                old_count = palindromes[data[i]]
                palindromes[data[i]] += 1
    #print(palindromes)
    if distinct:
        return len(palindromes) # number of distinct palindromes is the number of keys in the dict
    else: # number of palindromes is the sum of times we have seen each palindrome
        count = 0
        for key, value in palindromes.items():
            count += value
        return count

def reverse_string(s):

    '''Reverses the order of characters for input string.'''
    if type(s) == str: return s[::-1]
    else: return 'Invalid input data type'
    
def isPalindrome(s):
    '''Checks if input string is a palindrome'''

    return s == reverse_string(s)

def specialchar_replace(s):
    '''Replaces special charactes such as punctuation, apostrophes, etc.'''

    if '\n' in s:
        s = s.replace('\n', '')
    if '\'' in s:
        s = s.replace('\'', '')
    if '\"' in s:
        s = s.replace('\"', '')
    if '.' in s:
        s = s.replace('.', '')
    if '-' in s:
        s = s.replace('-','')
    if '(' in s:
        s = s.replace('(', '')
    if ')' in s:
        s = s.replace(')', '')
    if '?' in s:
        s = s.replace('?', '')
    if '!' in s:
        s = s.replace('!', '')
    if '/' in s:
        s = s.replace('/', '')
    if '&' in s:
        s = s.replace('&', '')
    if ',' in s:
        s = s.replace(',', '')
    if ';' in s:
        s = s.replace(';', '')
    return s

def pretty_print(input_list):
    '''Prints element by element of input list'''

    if type(input_list) == list:
        _length = len(input_list)
        for i in range(_length): print(input_list[i])
    else: print('Invalid argument type!')

def string_concatenator(data, phrase_length):
    '''Takes in a list of strings and concatenates phrase_length-many strings'''

    string_list = []
    if type(data) == list and type(phrase_length) == int:
        if phrase_length < 0:  return None
        for i in range(len(data) - phrase_length):
            concat = ''
            for j in range(phrase_length+1):
                concat += data[i+j]
            if concat != '' : string_list.append(concat)
        return string_list
    else: return None

if __name__ == "__main__":    
    #file_name = 'mini_adventure.txt'   # Test file
    file_name = 'adventures.txt'
    contents  = file_reader(file_name)
    clean_contents = clean_contents(contents)
    print(f'Total number of words in the document is {len(clean_contents)}')
    # Check for palindromic phrases of varying length
    for p in range(5):   # No palindromes of length > 3
        phrases = []
        phrases += string_concatenator(clean_contents, p)
        print(f'There are a total of {len(phrases)} phrases of length {p+1}')
        total = palindrome_counter(phrases)
        distinct = palindrome_counter(phrases, distinct=True)
        if total != 0:
            print(f'There are {total} total palindromes with phrase length of {p+1}.')
            print(f'The proportion of palindromes is {total/len(phrases)}')
        if distinct != 0: print(f'There are {distinct} many distinct palindromes with phrase length of {p+1}.\n' )
        if total == 0 and distinct == 0:
            print(f'There are no palindromes with phrase length {p+1}.\n')        
