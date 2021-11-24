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
    let print = [currentNode.value];
    while (currentNode.next) {
      print.push(currentNode.next.value);
      currentNode = currentNode.next;
    }
    console.log(print.join("-->"));
    console.log("head", this.head);
    console.log("tail", this.tail);
  }

  // autopilot solution
  // reverse() {
  //   let currentNode = this.head;
  //   let previousNode = null;
  //   while (currentNode) {
  //     let nextNode = currentNode.next;
  //     currentNode.next = previousNode;
  //     previousNode = currentNode;
  //     currentNode = nextNode;
  //   }
  //   this.tail = this.head;
  //   this.head = previousNode;
  // }

  reverse() {
    let pointer1 = this.head;
    let pointer2 = this.head.next;
    let pointer3 = this.head.next.next;

    pointer1.next = null;
    this.head = pointer1;
    pointer2.next = pointer1;

    while (pointer3.next) {
      pointer1 = pointer2;
      pointer2 = pointer3;
      pointer3 = pointer3.next;

      pointer2.next = pointer1;
    }

    pointer3.next = pointer2;

    this.head = pointer3;
  }
}

const myLinkedList = new LinkedList(2);
myLinkedList.prepend(1);
myLinkedList.printOut();
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
myLinkedList.reverse();
myLinkedList.printOut();
