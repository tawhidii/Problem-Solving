function Node(data) {
    this.data = data;
    this.next = null;
  }
  
  function push(head, data) {
    let new_node = new Node(data);
    new_node.next = head;
    return new_node;
  }
  
  function buildOneTwoThree() {
    let myList = null;
    myList = push(myList,3);
    myList = push(myList,2);
    myList = push(myList,1);
    return myList;
  }

  console.log(buildOneTwoThree())