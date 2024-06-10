#String to Integer (atoi)
#Implement the myAtoi(string) function, which converts a string to a 32-bit signed integer.

#The algorithm for myAtoi(string) is as follows:

# 1. Whitespace: Ignore any leading whitespace (" ")
# 2. Signedness: Determine the sign by checking ig the next character is '-' or '+', assuming positivity is neither present.
# 3. Conversion: Read the integer by skipping leading zeroes until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# 4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be set to -2^31, and integers greater than 2^31 - 1 should be set to 2^31 - 1.

#Example 1:
#Input: s = "42"
#Output: 42
#The underlined characters are what is read in and the caret is the current reader position. Step 1: "42" (no characters read becasue there is no leading whitespace)
#Step 2: "42" (no leading '+' or '-' character to read)

