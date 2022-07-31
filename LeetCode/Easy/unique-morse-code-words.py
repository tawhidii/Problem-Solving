class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",
        ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
        "..-","...-",".--","-..-","-.--","--.."]
        letters = "abcdefghijklmnopqrstuvwxyz"
        l=[]
        data = {}

        for z in range(len(letters)):
            data[letters[z]] = morse[z]
        
        for word in words:
            str_ = ""
            for w in word:
                str_  = str_ + data[w]
            l.append(str_)
        return len(set(l))  
        
        
                
        
s = Solution()
s.uniqueMorseRepresentations(["gin","zen","gig","msg"])



