function main(grid) {
  var maxN = parseInt(readLine());
  var maxM = parseInt(readLine());
  var grid = [];
  for(grid_i = 0; grid_i < maxN; grid_i++){
    grid[grid_i] = readLine().split(' ');
    grid[grid_i] = grid[grid_i].map(Number);
  }

  // var maxN = grid.length;
  // var maxM = grid[0].length;

  var search = function(i, j) {
    // debugger;
    var size = 0;
    if (grid[i][j] === 1) {
      size++;
      grid[i][j] = 0;
    }

    if (i > 0 && grid[i - 1][j] === 1) {
      size += search(i - 1, j);
    }
    if (j > 0 && grid[i][j - 1] === 1) {
      size += search(i, j - 1);
    }
    if (grid[i + 1] !== undefined && grid[i + 1][j] === 1) {
    // if (i < maxN && grid[i + 1][j] === 1) {
      size += search(i + 1, j);
    }
    if (j < maxM && grid[i][j + 1] === 1) {
      size += search(i, j + 1);
    }

    return size;
  }


  var largestBlock = 0;

  for (var i = 0; i < maxN; i++) {
    for (var j = 0; j < maxM; j++) {
      var currBlock = 0;
      if (grid[i][j] === 1) {
        currBlock += search(i, j, 0);
      }
      if (currBlock > largestBlock) {
        largestBlock = currBlock;
      }
    }
  }

  console.log(largestBlock);
}


// testCase = [[1,1,0,0],[0,1,1,0],[0,0,1,0,],[1,0,0,0]];

// main(testCase);