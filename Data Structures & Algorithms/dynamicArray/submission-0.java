class DynamicArray {

    private Integer[] arr;
    private int length;
    private int size;

    public DynamicArray(int capacity) {
        arr = new Integer[capacity];
        length = capacity;
        size = 0;
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i] = n;
    }

    public void pushback(int n) {
        if (size == arr.length) {
            resize();
        }
        arr[size] = n;
        size += 1;
    }

    public int popback() {
        int value = arr[size-1];
        arr[size-1] = null;
        size -= 1;
        return value;
    }

    private void resize() {
        length = length * 2;
        Integer[] newArr = new Integer[length];
        for (int i = 0; i < size; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return length;
    }
}
