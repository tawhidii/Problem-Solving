
class Solution:
    def flipAndInvertImage(self, image):
        result = []
        for row in image:
            temp = []
            for cell in row[::-1]:
                if cell == 0:
                    temp.append(1)
                else:
                    temp.append(0)
            result.append(temp)
        return result


        # result = []
        # rev_image = []
        # for im in image:
        #     rev_image.append(list(reversed(im)))
        # for i in range(len(rev_image)):
        #     temp = []
        #     for j in range(len(rev_image[i])):
        #         if rev_image[i][j] == 1:
        #             temp.append(0)
        #         else:
        #             temp.append(1)
        #     result.append(temp)
        # return result




s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))