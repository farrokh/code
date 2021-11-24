class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }
  enqueue(value) {
    const newValue = new Node(value);
    if (this.first === null) {
      this.first = newValue;
      this.last = newValue;
    } else {
      this.last.next = newValue;
      this.last = newValue;
    }
    this.size++;
  }
  dequeue() {
    if (this.first === null) return null;
    const value = this.first.value;
    this.first = this.first.next;
    this.size--;
    return value;
  }
  peek() {
    if (this.first === null) return null;
    return this.first.value;
  }
  isEmpty() {
    return this.size === 0;
  }
}
