with open('document.txt') as f:
 filecontens=f.read()
 print(filecontens)
print('File is closed:' ,f.closed)
