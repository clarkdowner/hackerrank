function main() {
  var n = parseInt(readLine());
  var a = [];
  var sorted = [];
  var even = true;
  

  // // turn this into binarySearch for insert
  // var sortHelper = function(newElement, sortedArray) {
  //   if (sortedArray.length === 0) {
  //     return [newElement];
  //   } else if (sortedArray[sortedArray.length - 1] < newElement) {
  //     sortedArray.push(newElement);
  //     return sortedArray;
  //   } else {
  //     for (var i = 0; i < sortedArray.length; i++) {
	 //      if (sortedArray[i] > newElement) {
  //         var first = sortedArray.slice(0, i);
  //         var second = sortedArray.slice(i);
  //         var newArray = first.push(newElement) + second;
  //         return newArray;
	 //      }
  //     }
  //   }      
  // }
  var findIndex = function(element, array) {
    var lowerBound = 0;
    var upperBound = array.length - 1;
    var searchAt = Math.floor((upperBound - lowerBound) / 2);


    while (element < array[searchAt - 1] || element > array[searchAt]) {
      if (element < array[searchAt - 1]) {
        upperBound = searchAt;
      } else {
        lowerBound = searchAt;
      }
      searchAt = Math.floor((upperBound - lowerBound) / 2);
    }
    return searchAt;
  }

  var insert = function(index, array, element) {
    var first = array.slice(0, index);
    var second = array.slice(index);
    return first.push(element) + second;
  }
  
  for (var i = 0; i < n; i++) {
    a[i] = parseInt(readLine());
    //sorted = sortHelper(a[i], sorted);
    // find index to insert
    var index = findIndex(a[i], sorted)
    // insert at index
    insert(index, sorted, a[i]);
    even = !even;
    
    if (even) {
      var one = sorted[sorted.length / 2];
      var two = sorted[(sorted.length / 2) - 1];
      if (one + two % 2 === 0) {
        console.log(one + two / 2 + '.0');
      } else {
        console.log((one + two) / 2);
      }
    } else {
      console.log(sorted[Math.floor(sorted.length / 2)] + '.0');
    }
  }
}
