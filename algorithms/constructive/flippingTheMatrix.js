function processData(input) {
  // input is string
  // split input on spaces
  var input = input.split(' ');
  // first input is how many matrices
  // for how many matrices
  var i = 1;
  while (i <= input[0]) {
    // size = Math.pow((size * 2), 2);
    var matrixSize = input[i] * 2;
    i += 1;
    // matrix = slice at current index, size
    var matrix = input.slice(i, i + matrixSize);

    for (var x = 0; x < matrixSize; x++) {
      matrix[x] = matrix[x].split(' ');
    }

    var maxSum = 0;
    // take max at each position
    for (var row = 0; row < matrixSize / 2; row++) {
      for (var col = 0; col < matrixSize / 2; col++) {
        var max = Math.max(matrix[row][col], matrix[matrixSize - 1 - row][col], matrix[row][matrixSize - 1 - col], matrix[matrixSize - 1 - row][matrixSize - 1 - col]);
        maxSum += max;
      }
    }
    console.log(maxSum);

    // i plus size of matrix
    i += matrixSize;

  }
}


