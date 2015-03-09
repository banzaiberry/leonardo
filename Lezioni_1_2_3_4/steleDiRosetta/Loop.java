import java.lang.Math;

/*
 * Loop Class
 */
public class Loop {
	final static int NLOOP = 100000;
	
	//public Loop() {
		// TODO 
	//}
	
	public void createTable(int nLoop){
		long p2,p3;
	    double sq;
	    long start, stop, time_spent;
	    
	    	    
	    System.out.println("Begin loop");
	    
	    start = System.currentTimeMillis();
	    for (int i = 0; i < nLoop; i++){
	    	p2 = (long)Math.pow((double)i, 2.0);
	    	p3 = (long)Math.pow((double)i, 3.0);
	    	sq = Math.sqrt((double)i);
	    	
	    	String result = String.format("%d\t%d\t%d\t%5.3f",i,p2,p3,sq);
	    	System.out.println(result);
	    	
	    }
	    stop = System.currentTimeMillis();
	    System.out.println("End loop");
	    
	    time_spent = stop - start;
	    System.out.println(String.format("Done in %d millsec\n", time_spent ));
		
	}

	public static void main(String[] args) {
		Loop myObj = new Loop();
		myObj.createTable(NLOOP);

	}

}
