// each row must contain 1-9 digits without repitiotn
// each column must contain the digits 1-9 withoiut reptition
// each 3x3 should contain 1-9 without repition

// we make a seen hashset
// with the outer and inner indexes and add the array where we see the index
// then we do the same with the square grid
// we are basically making vectors representations of each for row col and square
import java.util.HashSet;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> seen = new HashSet<String>();
        for (int outer = 0; outer < 9; outer++) {
            for (int inner = 0; inner < 9; inner++) {
                char current_index = board[outer][inner];

                if (current_index != '.') {
                    String rowCheck = current_index + " found in row " + outer;
                    String colCheck = current_index + " found in column " + inner;
                    String subgridCheck = current_index + " found in subgrid " + (outer / 3) + "-" + (inner / 3);

                    // Check if any identifier already exists in the set
                    if (!seen.add(rowCheck) || !seen.add(colCheck) || !seen.add(subgridCheck)) {
                        System.out.println(current_index + " found at row " + outer + " and column " + inner);
                        return false;
                    }

                }
            }
        }

        return true;

    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        char[][] validSudoku = {
                { '5', '3', '.', '.', '7', '.', '.', '.', '.' },
                { '6', '.', '.', '1', '9', '5', '.', '.', '.' },
                { '.', '9', '8', '.', '.', '.', '.', '6', '.' },
                { '8', '.', '.', '.', '6', '.', '.', '.', '3' },
                { '4', '.', '.', '8', '.', '3', '.', '.', '1' },
                { '7', '.', '.', '.', '2', '.', '.', '.', '6' },
                { '.', '6', '.', '.', '.', '.', '2', '8', '.' },
                { '.', '.', '.', '4', '1', '9', '.', '.', '5' },
                { '.', '.', '.', '.', '8', '.', '.', '7', '9' }
        };

        boolean result = solution.isValidSudoku(validSudoku);
        System.out.println(result);
    }
}