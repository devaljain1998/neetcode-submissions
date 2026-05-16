DELIMITER = '#'

class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Format: '{LENGTH_OF_WORD}{DELIMITED}{ORIGINAL_STRING}'
        """
        encoded_strings = []
        for s in strs:
            encoded_string = f'{len(s)}{DELIMITER}{s}'
            encoded_strings.append(encoded_string)
        return ''.join(encoded_strings)


    def decode(self, s: str) -> List[str]:
        """
        1. Read the length of the string -> l
        2. Skip the delimiter
        3. Read the next l words after it
        4. Append the words in the string
        """

        strings = []
        i, n = 0, len(s)

        while i < n:
            # Determine the length of the string:
            digits = 1
            while (i+digits-1) < n and s[i+digits-1].isdigit():
                digits += 1

            l = int(s[i:i+digits-1])
            
            i = i + digits # Next word should be followed by a delimiter
            word = ''
            for j in range(i, i+l):
                word += s[j]
            strings.append(word)
            i += l
        
        return strings
        