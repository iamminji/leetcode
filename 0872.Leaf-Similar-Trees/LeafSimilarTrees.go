// 872. Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/submissions/

package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func recursive(node *TreeNode, ans *[]int) {

	if node.Left == nil && node.Right == nil {
		*ans = append(*ans, node.Val)
		return
	}
	if node.Left != nil {
		recursive(node.Left, ans)
	}
	if node.Right != nil {
		recursive(node.Right, ans)
	}
	return
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	a := make([]int, 0)
	b := make([]int, 0)

	recursive(root1, &a)
	recursive(root2, &b)

	if len(a) != len(b) {
		return false
	}

	for idx, v := range a {
		if b[idx] != v {
			return false
		}
	}
	return true
}
