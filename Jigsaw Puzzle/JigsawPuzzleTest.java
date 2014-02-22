package jigsaw;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class JigsawPuzzleTest {

    @Before
    public void setUp() throws Exception {}

    @Test
    public final void testLastThreeDigits() {
        assertEquals(834, PuzzlePiece.lastThreeDigits(54321834));
        assertEquals(34, PuzzlePiece.lastThreeDigits(54321034));
        assertEquals(834, PuzzlePiece.lastThreeDigits(-54321834));
    }

    @Test
    public final void testToString() {
        PuzzlePiece piece = new PuzzlePiece(12345678, 4567890, 11112222, 40100);
        assertEquals("[678 890 222 100]", piece.toString());
    }

    @Test
    public final void testShuffle() {
        Integer[] a = new Integer[100];
        for (int i = 0; i < 100; i++) a[i] = i + 1;
        PuzzleCreator.shuffle(a);
        boolean good = false;
        for (int i = 0; i < 100; i++) 
            if (a[i] != i + 1) good = true;
        assertTrue(good);
        int sum = 0;
        for (int i = 0; i < 100; i++) sum += a[i];
        assertEquals(5050, sum);
    }
    
    @Test
    public final void testFindPiece() {
        PuzzlePiece[] pieces = new PuzzlePiece[100];
        for (int i = 0; i < 100; i++) {
            pieces[i] = new PuzzlePiece(-1, -1, -1, -1);   
        }
        PuzzlePiece goal = pieces[43];
        PuzzleSolver solver = new PuzzleSolver();
        PuzzlePiece found = solver.findPiece(goal.getTop(), goal.getLeft(), pieces);
        assertEquals(goal.getTop(), found.getTop());
        assertEquals(goal.getLeft(), found.getLeft());
        assertEquals(goal.getBottom(), found.getBottom());
        assertEquals(goal.getRight(), found.getRight());
    }
    @Test
    public final void testIsCorrectlyAssembled() {
        long a = 123456;
        long b = 78910;
        long c = 11112222;
        long d = 33334444;
        PuzzlePiece[][] puzzle = new PuzzlePiece[2][2];
        puzzle[0][0] = new PuzzlePiece(0, 0, a, b);
        puzzle[0][1] = new PuzzlePiece(0, a, 0, c);
        puzzle[1][0] = new PuzzlePiece(b, 0, d, 0);
        puzzle[1][1] = new PuzzlePiece(c, d, 0, 0);
        SolutionChecker checker = new SolutionChecker();
        assertTrue(checker.isCorrectlyAssembled(puzzle));
        puzzle[1][1] = new PuzzlePiece(d, c, 0, 0);
        assertFalse(checker.isCorrectlyAssembled(puzzle)); 
    }

}
