#variables
digit = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
tens = {'0': '', '1': {'0': 'ten', '1': 'eleven', '2': 'twelve', '3': 'thirteen', '4': 'fourteen', '5': 'fifteen',
                       '6': 'sixteen', '7': 'seventeen', '8': 'eighteen', '9': 'nineteen'},
        '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty',
        '9': 'ninety', }
unit = {0: '', 1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion', 6: 'quintillion',
        7: 'sextillion', 8: 'septillion', 9: 'octillion', 10: 'nonillion', 11: 'decillion',
        12: 'undecillion', 13: 'duodecillion', 14: 'tredecillion', 15: 'quatttuor-decillion', 16: 'quindecillion',
        17: 'duodecillion', 18: 'tredecillion', 19: 'octodecillion', 20: 'novemdecillion', 21: 'vigintillion'}

#function to convert block of 3 numbers to words
def block_converter(block):
    block_word = ''
    if int(block) == 0:
        return 'zero'
    for i, v in enumerate(block):
        if v != '0':
            if i == 0:
                block_word += digit[v] + ' hundred '
            if i == 1:
                block_word += tens[v][block[2]] if int(v) == 1 else tens[v]
                if v != '1' and block[2] != '0':
                    block_word += '-'
            if i == 2 and block[1] != '1':
                block_word += digit[v]
    return block_word

#function to use block_converter function to convert the whole number into words
def converter(number):
    word = ''
    blocks = [''.join(number[i:i + 3]) for i in range(0, len(number), 3)]
    for index, block in enumerate(blocks[::-1]):
        word = block_converter(block) + ' ' + unit[index] + ', ' + word
    return word

#main code
if __name__ == '__main__':
    while True:
        try:
            num = str(int(input('Enter any number: ')))
            break
        except ValueError:
            print("Not a number. Input again.")
    n = (len(num) // 3 + 1) * 3 if len(num) % 3 != 0 else len(num)
    print(f'{converter(num.zfill(n))[:-2].rstrip().capitalize()}')