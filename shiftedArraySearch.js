var search = function(array, target) {
  min = 0;
  max = array.length - 1;

  while (min <= max) {
    var searchAt = Math.floor((max - min) / 2) + min; 
    if (array[searchAt] === target) {
       return searchAt;
    } 

    if (array[min] < array[searchAt]) {
       if (array[min] <= target && target < array[searchAt]) {
          max = searchAt - 1;
       } else {
          min = searchAt + 1;
       }
    } else {
       if (array[searchAt] < target && target <= array[max]) {
          min = searchAt + 1;
       } else {
          max = searchAt - 1;
       }
    }
  }

  return -1;
}


console.log(search([12, 17, 2, 4, 5, 9], 13)); // -1
console.log(search([12, 17, 2, 4, 5, 9], 1)); // -1
console.log(search([12, 17, 2, 4, 5, 9], 12)); // 0
console.log(search([12, 17, 2, 4, 5, 9], 17)); // 1
console.log(search([12, 17, 2, 4, 5, 9], 2)); // 2
console.log(search([12, 17, 2, 4, 5, 9], 4)); // 3
console.log(search([12, 17, 2, 4, 5, 9], 5)); // 4
console.log(search([12, 17, 2, 4, 5, 9], 9)); // 5
