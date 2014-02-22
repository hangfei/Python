package jigsaw;

import java.util.Random;

/**
 * Defines one piece of a jigsaw puzzle.
 * @author Dave Matuszek
 * @version Feb 22, 2013
 */
public class PuzzlePiece {
    private static int Id = 0;
    Random rand = new Random();

    private long top;
    private long right;
    private long bottom;
    private long left;
    private int name;
    
    /**
     * Returns a number representing the shape of the bottom edge.
     */
    public long getBottom() {
        return bottom;
    }
    
    /**
     * Returns a number representing the shape of the left edge.
     */
    public long getLeft() {
        return left;
    }

    /**
     * Returns a number representing the shape of the right edge.
     */
    public long getRight() {
        return right;
    }

    /**
     * Returns a number representing the shape of the top edge.
     */
    public long getTop() {
        return top;
    }
   
    /**
     * Creates one piece of a jigsaw puzzle.
     * @param top A number representing the shape of the top edge.
     * @param left A number representing the shape of the left edge.
     * @param right A number representing the shape of the right edge.
     * @param bottom A number representing the shape of the bottom edge.
     */
    public PuzzlePiece(long top, long left, long right, long bottom) {
        this.top = chooseNumber(top);
        this.right = chooseNumber(right);
        this.bottom = chooseNumber(bottom);
        this.left = chooseNumber(left);
        this.name = ++Id;
        System.out.println("Created piece " + this);
    }
    
    /**
     * Returns the given number, unless the given number is -1,
     * in which case it returns a randomly chosen number.
     * @param number -1 if a random number is desired.
     * @return Either the given number, or a random number.
     */
    private long chooseNumber(long number) {
        if (number == -1) return rand.nextLong();
        else return number;
    }
    
    /**
     * Returns, as an int, the argument mod 1000.
     * @param longNumber The input number.
     * @return A number formed from the last three digits of the input number.
     */
    public static int lastThreeDigits(long longNumber) {
        return (int)(Math.abs(longNumber) % 1000);
    }

    /**
     * Returns a string representing this puzzle piece.
     * @see java.lang.Object#toString()
     */
    @Override
    public String toString() {
        return "[" + lastThreeDigits(top) +
               " " + lastThreeDigits(left) +
               " " + lastThreeDigits(right) + 
               " " + lastThreeDigits(bottom) + "]";
    }

}