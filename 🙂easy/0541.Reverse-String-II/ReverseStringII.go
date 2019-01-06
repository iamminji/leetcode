// 541. Reverse String II
// https://leetcode.com/problems/reverse-string-ii/
package main

import (
	"fmt"
)

func reverse(r []rune) []rune {
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return r
}

func reverseStr(s string, k int) string {
	r := []rune(s)

	for i := 0; i < len(s); i += 2 * k {
		if i < len(s)-k {
			reverse(r[i : i+k])
		} else {
			reverse(r[i:len(s)])
		}
	}
	return string(r)
}

func main() {
	//fmt.Println(reverseStr("abcdefghijk", 2))
	//fmt.Println(reverseStr("abcdefghijk", 3))
	fmt.Println(reverseStr("a", 2))
	fmt.Println(reverseStr("ab", 3))
	//fmt.Println(reverseStr("abcde", 2))
	//fmt.Println(reverseStr("kabcdefghijk", 3))
	fmt.Println(reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))
}
