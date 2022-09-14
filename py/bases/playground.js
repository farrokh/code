// Mazes can be loads of fun ... but only if a possible route actually exists. Your job is to write a function that determines whether it's possible to get from a starting point to a predetermined destination for a given maze.

// The maze itself is a two-dimensional array, consisting of ones (signifying barriers) and zeros (signifying open space).

// Example Maze #1:

// [
//     [1, 0, 0, 1, 1],
//     [1, 1, 0, 1, 1],
//     [1, 0, 0, 1, 1],
//     [1, 0, 1, 1, 0],
//     [1, 0, 0, 0, 0],
// ]
// You'll receive starting and destination coordinates in as (row, column) notation. This means (0, 2) in the example maze is middle cell in the top row, because the row is 0 and the column is 2. The start and destination coordinates will always have a value of 0.

// Your function will determine whether it is possible to get from the starting coordinate to the destination coordinate by only moving across 0-valued cells.

// Looking at our example maze again, let's assume that start = (0, 1) and dest = (4, 3). Here's the same maze, but this time the valid path is marked by replacing the 0 value with an asterisk (*).

// [
//     [1, *, *, 1, 1],
//     [1, 1, *, 1, 1],
//     [1, *, *, 1, 1],
//     [1, *, 1, 1, 0],
//     [1, *, *, *, 0],
// ]
// Because it's possible to get from the start to the destination by touching only zeros, your function should return true.

// Let's try an example where it isn't possible to get from the start to the destination.

// Example Maze #2:

// [
//     [1, 0, 0, 1],
//     [1, 1, 0, 1],
//     [0, 1, 0, 1],
// ]
// For this maze start = (2, 0) and dest = (0, 1). Given that the starting cell is entirely surrounded by ones, this maze isn't possible to complete.

// [ 
//     [1, 0, 0, 1],
//     [1, 1, 0, 1],
//     [*, 1, 0, 1],
// ]
// Allowed moves:

// The only moves allowed are up, down, left, and right. Diagonals are not allowed. For the maze diagram below, assume you're starting on the cell labeled E.

// [
//     [A, B, C],
//     [D, E, F],
//     [G, H, J],
// ]
// Starting at E, the valid moves are E -> B, E -> F, E -> H, and E -> D.


// Constraints

// 0 ≤ n, m ≤ 100
// 0 ≤ start, dest < n * m


const solution = (maze, startRow, startCol, destRow, destCol) => {
    const visited = new Set();
    const queue = [[startRow, startCol]];
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    const n = maze.length;
    const m = maze[0].length;
    while (queue.length) {
        const [row, col] = queue.shift();
        if (row === destRow && col === destCol) return true;
        if (visited.has(`${row},${col}`)) continue;
        visited.add(`${row},${col}`);
        for (const [rowOffset, colOffset] of directions) {
            const nextRow = row + rowOffset;
            const nextCol = col + colOffset;
            if (nextRow < 0 || nextRow >= n || nextCol < 0 || nextCol >= m) continue;
            if (maze[nextRow][nextCol] === 1) continue;
            queue.push([nextRow, nextCol]);
        }
    }
    return false;

};

console.log(solution([
  [0, 1],
  [1, 0],
], 0, 0, 1, 1));

