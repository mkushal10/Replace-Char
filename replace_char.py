# Get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'jashd', 'yuasdg'
# Expected Result : 'yushd jaasdg'

def getSwapFirstTwoCharOfString(input_str1, input_str2):
    input_str1 = list(input_str1.split()[0])
    input_str2 = list(input_str2.split()[0])
    input_str1[0:2], input_str2[0:2] = input_str2[0:2], input_str1[0:2]

    return ('').join(input_str1) + ' ' + ('').join(input_str2)

if __name__ == "__main__":
    first_string = input('Fnter the first string : ')
    second_string = input('Enter the second string : ')
    print(getSwapFirstTwoCharOfString(first_string, second_string))
