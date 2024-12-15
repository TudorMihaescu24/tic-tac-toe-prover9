import subprocess

def generateSolveFile(grid, player):
    
    prover9 = "formulas(assumptions).\n"

    for row in range(3):
        for col in range(3):
            value = grid[row][col]
            if value == 1:  # Player 1's mark (X)
                prover9 += f"mark({row + 1},{col + 1},X).\n"
            elif value == 2:  # Player 2's mark (O)
                prover9 += f"mark({row + 1},{col + 1},O).\n"
            else:  # Empty cell
                prover9 += f"mark({row + 1},{col + 1},E).\n"

    prover9 += """
    mark(1,1,X) & mark(1,2,X) & mark(1,3,X) -> win(X).
    mark(2,1,X) & mark(2,2,X) & mark(2,3,X) -> win(X).
    mark(3,1,X) & mark(3,2,X) & mark(3,3,X) -> win(X).

    mark(1,1,X) & mark(2,1,X) & mark(3,1,X) -> win(X).
    mark(1,2,X) & mark(2,2,X) & mark(3,2,X) -> win(X).
    mark(1,3,X) & mark(2,3,X) & mark(3,3,X) -> win(X).

    mark(1,1,X) & mark(2,2,X) & mark(3,3,X) -> win(X).
    mark(1,3,X) & mark(2,2,X) & mark(3,1,X) -> win(X).

    mark(1,1,O) & mark(1,2,O) & mark(1,3,O) -> win(O).
    mark(2,1,O) & mark(2,2,O) & mark(2,3,O) -> win(O).
    mark(3,1,O) & mark(3,2,O) & mark(3,3,O) -> win(O).

    mark(1,1,O) & mark(2,1,O) & mark(3,1,O) -> win(O).
    mark(1,2,O) & mark(2,2,O) & mark(3,2,O) -> win(O).
    mark(1,3,O) & mark(2,3,O) & mark(3,3,O) -> win(O).

    mark(1,1,O) & mark(2,2,O) & mark(3,3,O) -> win(O).
    mark(1,3,O) & mark(2,2,O) & mark(3,1,O) -> win(O).

end_of_list.

formulas(goals).
    """
    
    if(player == 1):
        prover9 += """
    win(X).
end_of_list.
    """
    else:
        prover9 += """
    win(O).
end_of_list.
    """

    with open("solve.in", "w") as f:
        f.write(prover9)
        
        
def check():
    try:
        with open("solve.out", "r") as output_file:
            content = output_file.read()
            if "Exiting with 1 proof." in content:
                return True  
            else:
                return False 
    except FileNotFoundError:
        return False


def run_prover9():
    try:
        with open("solve.out", "w") as output_file:
            result = subprocess.run(
                ["bin/prover9", "-f", "solve.in"],
                stdout=output_file, 
                text=True
            )
        if result.returncode != 0:
            return True 
    except FileNotFoundError:
        return False
