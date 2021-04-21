# file_1 = ''
# count_1 = 0
# with open('1.txt', encoding='utf-8') as file:
#     for line in file:
#         count_1 += 1
#         file_1 += line
#
# file_2 = ''
# count_2 = 0
# with open('2.txt', encoding='utf-8') as file:
#     for line in file:
#         count_2 += 1
#         file_2 += line
#
# file_3 = ''
# count_3 = 0
# with open('3.txt', encoding='utf-8') as file:
#     for line in file:
#         count_3 += 1
#         file_3 += line

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


read_files('1.txt', '2.txt', '3.txt')

# def write(*files):
#     with open('4.txt', 'a', encoding='utf-8') as file:
#         file.write(str(count_1) + '\n')
#         file.write(file_1)
#
#
# print(count_1)

