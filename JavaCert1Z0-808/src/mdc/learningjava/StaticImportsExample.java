package mdc.learningjava;

import static java.lang.Math.*;
import static java.lang.System.out;

public class StaticImportsExample {
    public static void main(String[] args) {
        int max = max(5,7);
        int min = min(5,7);
        out.println("The smallest number is " + min + " and the biggest number is " + max);
        out.println(PI);


    }
}
