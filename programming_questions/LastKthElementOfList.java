public class LastKthElementOfList {

    public static class Node {
        public int value;
        public Node next;

        Node(int value) {
            this.value = value;
            this.next = null;
        }

        Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }
    }

    private static Node kthLastElement(Node list, int k) {
        Node runner = list;
        for (int i = 0; i < k; i++) {
            runner = runner.next;
        }
        if (runner == null)
            return list;
        Node follower = list;
        while (runner.next != null) {
            runner = runner.next;
            follower = follower.next;
        }
        return follower.next;
    }

    public static Node solution() {
        Node list = new Node(1, new Node(2, new Node(3, new Node(4, new Node(5)))));
        int k = 4;
        return kthLastElement(list, k);
    }

}
