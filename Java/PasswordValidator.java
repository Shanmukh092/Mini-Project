/*
Problem Statement
Build a Password Strength Checker that validates a string against corporate security policies
and provides specific feedback on why a password failed.

Student Tasks:
1. The Policy: The password must be:
        ==> At least 8 characters long.
        ==> Contain at least one Uppercase letter.
        ==> Contain at least one Digit (0-9).
*/

import java.util.HashMap;
import java.util.Scanner;

class Password{
    public String validatePassword(String str){
        if(str.length()<8)  return "Invalid Password: Must be 8 Characters Long, Please Try Again";

        boolean isUpper = false,isDigit = false,isSpecial = false;
        HashMap<Character,Integer> map  = new HashMap<>();
        map.put('@', 1);
        map.put('$', 1);
        map.put('#', 2);
        map.put('&', 1);

        for(int i=0;i<str.length();i++){
            int acciValue = (int)str.charAt(i);
            if(48<=acciValue && acciValue<=57){
                isDigit = true;
            }
            if(65<=acciValue && acciValue<=90){
                isUpper = true;
            }
            if(map.containsKey(str.charAt(i))){
                isSpecial = true;
            }
        }
        if(!isDigit)    return "Invalid Password: Must have atleast 1 digit, Please Try Again";
        if(!isUpper)    return "Invalid Password: Must have atleast 1 upper case character, Please Try Again";
        if(!isSpecial)  return "Invalid Password: Must have atleast 1 special Character, Please Try Again";
        return "Valid Password, Meets all required Crieteria";
    }

    public boolean check(String s){
        return s.equals(new String("Valid Password, Meets all required Crieteria"));
    }
}

class PasswordValidator{
    public static void main(String[] args) {
        Password pwd = new Password();
        System.out.print("Enter Password:");
        Scanner sc = new Scanner(System.in);
        String Password = sc.nextLine();

        String s = pwd.validatePassword(Password);
        boolean truthVal = pwd.check(pwd.validatePassword(Password));

        while(!truthVal){
            System.out.print(s+"\nEnter Password:");
            Password = sc.nextLine();
            s = pwd.validatePassword(Password);
            truthVal = pwd.check(s);
        }
        sc.close();
    }
}