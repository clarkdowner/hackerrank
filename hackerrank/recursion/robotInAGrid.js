var robotPath = function(grid, path, right, down) {
  var right = right || 0;
  var down = down || 0;
  var path = path || '';

  if (right === grid[0].length - 1 && down === grid.length - 1 && grid[down][right] === 1) {
    return path.slice(1);
  }

  grid[down][right] = 0;

  if (grid[down + 1] !== undefined && grid[down + 1][right] === 1) {
    return robotPath(grid, path + ',d', right, down + 1);
  }
  if (grid[down][right + 1] !== undefined && grid[down][right + 1] === 1) {
    return robotPath(grid, path + ',r', right + 1, down);
  }
}


var tc1 = [
  [1,0,0,0,0],
  [1,0,0,0,0],
  [1,0,0,0,0],
  [1,1,1,1,1]];

var tc2 = [
  [1,1,1,1,1],
  [0,0,0,0,1],
  [0,0,0,0,1],
  [0,0,0,0,1]];

var tc3 = [
  [1,1,1,1,1],
  [0,1,0,0,1],
  [0,1,1,0,0],
  [0,0,1,1,1]];

var tc4 = [
  [1,0,0,0,0],
  [1,0,0,0,0],
  [1,0,0,0,0],
  [1,0,0,0,0]];

var tc5 = [
  [1,1,1,1,1,1,1,1,1],
  [0,1,0,0,1,1,1,1,1],
  [0,1,1,0,0,0,0,1,0],
  [0,0,1,1,1,1,1,1,1],
  [0,0,0,0,0,0,1,0,0],
  [0,0,1,1,1,1,1,1,1]];  

console.log(robotPath(tc1)); // d,d,d,r,r,r,r
console.log(robotPath(tc2)); // r,r,r,r,d,d,d
console.log(robotPath(tc3)); // r,d,d,r,d,r,r
console.log(robotPath(tc4)); // no path
console.log(robotPath(tc5)); // r,d,d,r,d,r,r,r,r,d,d,r,r