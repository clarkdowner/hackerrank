
var heapSort = function(array) {
  if (array === undefined || array.length === 0) {
    return [];
  }

  var sorted = [];
  var Heap = {};
  Heap.root = null;
  Heap.heap = [];

  Heap.swap = function(a, b) {
    var temp = this.heap[a];
    this.heap[a] = this.heap[b];
    this.heap[b] = temp;
  }

  Heap.compareParent = function(childIndex) {
    if (childIndex === 0) { return; }

    var parentIndex = Math.floor((childIndex + 1) / 2) - 1;

    if (this.heap[childIndex] < this.heap[parentIndex]) {
      this.swap(childIndex, parentIndex);
      this.compareParent(parentIndex);
    }
  }

  Heap.compareChildren = function(parentIndex) {
    var leftChildIndex = ((parentIndex + 1) * 2) - 1;
    var rightChildIndex = (parentIndex + 1) * 2;

    if (this.heap[leftChildIndex] === undefined) {
      return;
    } else if (this.heap[rightChildIndex] === undefined || this.heap[leftChildIndex] <= this.heap[rightChildIndex]) {
      if (this.heap[leftChildIndex] < this.heap[parentIndex]) {
        this.swap(leftChildIndex, parentIndex);
        this.compareChildren(leftChildIndex);
      }
    } else {
      if (this.heap[rightChildIndex] < this.heap[parentIndex]) {
        this.swap(rightChildIndex, parentIndex);
        this.compareChildren(rightChildIndex);
      }
    }
  }

  Heap.addNode = function(val) {
    this.heap.push(val);

    if (this.heap.length > 1) {
      this.compareParent(this.heap.length - 1);
    }
  }

  Heap.popRoot = function() {    
    var rootVal = this.heap[0];
    var tail = this.heap.pop();

    if (this.heap.length > 0) {
      this.heap[0] = tail;
      this.compareChildren(0);
    }

    return rootVal;
  }

  //iterate through array
  for (var i = 0; i < array.length; i++) {
    //add each element to heap
    Heap.addNode(array[i]);
  }

  //while heap has elements
  while (Heap.heap.length > 0) {
    //pop root and add to return array;
    var sort = Heap.popRoot();
    sorted.push(sort);
  }

  return sorted;
}

// ------

var assert = function(a, b) {
	var same = true;
	if (a.length !== b.length) {
		same = false;
	} 
	for (var i = 0; same && i < a.length; i++) {
		if (a[i] !== b[i]) {
			same = false;
		}
	}
	if (same) {console.log('success');}
	else {console.log('Expected ' + a + ' to equal ' + b);}
}

// test cases: 
var test1 = [1,2,3,4,5];
var test2 = [5,4,3,2,1];
var test3 = [];
var test4 = [1,1,1,1,1];
var test5 = [1,2,3,4,5,6,7,8];
var test6 = [1,2,6,5,4,3,7,8];
var test7 = [4,2,7,1,8,5,6,3];
var test8 = [1];
var test9 = [1,0];
var test10 = [0,1]
assert(heapSort(test1), [1,2,3,4,5]);
assert(heapSort(test2), [1,2,3,4,5]);
assert(heapSort(test3), []);
assert(heapSort(test4), [1,1,1,1,1]);
assert(heapSort(test5), [1,2,3,4,5,6,7,8]);
assert(heapSort(test6), [1,2,3,4,5,6,7,8]);
assert(heapSort(test7), [1,2,3,4,5,6,7,8]);
assert(heapSort(test8), [1]);
assert(heapSort(test9), [0,1]);
assert(heapSort(test10), [0,1]);
