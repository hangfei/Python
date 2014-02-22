package jigsaw;
import java.util.Random;

/**
 * A jigsaw puzzle.
 * @author Dave Matuszek
 * @version Feb 22, 2013
 */
public class JigsawPuzzle {
    static Random rand = new Random();

    /**
     * Creates and tries out a jigsaw puzzle.
     * @param args If provided, the number of rows and the number
     * of columns; else will use 3 rows and 4 columns.
     */
    public static void main(String args[]) {
        if (args.length != 2) args = new String[] { "3", "4" };
        int rows = new Integer(args[0]).intValue();
        int columns = new Integer(args[1]).intValue();
        new JigsawPuzzle().run(rows, columns);
    }
    
    /**
     * Creates a puzzle, disassembles it, solves it, and checks
     * if the solution is correct.
     * @param rows The number of rows in the puzzle.
     * @param columns The number of columns in the puzzle.
     */
    void run(int rows, int columns) {
        PuzzleCreator creator = new PuzzleCreator();
        PuzzlePiece[] pieces = creator.create(rows, columns);
        PuzzleSolver solver = new PuzzleSolver();
        PuzzlePiece[][] puzzle = solver.solve(rows, columns, pieces);
        SolutionChecker checker = new SolutionChecker();
        System.out.print("Checking for correctness, and...");
        if (checker.isCorrectlyAssembled(puzzle)) {
            System.out.println("everything fits!");
        } else {
            System.out.println("I DIDN'T DO IT RIGHT!!!");
        }
        print(puzzle);
    }
    
    /**
     * Returns a three-character string representing the last
     * three digits of the number. Special case:
     * The number -1 is represented as "---".
     * @param number The number to be represented.
     * @return A three-character string.
     */
    private static String threeDigits(long number) {
        if (number == -1) return "---";
        String s = "00" + number;
        return s.substring(s.length() - 3);
    }
    
    /**
     * Prints the puzzle (which may be only partially assembled).
     * @param puzzle The puzzle to be printed.
     */
    public static void print(PuzzlePiece[][] puzzle) {
        int rows = puzzle.length;
        int columns = puzzle[0].length;
        System.out.println("Current state of puzzle:");
        for (int i = 0; i < rows; i++) {
            System.out.println("+-----------+-----------+-----------+-----------+");
            for (int j = 0; j < columns; j++) {
                if (puzzle[i][j] == null) {
                    System.out.print("|    ---    ");
                } else {
                    System.out.print("|    " +
                                     threeDigits(puzzle[i][j].getTop()) +
                                     "    ");
                }
            }
            System.out.println("|");
            for (int j = 0; j < columns; j++) {
                if (puzzle[i][j] == null) {
                    System.out.print("|---     ---");
                } else {
                    System.out.print("|" +
                                     threeDigits(puzzle[i][j].getLeft()) +
                                     "     " +
                                     threeDigits(puzzle[i][j].getRight()));
                }
            }
            System.out.println("|");
            for (int j = 0; j < columns; j++) {
                if (puzzle[i][j] == null) {
                    System.out.print("|    ---    ");
                } else {
                    System.out.print("|    " +
                                     threeDigits(puzzle[i][j].getBottom()) +
                                     "    ");
                }
            }
            System.out.println("|");
        }
        System.out.println("+-----------+-----------+-----------+-----------+");
        System.out.println();
    }
}
