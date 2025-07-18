try:
    f = open('file1.txt', 'r')  # dostaje FileNotFoudError
    try:
        s = f.readlines()
        print(s)
    finally: #ten blok robi sie zawsze
        f.close()
except FileNotFoundError:
    print('File not found')
except:
    print('Something went wrong')

# f2 = open('file1.txt', 'w', encoding='utf-8')
# f2.write('Hello world')

#to samo przez with
try:
    with open('file1.txt', 'r') as f: #zamienia blok try and finally
        s = f.readlines()
        print(s)
except FileNotFoundError:
    print('File not found')

