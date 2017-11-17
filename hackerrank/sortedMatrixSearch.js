var sms = function(matrix, target) {
  var queue = [[0,0]];
  var maxVert = matrix.length;
  var maxHor = matrix[0].length === undefined ? 0 : matrix[0].length;
  
  var search = function(coord) {
    var vert = coord[0];
    var hor = coord[1];
    queue.shift();

    if (matrix[vert][hor] === target) {
      return vert + ',' + hor;
    }

    if (matrix[vert][hor] < target) {
      if (vert + 1 < maxVert) {
        // add to queue
        queue.push([vert + 1, hor])
      }
      if (hor + 1 < maxHor) {
        // add to queue
        queue.push([vert, hor + 1])
      }
    }

    while (queue.length > 0) {
      return search(queue[0]);
    }

    return 'not found';
  }

  return search(queue[0]);
}



var test1 = [[0,1,2,3,4]];

var test2 = [[0,1,2,3,4],
[5,6,7,8,9],
[10,11,12,13,14],
[15,16,17,18,19],
[20,21,22,23,24]];

var test3 = [[0,10,20,30,40],
[2,15,21,50,67],
[3,16,22,51,68],
[12,18,32,85,86],
[17,19,35,88,90]];

var assert = function(a,b) {
  if (a == b) {console.log('success');}
  else {console.log('Expected ' + a + ' to eqaul ' + b);}
}


assert(sms(test1, 0), '0,0');
assert(sms(test1, 4), '0,4');
assert(sms(test1, 8), 'not found');

assert(sms(test2, 4), '0,4');
assert(sms(test2, 9), '1,4');
assert(sms(test2, 24), '4,4');
assert(sms(test2, 18), '3,3');

assert(sms(test3, 4), 'not found');
assert(sms(test3, 3), '2,0');
assert(sms(test3, 18), '3,1');
assert(sms(test3, 32), '3,2');