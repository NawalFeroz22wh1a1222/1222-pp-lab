
# uppercase in a sentence
def convert(s):

    # Create a char array of
    # given string
    ch = list(s)
    print(ch)

    for i in range(len(s)):

        # If first character of a word is found
        if (i == 0 and ch[i] != ' ' or
                       ch[i] != ' ' and
                       ch[i - 1] == ' '):

            # If it is in lower-case
            if (ch[i] >= 'a' and ch[i] <= 'z'):

                # Convert into Upper-case
                ch[i] = chr(ord(ch[i]) - ord('a') +
                            ord('A'))

        # If apart from first character
        # Any one is in Upper-case
        elif (ch[i] >= 'A' and ch[i] <= 'Z'):

            # Convert into Lower-Case
            ch[i] = chr(ord(ch[i]) + ord('a') -
                        ord('A'))

    # Convert the char array
    # to equivalent string
    st = "".join(ch)

    return st



s = "hello world"

print(convert(s))