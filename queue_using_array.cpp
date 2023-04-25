class MyQueue {
   
    public int[] arr ;
    public int size=10;
    public int front=0;
    public int rear=0;
   

    public MyQueue() {
        this.arr = new int[size];
    }
   
    public void push(int x) {
        arr[rear]=x;
        rear++;
    }
   
    public int pop() {
        int ans = arr[front];
        front++;
        return ans;
    }
   
    public int peek() {
        return arr[front];
    }
   
    public boolean empty() {
        return rear-front==0;
    }
}