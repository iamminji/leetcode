// 921. Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

package main

import (
	"fmt"
)

type Stack struct {
	items []string
	len   int
}

func (stack *Stack) Push(p string) {
	stack.items = append(stack.items, p)
	stack.len += 1
}

func (stack *Stack) Pop() string {
	item := stack.items[stack.len-1]
	stack.items = stack.items[:stack.len-1]
	stack.len -= 1
	return item
}

func (stack *Stack) isEmpty() bool {
	return stack.len == 0
}

func minAddToMakeValid(S string) int {

	stack := Stack{}
	var res int

	for _, s := range S {
		if string(s) == "(" {
			stack.Push(")")
		} else {
			if !stack.isEmpty() {
				item := stack.Pop()
				if string(s) != item {
					res += 1
				}
			} else {
				res += 1
			}
		}
	}
	return res + stack.len
}

func main() {
	fmt.Println(minAddToMakeValid("()))(("))
	fmt.Println(minAddToMakeValid(""))
	fmt.Println(minAddToMakeValid(")"))
	fmt.Println(minAddToMakeValid("(())()("))

}
