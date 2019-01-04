(() => {

	let foo = (x, y = x * 2) => {

		return function bar(z) {
			if (z.length > 3) {
				return z.map( function baz(v){
					if (v > 3) return v + y;
					else return baz( v * 4 );
				} );

			}
			else {
				let obj = [];

				setTimeout( () => {
					obj.length = 1;
					obj[0] = this.w;
				}, 100 );

				return obj;
			}
		};
	}

	let p = foo( 2 );
	let list1 = [1,3,4];
	let list2 = list1.concat( 6 );

	list1 = p.call( { w: 42 }, list1 );
	list2 = p( list2 );


	setTimeout( () =>
		console.log( list1[0] === list2.reduce( (s,v) => s + v, 0))
	, 200);
})();