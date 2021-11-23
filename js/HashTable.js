class HashTable {
  constructor(size) {
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = (hash + key.charCodeAt(i) * i) % this.data.length;
    }
    return hash;
  }

  set(key, value) {
    let index = this._hash(key);
    if (!this.data[index]) {
      this.data[index] = [];
    }
    this.data[index] = [key, value];
    return this.data[index];
  }

  get(key) {
    let index = this._hash(key);
    if (this.data[index]) {
      for (let i = 0; i < this.data[index].length; i++) {
        if (this.data[index][i][0] === key) {
          return this.data[index][i][1];
        }
      }
      // or using map to return the value
      // this.data[index].map((item) => {
      //   if (item[0] === key) {
      //     return item[1];
      //   }
      // }
      // );
    }
    return undefined;
  }

  keys() {
    for (let index = 0; index < this.data.length; index++) {
      const element = this.data[index];
      for (let j = 0; j < element.length; j++) {
        return element[j][0];
      }
    }
  }
}

const myHashTable = new HashTable(50);
myHashTable.set("grapes", 10000);
myHashTable.get("grapes");
myHashTable.set("apples", 9);
myHashTable.get("apples");
