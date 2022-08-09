function Node(data) {
    this.data = data;
    this.next = null;
  }


function insertNth(head, index, data) {
    // Your code goes here.
    // Return the head of the list.

    let myHead = head;
    const newNode = new Node(data);
    if(!myHead){
        myHead = newNode;
    }
    for(let i=0;i<=index-1;i++){
        myHead = myHead.next;
    }
    myHead.next= newNode;
    newNode.next = myHead.next
    return myHead;
}