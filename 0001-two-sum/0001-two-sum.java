class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;

        /////////////// brute force ///////////////

        // for (int i=0; i < n-1; i++){
        //     for (int j = 0; j < n; j++){
        //         if (nums[i] + nums[j] == target){
        //             return new int[]{i, j};
        //         }
        //     }
        // }
        // return new int[]{};

        /////////////// two-pass hash table ///////////////

        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0; i<n; i++){
            numMap.put(nums[i], i);
        }

        for (int i = 0; i<n; i++){
            int complement = target - nums[i];
            if (numMap.containsKey(complement) && numMap.get(complement) != i){
                return new int[]{numMap.get(complement), i};
            }
        }
        return new int[]{};

        /////////////// one-pass hash table  ///////////////

        // Map<Integer, Integer> numMap = new HashMap<>();

        // for (int i = 0; i < n; i++){
        //     int complement = target - nums[i];
        //     if (numMap.containsKey(complement)){
        //         return new int[]{numMap.get(complement), i};
        //     }
        //     numMap.put(nums[i], i);
        // }
        // return new int[]{};
    }
}