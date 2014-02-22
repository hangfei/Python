package jigsaw;

import java.util.Random;

/**
 * Creates a jigsaw puzzle.
 * @author Dave Matuszek
 * @version Feb 22, 2013
 */
public class PuzzleCreator {
    static Random rand = new Random();
    
    /**
     * Creates a jigsaw puzzle.
     * @param rows The number of rows of pieces.
     * @param columns The number of pieces in each row.
     * @return The newly created jigsaw puzzle.
     */
    public PuzzlePiece[] create(int rows, int columns) {
        PuzzlePiece[] pieces = new PuzzlePiece[rows * columns];
        PuzzlePiece[][] puzzle = new PuzzlePiece[rows][columns];
        
        // Create the puzzle in assembled form
        System.out.println("Creating a " + rows + " by " + columns + " puzzle...\n");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                long left, right, top, bottom;
                top = (i == 0) ? 0L : puzzle[i - 1][j].getBottom();
                left = (j == 0) ? 0L : puzzle[i][j - 1].getRight();
                bottom = (i == rows - 1) ? 0L : -1;
                right = (j == columns - 1) ? 0L : -1;
                puzzle[i][j] = new PuzzlePiece(top, left, right, bottom);
                JigsawPuzzle.print(puzzle);
            }
        }
        System.out.println("Puzzle completed!\n\n");
        pieces = disassemble(puzzle);
        shuffle(pieces);
        return pieces;
    }
    
    /**
     * Disassembles the 2D puzzle into a 1D array.
     * @param puzzle The puzzle to be disassembled.
     * @return The pieces of the puzzle.
     */
    public PuzzlePiece[] disassemble(PuzzlePiece[][] puzzle) {
        int rows = puzzle.length;
        int columns = puzzle[0].length;
        PuzzlePiece[] pieces = new PuzzlePiece[rows * columns];
        int index = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                pieces[index] = puzzle[i][j];
                index++;
                puzzle[i][j] = null;
            }
        }
        return pieces;
    }
    
    /**
     * Shuffles an array.
     * @param array The array to be shuffled.
     */
    public static void shuffle(Object[] array) {
        System.out.println("Now shuffling the array...");
        for (int i = array.length - 1; i > 1; i--) {
            int j = rand.nextInt(i);
            Object temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        } 
        System.out.println(array);
    }
}
