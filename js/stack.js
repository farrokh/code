class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

// class Stack {
//   constructor() {
//     this.top = null;
//     this.bottom = null;
//     this.length = 0;
//   }
//     peek() {
//         return this.top;
//     }
//     push(value) {
//         const newNode = new Node(value);
//         if (this.length === 0) {
//             this.top = newNode;
//             this.bottom = newNode;
//         } else {
//             const holdingPointer = this.top;
//             this.top = newNode;
//             this.top.next = holdingPointer;
//         }
//         this.length++;
//         return this;
//     }
//     pop() {
//         if (this.length === 0) {
//             return undefined;
//         }
//         const holdingPointer = this.top;
//         this.top = this.top.next;
//         this.length--;
//         if (this.length === 0) {
//             this.bottom = null;
//         }
//         return holdingPointer;
//     }
// }

class Stack {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }
  peek() {
    return this.top;
  }
  push(value) {
    const newNode = new Node(value);
    if (this.length === 0) {
      this.top = newNode;
    } else {
      newNode.next = this.top;
      this.top = newNode;
      this.length++;
    }
    return this;
  }
  pop() {
    if (this.length === 0) {
      return "nothing to pop";
    }
    if (this.length === 1) {
      this.top = null;
      this.bottom = null;
      this.length--;
    }
    this.top = this.top.next;
    this.length--;
    return this;
  }
  isEmpty() {
    return !!this.length;
  }
}

const myStack = new Stack();
console.log(myStack.push(1));
