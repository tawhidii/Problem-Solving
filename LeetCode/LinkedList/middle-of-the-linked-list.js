/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var middleNode = function(head) {
    let count = 0;
    let keepHead = head;
    while(keepHead){
        count++;
        keepHead = keepHead.next;
    }
    let anotherCount = 0;
    const middle = Math.floor(count/2);
    while(anotherCount<middle){
        head = head.next;
        anotherCount++;
    }
    return head;
};