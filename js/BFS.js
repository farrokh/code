class Node {
  constructor(value) {
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(value) {
    const newNode = new Node(value);
    if (this.root === null) {
      this.root = newNode;
    } else {
      let pointer = this.root;
      while (pointer !== null) {
        if (value > pointer.value) {
          if (pointer.right) {
            pointer = pointer.right;
          } else {
            pointer.right = newNode;
            break;
          }
        } else {
          if (pointer.left) {
            pointer = pointer.left;
          } else {
            pointer.left = newNode;
            break;
          }
        }
      }
      pointer = newNode;
    }
  }
  create(values) {
    for (let i = 0; i < values.length; i++) {
      this.insert(values[i]);
    }
  }
  lookup(value) {
    if (this.root === null) {
      return null;
    }
    let pointer = this.root;
    while (pointer) {
      if (value === pointer.value) {
        return pointer;
      }

      if (value > pointer.value) {
        pointer = pointer.right;
      } else {
        pointer = pointer.left;
      }
    }
    return null;
  }

  breadthFirstTree() {
    let pointer = this.root;
    let list = [];
    let queue = [];
    queue.push(pointer);
    while (queue.length > 0) {
      pointer = queue.shift();
      list.push(pointer.value);
      if (pointer.left) {
        queue.push(pointer.left);
      }
      if (pointer.right) {
        queue.push(pointer.right);
      }
    }
    return list;
  }

  breadthFirstTreeRecursive(queue, list) {
    if (!queue.length) {
      return list;
    }
    let pointer = queue.shift();
    list.push(pointer.value);
    if (pointer.left) {
      queue.push(pointer.left);
    }
    if (pointer.right) {
      queue.push(pointer.right);
    }
    return this.breadthFirstTreeRecursive(queue, list);
  }

  isValidBST() {
    return this.isValidBSTHelper(this.root);
  }

  isValidBSTHelper(node) {
    if (node === null) {
      return;
    }
    if (node.left && node.left.value > node.value) {
      return false;
    }
    if (node.right && node.right.value < node.value) {
      return false;
    }
    return (
      this.isValidBSTHelper(node.left) && this.isValidBSTHelper(node.right)
    );
  }

  remove(value) {
    if (!this.root) {
      return false;
    }
    let currentNode = this.root;
    let parentNode = null;
    while (currentNode) {
      if (value < currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.left;
      } else if (value > currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.right;
      } else if (currentNode.value === value) {
        //We have a match, get to work!

        //Option 1: No right child:
        if (currentNode.right === null) {
          if (parentNode === null) {
            this.root = currentNode.left;
          } else {
            //if parent > current value, make current left child a child of parent
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.left;

              //if parent < current value, make left child a right child of parent
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.left;
            }
          }

          //Option 2: Right child which doesnt have a left child
        } else if (currentNode.right.left === null) {
          currentNode.right.left = currentNode.left;
          if (parentNode === null) {
            this.root = currentNode.right;
          } else {
            //if parent > current, make right child of the left the parent
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.right;

              //if parent < current, make right child a right child of the parent
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.right;
            }
          }

          //Option 3: Right child that has a left child
        } else {
          //find the Right child's left most child
          let leftmost = currentNode.right.left;
          let leftmostParent = currentNode.right;
          while (leftmost.left !== null) {
            leftmostParent = leftmost;
            leftmost = leftmost.left;
          }

          //Parent's left subtree is now leftmost's right subtree
          leftmostParent.left = leftmost.right;
          leftmost.left = currentNode.left;
          leftmost.right = currentNode.right;

          if (parentNode === null) {
            this.root = leftmost;
          } else {
            if (currentNode.value < parentNode.value) {
              parentNode.left = leftmost;
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = leftmost;
            }
          }
        }
        return true;
      }
    }
  }
}

const tree = new BinarySearchTree();
// tree.insert(9);
// tree.insert(4);
// tree.insert(6);
// tree.insert(20);
// tree.insert(170);
// tree.insert(15);
// tree.insert(1);
tree.create([5, 1, 4, null, null, 3, 6]);
console.log(tree.isValidBST());

//     9
//  4     20
//1  6  15  170

function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left || traverse(node.left);
  tree.right = node.right || traverse(node.right);
  return tree;
}
