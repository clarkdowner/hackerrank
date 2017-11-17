function main(mealCost, tipPercent, taxPercent) {
	let tipCost = tipPercent * mealCost / 100;
	let taxCost = taxPercent * mealCost / 100;
	let totalCost = Math.round(mealCost + tipCost + taxCost);

	console.log(totalCost);
}