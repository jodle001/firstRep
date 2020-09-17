#This is a pythong file made in VIM.

def count(lst):
    count = 0
    for i in lst:
        count += 1
    return count

sampleList = ["tree", "dog", "copper", "snail", "brush"]


def main():
    num  = count(sampleList)
    return num

print(main())
