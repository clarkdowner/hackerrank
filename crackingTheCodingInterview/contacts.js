function main() {
    var n = parseInt(readLine());
    var hashStore = {};
    for(var a0 = 0; a0 < n; a0++){
        var op_temp = readLine().split(' ');
        var op = op_temp[0];
        var contact = op_temp[1];
        if (op === 'add') {
            hashStore[contact] = contact;
        } else {
            var found = 0;
            for (var key in hashStore) {
                if (key.indexOf(contact) !== -1) {
                    found++;
                }
            }
            console.log(found);
        }
    }

}