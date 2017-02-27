// <!-- Matrix Sum -> find the max sum where each element is the only one in its row and column

//  7      53    183    439   863x
// 497    383x    563    79    973
// 287    63     343x    169   583
// 627    343    773    959x   943
// 767x    473    103    699   303
//  -->

function findIndMax(matrix) {
  var max = 0;

  // map over each element
  matrix.map(function(row) {
    row.map(function(elem) {
      max = elem > max ? elem : max;
    })
  })

  return max;
}

function inMarked(array, target) {
  return array.indexOf(target) !== -1 ? true : false;
}

function findBalance(markedRows, markedCols, matrix) {
  var min = Infinity;

  matrix.map(function(row, rowIndex) {
    if (inMarked(markedRows, rowIndex)) {
      row.map(function(elem, colIndex) {
        if (!inMarked(markedCols, colIndex)) {
          min = elem < min ? elem : min;
        }
      })
    }
  })

  return min;
}

function reduceMaxFromOrig(matrix, max) {
  var reducedMatrix = [];

  matrix.map(function(row, i) {
    reducedMatrix.push([]);
    row.map(function(elem) {
      reducedMatrix[i].push(max - elem);
    })
  })

  return reducedMatrix;
}

function reduceHorizontally(matrix) {
  var reducedSum = 0;

  // for each row
  matrix.map(function(row) {
    var rowMin = row.reduce(function(acc, elem) {
      return elem < acc ? elem : acc;
    })

    reduceSingleRow(row, rowMin); // intentional mutation
    reducedSum += rowMin;
  })

  return reducedSum;
}

function reduceSingleRow(row, min) {
  row.map(function(elem, i) {
    row[i] = elem - min;
  })
}

function reduceVertically(matrix) {
  var reducedSum = 0;

  matrix[0].map(function(_elem, colIndex) {
    // for each column
    var colMin = matrix[colIndex].reduce(function(acc, _row, rowIndex) {
      var elem = matrix[rowIndex][colIndex]
      return elem < acc ? elem : acc;
    }, Infinity)

    reduceSingleColumn(matrix, colIndex, colMin); // intentional mutation
    reducedSum += colMin
  })

  return reducedSum;
}

function reduceSingleColumn(matrix, colIndex, min) {
  matrix.map(function(_row, rowIndex) {
    matrix[rowIndex][colIndex] = matrix[rowIndex][colIndex] - min;
  })
}


function canAssign(matrix) {
  var assignedIndexes = {}; // col: row
  var markedRows = [];
  var markedCols = [];

  var markBoard = function() {
    // TODO: refactor with inMarked
    var markRow = function(rowNum) {
      if (markedRows.indexOf(rowNum) === -1) {
        markedRows.push(rowNum)
        return true;
      }
      return false;
    }
    var markCol = function(colNum) {
      if (markedCols.indexOf(colNum) === -1) {
        markedCols.push(colNum)
        return true;
      }
      return false;
    }
    var recursiveMarkRow = function(rowNum) {
      var row = matrix[rowNum];
      // Mark all (unmarked) columns having zeros in newly marked row(s)
      row.map(function(elem, colIndex) {
        if (elem === 0 && markCol(colIndex)) { 
          recursiveMarkCol(colIndex);
        }
      })
    }
    var recursiveMarkCol = function(colNum) {
      if (assignedIndexes[colNum] === undefined) {
        return;
      }
      var rows = assignedIndexes[colNum];
      rows.map(function(rowIndex) {
        if (markRow(rowIndex)) {
          recursiveMarkRow(rowIndex);
        }
      })
    }

    matrix.map(function(row, rowIndex) {
      var zeroIndexes = [];
      row.map(function(elem, colIndex) {
        if (elem === 0 && assignedIndexes[colIndex] === undefined) {
          zeroIndexes.push(colIndex);
        }
      })
      for (var i = 0; i < zeroIndexes.length; i++) {
        var column = zeroIndexes[i];
        if (assignedIndexes[column] === undefined) {
          assignedIndexes[column] = [rowIndex];
        } else {
          assignedIndexes[column] = assignedIndexes[column].push(rowIndex);
        }
      }
      // Mark all rows having no assignments 
      if (zeroIndexes.length === 0) {
        markRow(rowIndex);
        recursiveMarkRow(rowIndex);
      }
    })
  }

  markBoard();

  if (markedCols.length === markedRows.length) {
    return true;
  } else {
    return false;
  }
}

function markAndRedraw(matrix) {
  var assignedIndexes = {}; // col: row
  var markedRows = [];
  var markedCols = [];

  var markBoard = function() {
    // TODO: refactor with inMarked
    var markRow = function(rowNum) {
      if (markedRows.indexOf(rowNum) === -1) {
        markedRows.push(rowNum)
        return true;
      }
      return false;
    }
    var markCol = function(colNum) {
      if (markedCols.indexOf(colNum) === -1) {
        markedCols.push(colNum)
        return true;
      }
      return false;
    }
    var recursiveMarkRow = function(rowNum) {
      var row = matrix[rowNum];
      // Mark all (unmarked) columns having zeros in newly marked row(s)
      row.map(function(elem, colIndex) {
        if (elem === 0 && markCol(colIndex)) { 
          recursiveMarkCol(colIndex);
        }
      })
    }
    var recursiveMarkCol = function(colNum) {
      if (assignedIndexes[colNum] === undefined) {
        return;
      }
      var rows = assignedIndexes[colNum];
      rows.map(function(rowIndex) {
        if (markRow(rowIndex)) {
          recursiveMarkRow(rowIndex);
        }
      })
    }

    matrix.map(function(row, rowIndex) {
      var zeroIndexes = [];
      row.map(function(elem, colIndex) {
        if (elem === 0 && assignedIndexes[colIndex] === undefined) {
          zeroIndexes.push(colIndex);
        }
      })
      for (var i = 0; i < zeroIndexes.length; i++) {
        var column = zeroIndexes[i];
        if (assignedIndexes[column] === undefined) {
          assignedIndexes[column] = [rowIndex];
        } else {
          assignedIndexes[column] = assignedIndexes[column].push(rowIndex);
        }
      }
      // Mark all rows having no assignments 
      if (zeroIndexes.length === 0) {
        markRow(rowIndex);
        recursiveMarkRow(rowIndex);
      }
    })
  }

  var redrawBoard = function(amt) {
    matrix.map(function(row, rowIndex) {
      row.map(function(elem, colIndex) {
        if (!inMarked(markedRows, rowIndex) && inMarked(markedCols, colIndex)) {
          matrix[rowIndex][colIndex] = elem + amt;
        } else if (inMarked(markedRows, rowIndex) && !inMarked(markedCols, colIndex)) {
          matrix[rowIndex][colIndex] = elem - amt;
        }
      })
    })
  }

  markBoard();
  var balance = findBalance(markedRows, markedCols, matrix);
  redrawBoard(balance);

  return balance;
}

function findMaxReturnPositions(matrix) {
  var positions = new Set();
  var columnsClaimed = [];
  var rowsClamined = [];

  console.log('matrix: ', matrix)
  var count = 0;
  while (positions.size < matrix.length && count < 20) {
  	count++;
    // console.log(positions.size)
    matrix.map(function(row, rowIndex) {
      if (rowsClamined.indexOf(rowIndex) === -1) {
        var zeroIndexes = [];
        row.map(function(elem, colIndex) {
          if (elem === 0 && columnsClaimed.indexOf(colIndex) === -1) {
            zeroIndexes.push(colIndex);
          }
        })
        if (zeroIndexes.length === 1) {
          columnsClaimed.push(zeroIndexes[0]);
          rowsClamined.push(rowIndex);
          // add to set
          positions.add([rowIndex, zeroIndexes[0]])
        }
      }
    })
  }

  return positions;
}

function addMaxPositions(matrix, positions) {
  var sum = 0;

  positions.forEach(function(tuple) {
    var amt = matrix[tuple[0]][tuple[1]];
    sum += amt;
  })

  return sum;
}

function findMatrixSum(origMatrix) {
  // initialize maxSum
  var maxSum = 0;

  // find individual max
  var indMax = findIndMax(origMatrix);

  // reduce all values from max
  var matrix = reduceMaxFromOrig(origMatrix, indMax);
  // console.log('matrix: ', matrix);
  // maxSum += indMax;

  // reduce horizontally
  reduceHorizontally(matrix); // intentional mutation
  // console.log('matrix: ', matrix);
  // reduce vertically
  reduceVertically(matrix); // intentional mutation
  console.log('matrix: ', matrix);
  // while !canAssign
  while (!canAssign(matrix)) {
    markAndRedraw(matrix);
    console.log('redraw')
  }

  // var set = findMaxReturnPositions(matrix);
  // console.log('set: ', set)

  // return addMaxPositions(origMatrix, set);
}
 
var board =   [[7,  53, 183, 439, 863],
[497, 383, 563,  79, 973],
[287,  63, 343, 169, 583],
[627, 343, 773, 959, 943],
[767, 473, 103, 699, 303]]
 
var answerBoard1 = 3315

var board2 = [[7,  53, 183, 439, 863, 497, 383, 563,  79, 973, 287,  63, 343, 169, 583],[627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
[447, 283, 463,  29,  23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
[217, 623,   3, 399, 853, 407, 103, 983,  89, 463, 290, 516, 212, 462, 350],
[960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
[870, 456, 192, 162, 593, 473, 915,  45, 989, 873, 823, 965, 425, 329, 803],
[973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
[322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601,  95, 973],
[445, 721,  11, 525, 473,  65, 511, 164, 138, 672,  18, 428, 154, 448, 848],
[414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
[184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
[821, 461, 843, 513,  17, 901, 711, 993, 293, 157, 274,  94, 192, 156, 574],
[34, 124,   4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
[815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
[813, 883, 451, 509, 615,  77, 281, 613, 459, 205, 380, 274, 302,  35, 805]]

// console.log(findMatrixSum(board) === 3315)
console.log(findMatrixSum(board2) === 13938)
// console.log(findMatrixSum(board))