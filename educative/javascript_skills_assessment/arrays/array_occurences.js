const findAllOccurrences = (arr, target) => {
    return arr.map((elem, i) => elem === target ? i : null)
        .filter(elem => elem != null);
};
