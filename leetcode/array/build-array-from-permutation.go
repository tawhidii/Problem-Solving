// generic solution
// func buildArray(nums []int) []int {
// 	var ans []int
// 	for idx, _ := range nums {
// 		ans = append(ans, nums[nums[idx]])
// 	}
// 	return ans
// }

// most optimal one
func buildArray(nums []int) []int {
	ans := make([]int, len(nums))
	for idx, num := range nums {
		ans[idx] = nums[num]
	}
	return ans
}