// 641. Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

// TODO
// 이 문제의 문제점은... circular-deque 인데 circular 를 검증할 함수가 없다는 것
// 우선 accepted 되었지만, 검증이 필요함

package main

type node struct {
	val  int
	prev *node
	next *node
}

type MyCircularDeque struct {
	length int
	size   int
	front  *node
	last   *node
}

/** Initialize your data structure here. Set the size of the deque to be k. */
func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{size: k, length: 0}
}

/** Adds an item at the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertFront(value int) bool {

	newNode := &node{val: value}

	if this.length == 0 && this.size > 0 {
		this.front = newNode
		this.last = newNode
	} else if this.length >= this.size {
		return false
	} else {
		temp := this.front
		newNode.next = temp
		temp.prev = newNode
		this.front = newNode
		this.last.next = this.front
		this.front.prev = this.last
	}
	this.length += 1
	return true
}

/** Adds an item at the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) InsertLast(value int) bool {
	newNode := &node{val: value}
	if this.length == 0 && this.size > 0 {
		this.front = newNode
		this.last = newNode
	} else if this.length >= this.size {
		return false
	} else {
		temp := this.last
		temp.next = newNode
		newNode.prev = temp
		this.last = newNode
		this.last.next = this.front
		this.front.prev = this.last
	}
	this.length += 1
	return true
}

/** Deletes an item from the front of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteFront() bool {
	if this.length == 0 {
		return false
	}

	if this.length == 1 {
		this.front = nil
		this.last = nil
		this.length -= 1
		return true
	}

	temp := this.front
	this.front = temp.next
	this.last.next = this.front
	this.front.prev = this.last
	this.length -= 1
	return true
}

/** Deletes an item from the rear of Deque. Return true if the operation is successful. */
func (this *MyCircularDeque) DeleteLast() bool {
	if this.length == 0 {
		return false
	}

	if this.length == 1 {
		this.front = nil
		this.last = nil
		this.length -= 1
		return true
	}

	temp := this.last
	this.last = temp.prev
	this.last.next = this.front
	this.front.prev = this.last
	this.length -= 1
	return true
}

/** Get the front item from the deque. */
func (this *MyCircularDeque) GetFront() int {
	if this.length == 0 {
		return -1
	}
	return this.front.val
}

/** Get the last item from the deque. */
func (this *MyCircularDeque) GetRear() int {
	if this.length == 0 {
		return -1
	}
	return this.last.val

}

/** Checks whether the circular deque is empty or not. */
func (this *MyCircularDeque) IsEmpty() bool {
	return this.length == 0
}

/** Checks whether the circular deque is full or not. */
func (this *MyCircularDeque) IsFull() bool {
	return this.length == this.size
}
