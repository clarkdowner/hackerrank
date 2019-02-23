// return all elements that occur more than once
const duplicates = arr => {
    let element_map = {};
    let dupes = [];

    for (let i = 0; i < arr.length; i++) {
        let elem = arr[i];
        if (!(elem in element_map)) {
            element_map[elem] = false;
        } else if (element_map[elem] == false) {
            dupes.push(elem);
            element_map[elem] = true;
        }
    }

    return dupes;
};
