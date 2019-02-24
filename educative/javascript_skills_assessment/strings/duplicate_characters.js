const reduceString = (str, amount) => {
    if (str.length <= amount) {
      return str;
    }

    let split_str = str.split('');
    return split_str.map((elem, i) => {
        if (i <= amount-1) {return elem;}

        if (split_str.slice(i-amount,  i).every(el => el === elem)) {
            return '';
        }
        return elem;
    }).join('');
};
