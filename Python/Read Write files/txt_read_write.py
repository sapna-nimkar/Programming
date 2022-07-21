'''
python oprogram to read , write a text file
'''

with open("my_textfile.txt", "w") as myfile:
    result = myfile.writelines('This is my new text file \n and this is good.')

with open("my_textfile.txt", "r") as myfile:
    result = myfile.readlines()[1]
    print(result)

    