
function main() {
  var t = parseInt(readLine());
  
  var swapper = function(index, array) {
    var temp = array[index];
    array[index] = array[index + 1];
    array[index + 1] = temp;
      //console.log('indexes swapped: ' + index);
  };

  var mergeSort = function(array) {
    var midpoint = Math.floor(array.length / 2);
    var leftHalf = array.slice(0, midpoint);
    var rightHalf = array.slice(midpoint);
  };
  
  // var mergeSort = function(array) {
  //   //var anySwaps = false;  
  //   for (var i = 0; i < array.length - 1; i++) {
  //     if (array[i] > array[i + 1]) {
  //       swapper(i, array);
  //       numSwaps++;
  //       anySwaps = true;
  //     }  
  //   }
  //   if (anySwaps) {
  //     mergeSort(array);  
  //   }  
  // };
  
  for (var a0 = 0; a0 < t; a0++) {
    var n = parseInt(readLine());
    arr = readLine().split(' ');
    arr = arr.map(Number);
    var numSwaps = 0;
    //console.log(arr)
    
    //mergeSort(arr);
    //console.log(numSwaps);
  }

}
