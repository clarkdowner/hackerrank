
function main() {
  var t = parseInt(readLine());
  var numSwaps = 0;

  var mergeHalves = function(array, leftHalf, rightHalf, leftStart, rightEnd) {
    // var midpoint = Math.floor((leftStart + rightEnd) / 2);
    // var leftEnd = midpoint - 1;
    // var rightStart = midpoint;

    // var left = leftStart;
    // var right = rightStart;
    // var index = leftStart;
    var temp = [];
    var left = 0;
    var right = 0;
    var index = 0;

    while (left <= leftHalf.length || right <= rightHalf.length) {
      if (rightHalf[right] === undefined || leftHalf[left] <= rightHalf[right]) {
        temp[index] = leftHalf[left];
        left++;
      } else {
        temp[index] = rightHalf[right];
        right++;
      }
      index++;
    }

    // while (left <= leftEnd || right <= rightEnd) {
    //   if (array[left] <= array[right] || array[right] === undefined) {
    //     temp[index] = array[left];
    //     left++;
    //   } else {
    //     temp[index] = array[right];
    //     right++;
    //   }
    //   index++;  
    // }

    for (var i = leftStart; i <= rightEnd; i++) {
      if (array[i] !== temp[i]) {
        numSwaps++;
      }
      array[i] = temp[i];
    }
  }

  var mergeSort = function(array, leftStart, rightEnd) {
    if (array.length === 1) {
      return array;
    }
    var leftStart = leftStart || 0;
    var midpoint = Math.floor(array.length / 2);
    var leftHalf = array.slice(0, midpoint);
    var rightHalf = array.slice(midpoint + 1);
    // var leftStart = leftStart || 0;
    // var rightEnd = rightEnd || array.length - 1;
    // if (leftStart >= rightEnd) {
    //   return;
    // }
    // var midpoint = Math.floor((leftStart + rightEnd)/ 2);
    // var leftEnd = midpoint - 1;
    // var rightStart = midpoint;
    mergeSort(leftHalf, midpoint - leftHalf.length, midpoint);
    mergeSort(rightHalf, midpoint + 1, midpoint + 1 + rightHalf.length);
    mergeHalves(array, leftHalf, rightHalf, midpoint - leftHalf.length, midpoint + 1 + rightHalf.length);

    // mergeSort(array, temp, leftStart, leftEnd);
    // mergeSort(array, temp, rightStart, rightEnd);
    // mergeHalves(array, temp, leftStart, rightEnd);
  };
  
  for (var a0 = 0; a0 < t; a0++) {
    var n = parseInt(readLine());
    arr = readLine().split(' ');
    arr = arr.map(Number);
    //console.log(arr)
    
    mergeSort(arr);
    //console.log(numSwaps);
  }
}
