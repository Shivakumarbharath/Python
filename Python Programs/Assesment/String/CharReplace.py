'''
. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'


'''

smpl = input("Enter 2 strings seperated by ',' ").split(',')

chr1, chr2 = smpl[0][-1], smpl[1][-1]

print(smpl[0][0:-1] + chr2 + ' ' + smpl[1][0:-1] + chr1)
