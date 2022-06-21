

def designerPdfViewer(h, word):
    # Write your code here
    letter_house = {}
    letters_list = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(letters_list)):
        letter_house[letters_list[i]] = h[i]
    
    max_value = 0
    for w in word:
        if letter_house[w]>max_value:
            max_value = letter_house[w]
    return max_value * len(word)


print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],'abc'))