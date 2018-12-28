// 605. Can Place Flowers
// https://leetcode.com/problems/can-place-flowers/

package main

import "fmt"

func canPlaceFlowers(flowerbed []int, n int) bool {
	i := 0
	length := len(flowerbed)
	if length == 1 {
		return flowerbed[0] == 0
	}
	count := 0
	for i <= length-1 {
		if flowerbed[i] == 0 {
			if i == 0 {
				if i+1 <= length-1 && flowerbed[i+1] == 0 {
					count += 1
					flowerbed[i] = 1
				}
			} else if i == length-1 {
				if i-1 >= 0 && flowerbed[i-1] == 0 {
					count += 1
					flowerbed[i] = 1
				}
			} else {
				if i-1 >= 0 && i+1 <= length-1 && flowerbed[i-1] == 0 && flowerbed[i+1] == 0 {
					count += 1
					flowerbed[i] = 1
				}
			}
		}
		if count >= n {
			return true
		}
		i += 1
	}
	return false
}

func main() {
	fmt.Println(canPlaceFlowers([]int{1}, 1))
}
