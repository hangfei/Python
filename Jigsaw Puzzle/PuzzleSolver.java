package jigsaw;

/**
 * Solves jigsaw puzzles.
 * @author Dave Matuszek
 * @version Feb 22, 2013
 */
public class PuzzleSolver {

    /**
     * Solves a jigsaw puzzle.
     * @param rows The number of rows that should be in the solved puzzle.
     * @param columns The number of pieces that should be in each row.
     * @param pieces All the pieces.
     * @return The solved puzzle.
     */
    public PuzzlePiece[][] solve(int rows, int columns, PuzzlePiece[] pieces) {
        System.out.println("-----------------------------------------------\n");
        System.out.println("Now trying to solve the puzzle...");
        PuzzlePiece[][] puzzle = new PuzzlePiece[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                long matchAbove = (i == 0) ? 0L : puzzle[i - 1][j].getBottom();
                long matchLeft = (j == 0) ? 0L : puzzle[i][j - 1].getRight();
                PuzzlePiece piece = findPiece(matchAbove, matchLeft, pieces);
                System.out.println("Placing piece " + piece);
                putPiece(puzzle, piece, i, j);
                JigsawPuzzle.print(puzzle);
            }
        }
        System.out.println("Done solving puzzle.");
        return puzzle;
    }
    
    /**
     * Places one piece into the solved puzzle.
     * @param puzzle The 2D jigsaw puzzle.
     * @param piece The piece to place.
     * @param row The row in which to place the piece.
     * @param column The column in which to place the piece.
     */
    private void putPiece(PuzzlePiece[][] puzzle, PuzzlePiece piece, int row, int column) {
        puzzle[row][column] = piece;
    }


    /**
     * Finds a piece with the desired edges.
     * @param topWanted The edge that is wanted for the top of the piece.
     * @param leftWanted The edge that is wanted for the left side of the piece.
     * @param pieces The pieces to search through.
     * @return The desired piece.
     */
    PuzzlePiece findPiece(long topWanted, long leftWanted, PuzzlePiece[] pieces) {
        int numberOfPieces = pieces.length;
        for (int i = 0; i < numberOfPieces; i++) {
            if (pieces[i] == null) continue;
            if (pieces[i].getTop() == topWanted &&
                    pieces[i].getLeft() == leftWanted) {
                return pieces[i];
            }
        }
        System.out.println("Cannot find a piece matching " + topWanted +
                           "  " + leftWanted + "!!!");
        System.exit(1);
        return null;
    }
}
