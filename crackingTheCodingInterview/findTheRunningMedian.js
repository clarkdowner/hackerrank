function main() {
  var n = parseInt(readLine());
  var a = [];
  var sorted = [];
  var even = true;
  

  // turn this into binarySearch for insert
  var sortHelper = function(newElement, sortedArray) {
    if (sortedArray.length === 0) {
      return [newElement];
    } else if (sortedArray[sortedArray.length - 1] < newElement) {
      sortedArray.push(newElement);
      return sortedArray;
    } else {
      for (var i = 0; i < sortedArray.length; i++) {
	      if (sortedArray[i] > newElement) {
          var first = sortedArray.slice(0, i);
          var second = sortedArray.slice(i);
          var newArray = first.push(newElement) + second;
          return newArray;
	      }
      }
    }      
  }
  
  for(var a_i = 0; a_i < n; a_i++){
    a[a_i] = parseInt(readLine());
    sorted = sortHelper(a[a_i], sorted);
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
