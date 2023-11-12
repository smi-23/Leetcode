class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> table = new HashMap<>();
        table.put('I', 1);
        table.put('V', 5);
        table.put('X', 10);
        table.put('L', 50);
        table.put('C', 100);
        table.put('D', 500);
        table.put('M', 1000);

        int ans = 0;
        int n = s.length();
        for (int i = 0; i < n; i++){
            if (i < n -1 && table.get(s.charAt(i)) < table.get(s.charAt(i+1))){
                ans -= table.get(s.charAt(i));
            }else{
                ans += table.get(s.charAt(i));
            }
        }
        return ans;
    }
}