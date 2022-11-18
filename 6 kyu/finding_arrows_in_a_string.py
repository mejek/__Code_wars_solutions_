def arrow_search(string: str) -> int:
    result = []
    for _string in [string, string.replace('<','_').replace('>', '<').replace('_', '>')[::-1]]:
        print(_string)
        arrow_flag = 0
        tail_flag = ''
        count = 0
        for n in _string:

            if n == '<' and tail_flag == '':
                count += 1
                arrow_flag = 1

            if arrow_flag == 1 and tail_flag == '':
                if n == '.' or n == '>':
                    arrow_flag = 0
                    tail_flag = ''
                if n == '-':
                    count += 1
                    tail_flag = '-'
                if n == '=':
                    count += 3
                    tail_flag = '='

            elif arrow_flag == 1 and tail_flag != '':
                if n == '<':
                    count += 1
                    tail_flag = ''
                elif tail_flag == '-':
                    if n == '-':
                        count += 1
                    else:
                        tail_flag = ''
                        arrow_flag = 0
                elif tail_flag == '=':
                    if n == '=':
                        count += 2
                    else:
                        tail_flag = ''
                        arrow_flag = 0
            print(n, count)
        result.append(count)
    print(result)
    return result[1] - result[0]

arrow_search('>>><.=<=<..=<>')
