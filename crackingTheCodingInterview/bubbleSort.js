
function main() {
  var n = parseInt(readLine());
  a = readLine().split(' ');
  a = a.map(Number);
  
  var swap = function(firstIndex, secondIndex, arrayToSwap) {
    var array = arrayToSwap || a;
    var secondIndex = secondIndex || firstIndex + 1;
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
  }
  
  var numSwaps = 0;
  
  var sortArray = function(array) {
    var anySwaps = false;
    for (var i = 0; i < array.length - 1; i++) {
      if (array[i] > array[i + 1]) {
        swap(i, i + 1, array);
        anySwaps = true;
        numSwaps++;
      }
    }
    if (anySwaps) {
      sortArray(array);
    }
  }
  sortArray(a);
  
  console.log('Array is sorted in ' + numSwaps + ' swaps.')
  console.log('First Element: ' + a[0]);
  console.log('Last Element: ' + a[a.length - 1]);
}
