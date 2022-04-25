public class TwoSum {
	public static void main(String[] args){
		System.out.println("Test");
		int[] intArray = new int[]{2,7,11,15};

		int[] answer = twoSum(intArray,9);
		System.out.println(answer[0] + " " + answer[1]);
	}
	
	public static int[] twoSum(int[] nums, int target){
		for(int i =0; i<nums.length; i++){
			for(int j = i+1;j<nums.length;j++){
				if(nums[i] + nums[j] == target){
					return new int[] {i,j};
				}
			}
		}
		return null;
	}
}
