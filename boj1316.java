import java.util.Arrays;
import java.util.Scanner;

public class boj1316 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count=0;
        for(int i=0;i<N;i+=1){
            boolean groud_word = false;
            String previous_word = "";
            String Nword_string = sc.nextLine();
            char[] Nword = Nword_string.toCharArray();
            for(int j=0;j<Nword.length;j+=1){
                System.out.println(previous_word.indexOf(Nword[j]));
                System.out.println("-------------");
                if(previous_word.lastIndexOf(Nword[j])==-1){
                    previous_word+=Nword[j];
                    groud_word=true;
                    continue;
                }
                if(previous_word.lastIndexOf(Nword[j])==1){
                    groud_word=true;
                }
                else if(previous_word.lastIndexOf(Nword[j])>=2){
                    groud_word=false;
                    break;
                }
            }
            System.out.println(previous_word);
            if(groud_word){
                count+=1;
            }

        }
        System.out.println(count);
    }
}
