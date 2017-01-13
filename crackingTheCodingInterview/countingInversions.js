function main() {
    var t = parseInt(readLine());
    
    var swapper = function(index, array) {
      var temp = array[index];
      array[index] = array[index + 1];
      array[index + 1] = temp;
        //console.log('indexes swapped: ' + index);
    };
    
    var sortArray = function(array) {
      var anySwaps = false;  
      for (var i = 0; i < array.length - 1; i++) {
        if (array[i] > array[i + 1]) {
          swapper(i, array);
          numSwaps++;
          anySwaps = true;
        }  
      }
      if (anySwaps) {
        sortArray(array);  
      }  
    };
    
    for(var a0 = 0; a0 < t; a0++){
        var n = parseInt(readLine());
        arr = readLine().split(' ');
        arr = arr.map(Number);
        var numSwaps = 0;
        
        sortArray(arr);
        console.log(numSwaps);
    }

}