func getConcatenation(nums []int) []int {
	n := len(nums) * 2
	ans := make([]int, n)
	for idx, num := range nums {
		ans[idx] = num
		ans[idx+len(nums)] = num

	}
	return ans
}
