//Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
//Any live cell with two or three live neighbours lives on to the next generation.
//Any live cell with more than three live neighbours dies, as if by overpopulation.
//Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

// howManyNeighbors function (position, board)
	// return numberOfLiveNeighbors


// conwaysGame function take 2D board (array of arrays) with initial state

	// initialize nextState 

	// capture nextState
		// iterate over each row
			// iterate over each element in row
				// newElementState variable
				
				// if element is live
					// if 2 || 3 neighbors are live
						// live element
					// else
						// dead element

				// else element is dead
					// if 3 neighbors are live
						// live element
					// else
						// dead element
				
				// save nextState element to nextState	

	// print nextState

	// call conwaysGame with nextState