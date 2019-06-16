
/*
 * 2. Add Two Numbers
 * https://leetcode.com/problems/add-two-numbers/
 * */


public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode(0);
        ListNode dummy = l3;
        int sum = 0;
        int carry = 0;
        int lval1 = 0;
        int lval2 = 0;

        while (l1 != null || l2 != null) {

            if (l1 == null) {
                lval1 = 0;
            } else {
                lval1 = l1.val;
            }

            if (l2 == null) {
                lval2 = 0;
            } else {
                lval2 = l2.val;
            }

            sum = lval1 + lval2 + carry;
            if (sum >= 10) {
                carry = sum / 10;
            } else {
                carry = 0;
            }

            l3.next = new ListNode(sum % 10);
            l3 = l3.next;
            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }

        if (carry > 0) {
            l3.next = new ListNode(carry);
        }
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2);
        ListNode l2 = new ListNode(4);
        ListNode l3 = new ListNode(3);
        ListNode l4 = new ListNode(5);
        ListNode l5 = new ListNode(6);
        ListNode l6 = new ListNode(4);
        ListNode l7 = new ListNode(8);

        l1.next = l2;
        l2.next = l3;

        l4.next = l5;
        l5.next = l6;
        l6.next = l7;

        Solution solution = new Solution();
        ListNode result = solution.addTwoNumbers(l1, l4);
        while (result != null) {
            System.out.println(result.val);
            result = result.next;
        }
    }
}
