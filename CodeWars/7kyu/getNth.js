function Node(data) {
    this.data = data;
    this.next = null;
  }
  
  function getNth(node, index) {
    // Your code goes here.
    if(!node) throw new Error('Invalid index value should throw error.')
    return index === 0 ? node : getNth(node.next,index-1);
  }
  