/*
 * Complete the 'compareTriplets' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

func compareTriplets(a []int32, b []int32) []int32 {
	value_alice := 0
	value_bob := 0
	for i := 0; i < len(a); i++ {
		if a[i] > b[i] {
			value_alice = value_alice + 1
		}
		if a[i] < b[i] {
			value_bob = value_bob + 1
		}
	}
	// fmt.Println(value_alice)
	// fmt.Println(value_bob)
	result := []int32{int32(value_alice), int32(value_bob)}
	return result
}

