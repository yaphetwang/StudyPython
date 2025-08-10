file = open('input.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()

# with expression [as variable]:
#     代码块
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    file_content = infile.read()
    print(file_content)
    print(outfile.closed)
    outfile.write(file_content)
