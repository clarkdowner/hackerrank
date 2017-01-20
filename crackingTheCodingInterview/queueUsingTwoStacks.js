function processData(input) {
  //Enter your code here
  
  var inputArray = input.split('\n');
  //console.log(inputArray);
  var queue = [];
  var index = 0;
  for (var i = 1; i < inputArray.length; i++) {
    if (inputArray[i] == 2) {
      index++;
    } else if (inputArray[i] == 3) {
      console.log(queue[index])
    } else {
      var value = inputArray[i].split(' ');
      queue.push(value[1]);
    }
  }

} 