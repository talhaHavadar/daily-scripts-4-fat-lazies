public class WellFormedBrackets {
    /*

    This problem was asked by Facebook.

    Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
    For example, given the string "([])[]({})", you should return true.
    Given the string "([)]" or "((()", you should return false.
    * */

    /**
     * O(n) time-complexity
     * O(1) space-complexity
     * @param str
     * @return
     */
    private static boolean isWellFormed(String str) {
        int start_open = 0;
        int open_idx = -1;

        for (int curr_idx = 0; curr_idx < str.length(); curr_idx++) {
            char c = str.charAt(curr_idx);
            if ((c == '(' || c == '[' || c == '{') && open_idx < start_open) {
                start_open = curr_idx;
                open_idx = start_open;
            }
            else if (c == '(' || c == '[' || c == '{') {
                open_idx++;
            }
            else if (open_idx < start_open) {
              return false;
            } else {
                char open_char = str.charAt(open_idx);
                if ((open_char == '(' && c == ')') || (open_char == '[' && c == ']') || (open_char == '{' && c == '}')) {
                    open_idx--;
                } else {
                    return false;
                }
            }
        }
        return open_idx < start_open;
    }

    public static void solution() {
        String sTrue = "([])[]({})";
        String sFalse = "([)]";
        String sFalse2 = "((()";
        String sTrue2 = "()";
        String sFalse3 = "()]()";

        System.out.println("sTrue: " + isWellFormed(sTrue));
        System.out.println("sFalse: " + isWellFormed(sFalse));
        System.out.println("sFalse2: " + isWellFormed(sFalse2));
        System.out.println("sTrue2: " + isWellFormed(sTrue2));
        System.out.println("sFalse3: " + isWellFormed(sFalse3));

    }

}
