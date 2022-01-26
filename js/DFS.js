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

  depthFirstSearchPreOrder() {
    return traversePreOrder(this.root, []);
  }
  depthFirstSearchPostOrder() {
    return traversePostOrder(this.root, []);
  }
  depthFirstSearchInOrder() {
    return traverseInOrder(this.root, []);
  }
}

function traversePreOrder(node, list) {
  list.push(node.value);
  if (node.left) {
    traversePreOrder(node.left, list);
  }
  if (node.right) {
    traversePreOrder(node.right, list);
  }
  return list;
}

function traversePostOrder(node, list) {
  if (node.left) {
    traversePostOrder(node.left, list);
  }
  if (node.right) {
    traversePostOrder(node.right, list);
  }
  list.push(node.value);
  return list;
}

function traverseInOrder(node, list) {
  if (node.left) {
    traverseInOrder(node.left, list);
  }
  list.push(node.value);
  if (node.right) {
    traverseInOrder(node.right, list);
  }
  return list;
}

const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
console.log(tree.depthFirstSearchInOrder());
// console.log(tree.depthFirstSearchPostOrder());
// console.log(tree.depthFirstSearchPreOrder());

//     9
//  4     20
//1  6  15  170

function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left || traverse(node.left);
  tree.right = node.right || traverse(node.right);
  return tree;
}
