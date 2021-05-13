def mid_palindromes(filename):
    with open(filename, 'r') as fr, open('output_p.txt', 'w') as fw:
        for line in fr:
            line= line.strip()
            if line[1:-1]== line[-2:0:-1]:
                #or print(line[1:-1], line[1:-1][::-1])
                fw.write(line +'\n')

mid_palindromes('input_p.txt')