package jigsaw;

public class SolutionChecker {

    boolean isCorrectlyAssembled(PuzzlePiece[][] puzzle) {
        int rows = puzzle.length;
        int columns = puzzle[0].length;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                PuzzlePiece piece = puzzle[i][j];
                
                if (i == 0 && piece.getTop() != 0) return false;
                if (i != 0 &&
                    piece.getTop() != puzzle[i - 1][j].getBottom()) return false;
                
                if (i == rows - 1 && piece.getBottom() != 0) return false;
                
                if (j == 0 && piece.getLeft() != 0) return false;
                if (j != 0 &&
                    piece.getLeft() != puzzle[i][j - 1].getRight()) return false;
                
                if (j == columns - 1 && piece.getRight() != 0) return false;
            }
        }
        return true;
    }
}
