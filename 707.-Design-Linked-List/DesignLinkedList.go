// 707. Design Linked List
// https://leetcode.com/problems/design-linked-list/

package main

type MyNode struct {
	idx  int
	val  int
	prev *MyNode
	next *MyNode
}

type MyLinkedList struct {
	Length int
	head   *MyNode
	tail   *MyNode
}

/** Initialize your data structure here. */
func Constructor() MyLinkedList {
	return MyLinkedList{}
}

/** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
func (this *MyLinkedList) Get(index int) int {

	if this.head == nil {
		return -1
	}
	ptr := this.head.next
	for ptr != nil && ptr.idx > -1 {
		if ptr.idx == index {
			return ptr.val
		}
		ptr = ptr.next
	}
	return -1
}

/** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
func (this *MyLinkedList) AddAtHead(val int) {

	if this.head == nil {
		this.head = &MyNode{idx: -1}
		this.tail = &MyNode{idx: -1}
	}

	node := &MyNode{val: val}
	// 한번도 안들어왔을때
	if this.head.next == nil {
		node.idx = 0
		node.prev = this.head
		this.head.next = node
		this.tail.prev = node
		node.next = this.tail
	} else {
		temp := this.head.next

		for temp != nil && temp.idx > -1 {
			temp.idx += 1
			temp = temp.next
		}

		ptr := this.head.next
		ptr.prev = node
		node.next = ptr
		node.idx = 0
		this.head.next = node
	}

	this.Length += 1
}

/** Append a node of value val to the last element of the linked list. */
func (this *MyLinkedList) AddAtTail(val int) {
	if this.tail == nil {
		this.head = &MyNode{idx: -1}
		this.tail = &MyNode{idx: -1}
	}

	node := &MyNode{val: val, idx: this.Length}

	temp := this.tail.prev
	temp.next = node
	node.prev = temp

	node.next = this.tail
	this.tail.prev = node

	this.Length += 1
}

/** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
func (this *MyLinkedList) AddAtIndex(index int, val int) {

	if index == 0 {
		this.AddAtHead(val)
	} else if index == this.Length {
		this.AddAtTail(val)
	} else if index > this.Length {
		return
	} else {
		ptr := this.head.next
		node := &MyNode{val: val, idx: index}

		for ptr != nil {
			if ptr.idx == index {
				temp := ptr.prev
				temp.next = node
				node.prev = temp
				ptr.prev = node
				node.next = ptr
				break
			}
			ptr = ptr.next
		}

		for ptr != nil && ptr.idx > -1 {
			ptr.idx += 1
			ptr = ptr.next
		}

		this.Length += 1
	}
}

/** Delete the index-th node in the linked list, if the index is valid. */
func (this *MyLinkedList) DeleteAtIndex(index int) {
	ptr := this.head.next

	for ptr != nil {
		if ptr.idx == index {
			prev := ptr.prev
			next := ptr.next

			prev.next = next
			next.prev = prev
			this.Length -= 1
			break
		}
		ptr = ptr.next
	}

	for ptr != nil && ptr.idx > -1 {
		ptr.idx -= 1
		ptr = ptr.next
	}
}
