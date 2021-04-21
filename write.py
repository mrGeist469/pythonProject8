def read_files(*files_name):
    size_files = {}
    file_1 = ''
    file_2 = ''
    file_3 = ''
    count_file = 0
    for file_name in files_name:
        count_file += 1
        count_line = 0
        with open(file_name, encoding='utf-8') as file:
            for line in file:
                count_line += 1
                if count_file == 1:
                    file_1 += line
                elif count_file == 2:
                    file_2 += line
                else:
                    file_3 += line
            size_files[file_name] = count_line
    if size_files['1.txt'] < size_files['2.txt'] < size_files['3.txt']:
        with open('4.txt', 'a', encoding='utf-8') as file:
            file.write('1.txt' + '\n')
            file.write(str(size_files['1.txt']) + '\n')
            file.write(file_1 + '\n')
            file.write('2.txt' + '\n')
            file.write(str(size_files['2.txt']) + '\n')
            file.write(file_2 + '\n')
            file.write('3.txt' + '\n')
            file.write(str(size_files['3.txt']) + '\n')
            file.write(file_3 + '\n')
    elif size_files['1.txt'] > size_files['2.txt'] > size_files['3.txt']:
        with open('4.txt', 'a', encoding='utf-8') as file:
            file.write('3.txt' + '\n')
            file.write(str(size_files['3.txt']) + '\n')
            file.write(file_3 + '\n')
            file.write('2.txt' + '\n')
            file.write(str(size_files['2.txt']) + '\n')
            file.write(file_2 + '\n')
            file.write('1.txt' + '\n')
            file.write(str(size_files['1.txt']) + '\n')
            file.write(file_1 + '\n')
    elif size_files['1.txt'] < size_files['2.txt'] or size_files['3.txt'] < size_files['1.txt']:
        with open('4.txt', 'a', encoding='utf-8') as file:
            file.write('3.txt' + '\n')
            file.write(str(size_files['3.txt']) + '\n')
            file.write(file_3 + '\n')
            file.write('1.txt' + '\n')
            file.write(str(size_files['1.txt']) + '\n')
            file.write(file_1 + '\n')
            file.write('2.txt' + '\n')
            file.write(str(size_files['2.txt']) + '\n')
            file.write(file_2 + '\n')
    elif size_files['1.txt'] < size_files['2.txt'] or size_files['3.txt'] < size_files['2.txt']:
        with open('4.txt', 'a', encoding='utf-8') as file:
            file.write('1.txt' + '\n')
            file.write(str(size_files['1.txt']) + '\n')
            file.write(file_1 + '\n')
            file.write('3.txt' + '\n')
            file.write(str(size_files['3.txt']) + '\n')
            file.write(file_3 + '\n')
            file.write('2.txt' + '\n')
            file.write(str(size_files['2.txt']) + '\n')
            file.write(file_2 + '\n')
    elif size_files['1.txt'] > size_files['2.txt'] or size_files['3.txt'] > size_files['1.txt']:
        with open('4.txt', 'a', encoding='utf-8') as file:
            file.write('2.txt' + '\n')
            file.write(str(size_files['2.txt']) + '\n')
            file.write(file_2 + '\n')
            file.write('1.txt' + '\n')
            file.write(str(size_files['1.txt']) + '\n')
            file.write(file_1 + '\n')
            file.write('3.txt' + '\n')
            file.write(str(size_files['3.txt']) + '\n')
            file.write(file_3 + '\n')
    else:
        with open('4.txt', 'a', encoding='utf-8') as file:
            file.write('2.txt' + '\n')
            file.write(str(size_files['2.txt']) + '\n')
            file.write(file_2 + '\n')
            file.write('3.txt' + '\n')
            file.write(str(size_files['3.txt']) + '\n')
            file.write(file_3 + '\n')
            file.write('1.txt' + '\n')
            file.write(str(size_files['1.txt']) + '\n')
            file.write(file_1 + '\n')


read_files('1.txt', '2.txt', '3.txt')
