// https://www.educative.io/collection/page/10370001/2650002/2590002

// Modifies the original array
const removeWithoutCopy = function (arr, item) {
    let i = 0;

    while (i < arr.length) {
        if (arr[i] == item) {
            arr.splice(i, 1);
        } else {
            i++;
        }
    }

    return arr;
};
