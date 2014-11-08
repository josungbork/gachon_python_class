import java.util.ArrayList;

public class BubbleSort {
  public static void main(String[] args) {

    ArrayList<Integer> randArrayList;
  	for (int count = 0; count < 5; count++)
  	{
  		randArrayList = new ArrayList<Integer>();
        int randNum = 0;
        int i = 0;

        while(randArrayList.size() != 2000)
        {
            randNum = (int)(Math.random() * 2000);
            if (!randArrayList.contains(new Integer(randNum)))
            {
                randArrayList.add(randNum);
            }
        }

        // Integer[] index = new Integer[randArrayList.size()];
        // index = randArrayList.toArray();

        

        int[] index = new int[randArrayList.size()];
       
        for (Integer n : randArrayList) {
            index[i++] = n.intValue();
            System.out.print(n.intValue());
        }

        int j, temp;

        for (i = 0; i < index.length - 1; i++) {
          for (j = 0; j < index.length - 1 - i; j++) {
            if (index[j] > index[j + 1]) {
              temp = index[j];
              index[j] = index[j + 1];
              index[j + 1] = temp;
            }
          }
        }

        for (i = 0; i < index.length; i++) {
          System.out.print(index[i] + " ");
        }
  	}
  }
}