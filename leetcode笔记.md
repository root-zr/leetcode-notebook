# 🔥 LeetCode 热题 HOT 100



#### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

**提示：**

- `2 <= nums.length <= 103`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **只会存在一个有效答案**

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i< nums.length; i++) {
            if(map.containsKey(target - nums[i])) {
                return new int[] {map.get(target-nums[i]),i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

//直接用暴力破解法也能解决这个问题
```

#### [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

![](E:\大三下\leetcode\img\addtwonumber1.jpg)



```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```

**示例 2：**

```
输入：l1 = [0], l2 = [0]
输出：[0]
```

**示例 3：**

```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```

**提示：**

- 每个链表中的节点数在范围 `[1, 100]` 内
- `0 <= Node.val <= 9`
- 题目数据保证列表表示的数字不含前导零

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode pre = new ListNode(0);
        ListNode cur = pre;
        int carry = 0;
        while(l1 != null || l2 != null) {
            int x = l1 == null ? 0 : l1.val;
            int y = l2 == null ? 0 : l2.val;
            int sum = x + y + carry;
            
            carry = sum / 10;
            sum = sum % 10;
            cur.next = new ListNode(sum);

            cur = cur.next;
            if(l1 != null)
                l1 = l1.next;
            if(l2 != null)
                l2 = l2.next;
        }
        if(carry == 1) {
            cur.next = new ListNode(carry);
        }
        return pre.next;
    }
}
```



#### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。

**示例 1:**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

**示例 2:**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

**示例 4:**

```
输入: s = ""
输出: 0
```

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max = 0;//最长子串长度
        int left = 0;//滑动窗口左下标，i相当于滑动窗口右下标
        for(int i = 0; i < s.length(); i ++){
            if(map.containsKey(s.charAt(i))){
                //charAt() 方法用于返回指定索引处的字符。            
                //索引范围为从 0 到 length() - 1。
                left = Math.max(left,map.get(s.charAt(i)) + 1);      
                //map.get():返回字符所对应的索引(原函数是返回KEY对应的值，这里值就是字符串的索                //引），当发现重复元素时，窗口左指针右移
            }        
           //map.get('a')=0,因为map中只有第一个a的下标，然后更新left指针到原来left的的下一位
            map.put(s.charAt(i),i);      //再更新map中a映射的下标
            max = Math.max(max,i-left+1);     //比较两个参数的大小
        }
        return max;
        
    }
}
```

#### [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

**示例 1：**

```
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
```

**示例 2：**

```
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```

**示例 3：**

```
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
```

**示例 4：**

```
输入：nums1 = [], nums2 = [1]
输出：1.00000
```


**示例 5：**

```
输入：nums1 = [2], nums2 = []
输出：2.00000
```

**提示：**

* nums1.length == m
* nums2.length == n
* 0 <= m <= 1000
* 0 <= n <= 1000
* 1 <= m + n <= 2000
* -106 <= nums1[i], nums2[i] <= 106

**进阶：**   你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

```java
//采用归并排序的方式来解题
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {    
        int a = 0;  
        int b = 0;
        int len1 = nums1.length;
        int len2 = nums2.length;

        //判断是否有一个数组是空的，直接用另一个数组计算中位数
        if(len1 == 0){
            double result = middle(nums2,len1,len2);
            return result ;
        }

        if(len2 == 0){
            double result = middle(nums1,len1,len2);
            return result ;
        }
         
        //第三个数组，长度为前两个之和，保存排好序的数组
        int[] nums = new int[len1 + len2];
        int count = 0;  

        while(a < len1 && b < len2){
            if(nums1[a] <= nums2[b]){
                nums[count++] = nums1[a];
                a++;
            }

            else{
                nums[count++] = nums2[b];
                b++;
            }
            
            //第一个数组已经排完了，把第二个数组中的元素全部放到后面就行
            if(a == len1){
                for(int i = b; i <len2; i++){
                    nums[count++] = nums2[i];
                }
            }
            //第二个数组已经排完了，把第一个数组中的元素全部放到后面
            if(b == len2){
                for(int i = a; i <len1; i++){
                    nums[count++] = nums1[i];
                }
            }
        }
      
       return middle(nums,len1,len2);
     
    }
    
    //找一个数组的中位数的函数
    public double middle(int[] nums, int len1,int len2){
        if((len1+ len2)%2 == 0){
            int mid = (len1+ len2)/2 ;
            return (nums[mid] + nums[mid-1])/2.0;
        }

        else{
            int mid = (len1+ len2)/2;
            return nums[mid] ;
        }
    }
}
```

#### [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

**示例 1：**

```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

**示例 2：**

```
输入：s = "cbbd"
输出："bb"
```


**示例 3：**

```
输入：s = "a"
输出："a"
```


**示例 4：**

```
输入：s = "ac"
输出："a"
```

**提示：**

* 1 <= s.length <= 1000
* s 仅由数字和英文字母（大写和/或小写）组成

从回文串的定义展开讨论：

* 如果一个字符串的头尾两个字符都不相等，那么这个字符串一定不是回文串；
* 如果一个字符串的头尾两个字符相等，才有必要继续判断下去。
  * 如果里面的子串是回文，整体就是回文串；
  * 如果里面的子串不是回文串，整体就不是回文串。

```java
public class Solution {

    public String longestPalindrome(String s) {
       
        int len = s.length();
        if (len < 2) {
            return s;
        }
    
        int maxLen = 1;
        int begin = 0;

        // dp[i][j] 表示 s[i, j] 是否是回文串
        boolean[][] dp = new boolean[len][len];
        char[] charArray = s.toCharArray();

        for (int i = 0; i < len; i++) {
            dp[i][i] = true;
        }
        for (int j = 1; j < len; j++) {
            for (int i = 0; i < j; i++) {
                if (charArray[i] != charArray[j]) {
                    dp[i][j] = false;
                } else {
                    if (j - i < 3) {
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1];
                    }
                }

       // 只要 dp[i][j] == true 成立，就表示子串 s[i..j] 是回文，此时记录回文长度和起始位置
                if (dp[i][j] && j - i + 1 > maxLen) {
                    maxLen = j - i + 1;
                    begin = i;
                }
            }
        }
        return s.substring(begin, begin + maxLen);
    }
}

```

