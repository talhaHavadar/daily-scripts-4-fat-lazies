import java.util.HashMap;

public class PalindromeGeneration {
    /*

    This problem was asked by Quora.

    Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
    anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
    lexicographically earliest one (the first one alphabetically).
    For example, given the string "race", you should return "ecarace", since we can add three letters to it
    (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from
    "race" by adding three letters, but "ecarace" comes first alphabetically.
    As another example, given the string "google", you should return "elgoogle".

     */

    private static Boolean isPalindrome(String string) {
        for (int left = 0; left < string.length() / 2; left++) {
            int right = string.length() - 1- left;
            if (string.charAt(left) != string.charAt(right)) {
                return false;
            }
        }
        return true;
    }
    private static String helper(String subString, HashMap<String, String> cache) {
        if(cache.containsKey(subString)) return cache.get(subString);

        String result = "";

        for (int left = 0; left < subString.length() / 2; left++) {
            int right = subString.length() - 1- left;
            if (subString.charAt(left) != subString.charAt(right)) {
                String prefix = subString.substring(0, left);
                String suffix = subString.substring(right + 1);
                String newSub = subString.substring(left, right + 1);
                String leftSubstring = prefix + helper(newSub + subString.charAt(left), cache) + suffix;
                String rightSubstring = prefix + helper(subString.charAt(right) + newSub, cache) + suffix;
                String candidate = rightSubstring;
                if (leftSubstring.length() < rightSubstring.length() && isPalindrome(leftSubstring)) {
                    candidate = leftSubstring;
                } else if (leftSubstring.length() == rightSubstring.length() && leftSubstring.compareTo(rightSubstring) < 0 && isPalindrome(leftSubstring)) {
                    candidate = leftSubstring;
                }
                if ("".equals(result) || candidate.length() < result.length() && isPalindrome(candidate)) {
                    result = candidate;
                }
            }
        }
        if ("".equals(result)) {
            cache.put(subString, subString);
        } else {
            cache.put(subString, result);
        }

        return "".equals(result) ? subString: result;
    }


    private static String generatePalindrome(String input) {
        HashMap<String, String> cache = new HashMap<>();
        return helper(input, cache);
    }

    public static void solution() {
        System.out.println(generatePalindrome("google"));
    }
}
