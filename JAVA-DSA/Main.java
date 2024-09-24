
class Main {
    static int count = 0;
    public static void func(){ 
        if ( count == 4 ) return;
        System.out.println(count);
        count++;
        func();
    }

    public static void main(String args[]) {
        func();
    }
}

