// 337. House Robber III
// https://leetcode.com/problems/house-robber-iii/

package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode `json:"left"`
	Right *TreeNode `json:"right"`
}

func max(v1, v2 int) int {
	if v1 > v2 {
		return v1
	}
	return v2
}

func recursive(node *TreeNode, visited map[*TreeNode]int) int {

	var v int

	if node == nil {
		return 0
	}

	if val, ok := visited[node]; ok {
		return val
	}

	if node.Left != nil {
		v += recursive(node.Left.Left, visited) + recursive(node.Left.Right, visited)
	}

	if node.Right != nil {
		v += recursive(node.Right.Left, visited) + recursive(node.Right.Right, visited)
	}
	val := max(v+node.Val, recursive(node.Left, visited)+recursive(node.Right, visited))
	visited[node] = val
	return val
}

func rob(root *TreeNode) int {
	visited := make(map[*TreeNode]int)
	return recursive(root, visited)
}

func main() {

	node := &TreeNode{Val: 3}
	//////
	node.Left = &TreeNode{Val: 2}
	node.Right = &TreeNode{Val: 3}
	node.Left.Left = nil
	node.Left.Right = &TreeNode{Val: 3}
	node.Right.Right = &TreeNode{Val: 1}

	fmt.Println(rob(node))
}
