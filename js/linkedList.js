// constructor
class LinkedList {
  constructor(value) {
    this.head = { value, next: null };
    this.tail = this.head;
    this.length = 1;
  }
  append(value) {
    this.tail.next = { value, next: null };
    this.tail = this.tail.next;
    this.length++;
  }

  prepend(value) {
    const newNode = { value, next: this.head };
    this.head = newNode;
    this.length++;
  }

  insert(index, value) {
    const newNode = { value, next: null };
    if (index >= this.length - 1) {
      this.append(value);
    }
    if (index === 0) {
      this.prepend(value);
    }
    let i = 1;
    let previousNode = this.nodeAtIndex(index - 1);
    newNode.next = previousNode.next;
    previousNode.next = newNode;
  }

  delete(index) {
    if (index === 0) {
      this.head = this.head.next;
      this.length--;
      return;
    }
    if (index >= this.length - 1) {
      let previousNode = this.nodeAtIndex(this.length - 2);
      previousNode.next = null;
      this.tail = previousNode;
    } else {
      let previousNode = this.nodeAtIndex(index - 1);
      previousNode.next = previousNode.next.next;
    }
    this.length--;
  }

  nodeAtIndex(index) {
    if (index >= this.length - 1) {
      return this.tail;
    }

    let i = 0;
    let currentNode = this.head;
    while (i !== index) {
      currentNode = currentNode.next;
      i++;
    }
    return currentNode;
  }

  printOut() {
    let currentNode = this.head;
    let print = [];
    while (currentNode.next) {
      print.push(currentNode.next.value);
      currentNode = currentNode.next;
    }
    console.log(print.join("-->"));
  }
}

const myLinkedList = new LinkedList(2);
myLinkedList.prepend(1);
myLinkedList.append(4);
myLinkedList.append(7);
myLinkedList.append(8);
myLinkedList.prepend(0);
myLinkedList.insert(1, 1.5);
myLinkedList.insert(3, 5);
myLinkedList.insert(13, 5);
myLinkedList.printOut();
myLinkedList.delete(0);
myLinkedList.printOut();
