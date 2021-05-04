# Heuristic Search

## Idea:
	
	Storing the state of puzzle in a nxn array is tedious 
	It may overflow for large search space
	
	So , we chose current position of blank slot along with the path visited as our state
	Now you can simply think of a state machine where each operation updates the state by 
	a cell movement and updates the path visited

	in these cases persistent structural sharing or immutability is a great virtue

	Operations are moves - left , right , up , down


## Uniform Cost Search
	current implementation involves non-overlapping traversal of the puzzle
	but the point that cycle may occur is missing

	TODO: add cyclic property to the graph
	TODO: add tests for UCS

## A-star algorithm with misplaced tile Heuristic


## A-start algorithm with manhattan distance


