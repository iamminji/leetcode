/*
	492. Construct the Rectangle
	https://leetcode.com/problems/construct-the-rectangle/
*/

package main

import (
	"fmt"
	"math"
)

func constructRectangle(area int) []int {
	end := math.Sqrt(float64(area))
	result := []int{area, 1}
	for i := 2; i <= int(end); i++ {
		if float64(area)/float64(i) == float64(i) {
			result = []int{area/i, i}
			break
		}
		if area % i == 0 {
			if result[0] - result[1] >= (area/i -  i) {
				result = []int{area/i, i}
			}
		}
	}

	if result[0] > result[1] {
		return []int{result[0], result[1]}
	}
	return []int{result[1], result[0]}
}

func main() {
	fmt.Println(constructRectangle(5))
}