// 443. String Compression
// https://leetcode.com/problems/string-compression/
package main

import (
	"fmt"
	"strconv"
)

func compress(chars []byte) int {

	start := 0
	end := 0
	count := 0

	for end < len(chars) {
		chars[start] = chars[end]
		for end < len(chars) && chars[start] == chars[end] {
			count++
			end++
		}
		if count > 1 {
			countStr := strconv.Itoa(count)
			for _, c := range []byte(countStr) {
				start++
				chars[start] = c
			}
		}
		start++
		count = 0
	}
	return start
}

func main() {
	// 'a2b3c3d1' => 8
	fmt.Println(compress([]byte{'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'}))
	fmt.Println(compress([]byte{'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'}))
	fmt.Println(compress([]byte{'a', 'a', 'd', 'd'}))
	fmt.Println(compress([]byte{'a', 'b', 'a'}))
	fmt.Println(compress([]byte{'b', 'b', 'b'}))
}
