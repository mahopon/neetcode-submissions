class LinkedListNode {
    private int value;
    private LinkedListNode next;

    public LinkedListNode(int value, LinkedListNode next) {
        this.value = value;
        this.next = next;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public LinkedListNode getNext() {
        return next;
    }

    public void setNext(LinkedListNode next) {
        this.next = next;
    }
}

class LinkedList {

    private LinkedListNode head;

    public LinkedList() {
        head = null;
    }

    public int get(int index) {
        if (head == null) return -1;
        if (index == 0) return head.getValue();

        LinkedListNode t_node = head;
        int counter = 0;
        while (t_node.getNext() != null) {
            t_node = t_node.getNext();
            counter += 1;
            if (counter == index) return t_node.getValue();
        }

        return -1;
    }

    public void insertHead(int val) {
        if (head == null) head = new LinkedListNode(val, null);
        else head = new LinkedListNode(val, head);
    }

    public void insertTail(int val) {
        LinkedListNode newNode = new LinkedListNode(val, null);
        if (head == null) head = newNode;
        else {
            LinkedListNode t_node = head;
            while (t_node.getNext() != null) {
                t_node = t_node.getNext();
            }
            t_node.setNext(newNode);
        }
    }

    public boolean remove(int index) {
        if (head == null) return false;
        if (index == 0) {
            if (head.getNext() != null) head = head.getNext();
            else head = null;
            return true;
        }

        LinkedListNode t_node = head;
        int counter = 0;
        while (counter < index - 1 && t_node != null) {
            t_node = t_node.getNext();
            counter += 1;
        }

        if (t_node != null && t_node.getNext() != null) {
            t_node.setNext(t_node.getNext().getNext());
            return true;
        }

        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> list = new ArrayList<>();
        
        LinkedListNode t_node = head;
        while (t_node != null) {
            list.add(t_node.getValue());
            t_node = t_node.getNext();
        }

        return list;
    }
}
