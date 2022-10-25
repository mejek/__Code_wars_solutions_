# Description:
#
# You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:
#
# "1000.00
# 125 Market 125.45
# 126 Hardware 34.95
# 127 Video 7.45
# 128 Book 14.32
# 129 Gasoline 16.10"
#
# The first line shows the original balance. Each other line (when not blank) gives information:
# check number, category, check amount. (Input form may change depending on the language).
#
# First you have to clean the lines keeping only letters, digits, dots and spaces.
#
# Then return a report as a string (underscores show spaces -- don't put them in your solution.' \
#  They are there so you can see them and how many of them you need to have):
#
# "Original_Balance:_1000.00
# 125_Market_125.45_Balance_874.55
# 126_Hardware_34.95_Balance_839.60
# 127_Video_7.45_Balance_832.15
# 128_Book_14.32_Balance_817.83
# 129_Gasoline_16.10_Balance_801.73
# Total_expense__198.27
# Average_expense__39.65"
#
# On each line of the report you have to add the new balance and then in the last two lines
# the total expense and the average expense. So as not to have a too long result string
# we don't ask for a properly formatted result.
# Notes
#
#     See input examples in Sample Tests.
#     It may happen that one (or more) line(s) is (are) blank.
#     Round to 2 decimals your calculated results (Elm: without traling 0)
#     The line separator of results may depend on the language \n or \r\n. See examples in the "Sample tests".
#     R language: Don't use R's base function "mean()" that could give results slightly different from expected ones.
#
# My solution:

book = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""
def balance(book):
    cleaned_book = []
    for line in book.split('\n'):
        if line == '':
            continue
        else:
            cleaned_book.append(''.join([x for x in line if (x.isalnum() or x in ' .')]))

    formated_book = []
    count = 0

    for n in range(len(cleaned_book)):
        if n == 0:
            actual_balance = original_balance = float(cleaned_book[n])
            formated_book.append(f'Original Balance: {float(cleaned_book[n]):.2f}')
        else:
            actual_balance -= float(cleaned_book[n].split()[-1])
            count += 1
            formated_book.append(' '.join(cleaned_book[n].split()[:2]) +
                                 f' {float(cleaned_book[n].split()[-1]):.2f} ' + f'Balance {actual_balance:.2f}')

    total_expence = round(original_balance-actual_balance, 2)
    formated_book.append(f'Total expense  {total_expence:.2f}')
    formated_book.append(f'Average expense  {total_expence/count:.2f}')
    return '\r\n'.join(formated_book)



balance(book)