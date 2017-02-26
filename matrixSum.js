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
    })

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

function canAssign(matrix, assignedIndexes = []) {
  var assignments = 0;

  matrix.map(function(row, sliceAt) {
    zeroIndexes = [];
    row.map(function(elem, index) {
      if (elem === 0 && assignedIndexes.indexOf(index) === -1) {
        zeroIndexes.push(index);
      }
    })

    if (zeroIndexes.length === 0) {
      return false;
    } else if (zeroIndexes.length === 1) {
      assignments++;
      assignedIndexes = assignedIndexes.concat(zeroIndexes);
    } else {
      return zeroIndexes.reduce(function(acc, elem) {
        var tempAssign = zeroIndexes.concat([elem]);
        return acc || canAssign(matrix.slice(sliceAt + 1), tempAssign);
      }, false)
    }
  })

  return assignments === matrix.length ? true : false;
}

function markBoard(matrix) {
  var assignedIndexes = {}; // index: row
  var markedRows = [];
  var markedCols = [];

  var markRow = function(rowNum) {
    if (markedRows.indexOf(rowNum) === -1) {
      markedRows.push(rowNum)
    }
  }
  var markCol = function(colNum) {
    if (markedCols.indexOf(colNum) === -1) {
      markedCols.push(colNum)
    }
  }

  matrix.map(function(row, rowIndex) {
    // console.log('called')
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
    // Mark all rows having no assignments (row 3).
    if (zeroIndexes.length === 0) {
      markRow(rowIndex);
      row.map(function(elem, colIndex) {
      // Mark all (unmarked) columns having zeros in newly marked row(s) (column 1).
        if (elem === 0) { markCol(colIndex); }
      })
    }
    // console.log("numAssigments: ", zeroIndexes.length)
  })
  // Mark all rows having assignments in newly marked columns (row 1).
  for (var i = 0; i < markedCols.length; i++) {
    var col = markedCols[i];
    for (var j = 0; j < assignedIndexes[col].length; j++) {
      var row = assignedIndexes[col][j];
      markRow(row);
    }
  }

  console.log('markedRows: ', markedRows);
  console.log('markedCols: ', markedCols);
}

function findMatrixSum(origMatrix) {
  // initialize maxSum
  var maxSum = 0;

  // find individual max
  var indMax = findIndMax(origMatrix);

  // reduce all values from max
  var matrix = reduceMaxFromOrig(origMatrix, indMax);
  // console.log(matrix)

  maxSum += indMax;
  // console.log('maxSum: ', maxSum)

  // reduce horizontally
  maxSum += reduceHorizontally(matrix); // intentional mutation
  // console.log(matrix)
  // console.log('maxSum: ', maxSum)

  // reduce vertically
  maxSum += reduceVertically(matrix); // intentional mutation
  console.log(matrix)
  // console.log('maxSum: ', maxSum)

  // while !canAssign
  while (!canAssign(matrix)) {
    // balance and redraw board
    markBoard(matrix);
    return maxSum;

  }

  return maxSum;
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

console.log(findMatrixSum(board) === 3315)
// console.log(findMatrixSum(board2) === 13938)
