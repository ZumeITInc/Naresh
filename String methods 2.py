# rstrip(): this function removes specific special character to the right side of given string
string = '!!!!Python Developer!!!!'
string.rstrip( '!' )
print(string.rstrip( '!' ) )

# strip(): this function removes specific special character from both sides to the given string.
string.strip( '!' )
print(string.strip('!') )


# swapcase(): This function swaps all lower case letters into upper case and vice versa.
string.swapcase()
print(string.swapcase())


# reversed(): this function reverses the string
print(string.join(reversed(string)))

# replace(): this function replaces an existing character(s) with new character(s).
string_one = string.replace( "python is a"," programming language" )
print(string_one
      )
