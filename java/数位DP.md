#### [面试题 17.06. 2出现的次数](https://leetcode.cn/problems/number-of-2s-in-range-lcci/)

编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。

**示例:**

> 输入: 25
> 输出: 9
> 解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)

提示：

- `n <= 10^9`

```
class Solution {
    char[] s;
    int[][] dp;

    public int numberOf2sInRange(int n) {
        s = Integer.toString(n).toCharArray();
        dp = new int[s.length][s.length];
        for(int i = 0; i < s.length; i++) {
            Arrays.fill(dp[i], -1);
        }

        return count(0, true, 0);
    }

    public int count(int i, boolean isLimit, int times) {
        if (i == s.length) {
            return times;
        }

        if (!isLimit && dp[i][times] != -1) {
            return dp[i][times];
        }

        int ans = 0;
        int up = isLimit ? s[i] - '0' : 9;
        for (int d = 0; d <= up; d++) {
            ans += count(i + 1, isLimit && d == up, times + (d == 2 ? 1 : 0));
        }
        
        if (!isLimit) {
            dp[i][times] = ans;
        }

        return ans;
    }
}
```

#### [902. 最大为 N 的数字组合](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/)

给定一个按 **非递减顺序** 排列的数字数组 `digits` 。你可以用任意次数 `digits[i]` 来写的数字。例如，如果 `digits = ['1','3','5']`，我们可以写数字，如 `'13'`, `'551'`, 和 `'1351315'`。

返回 *可以生成的小于或等于给定整数 `n` 的正整数的个数* 。

 

**示例 1：**

> 输入：digits = ["1","3","5","7"], n = 100
> 输出：20
> 解释：
> 可写出的 20 个数字是：
> 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

**示例 2：**

> 输入：digits = ["1","4","9"], n = 1000000000
> 输出：29523
> 解释：
> 我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
> 81 个四位数字，243 个五位数字，729 个六位数字，
> 2187 个七位数字，6561 个八位数字和 19683 个九位数字。
> 总共，可以使用D中的数字写出 29523 个整数。

**示例 3:**

> 输入：digits = ["7"], n = 8
> 输出：1

 

**提示：**

- `1 <= digits.length <= 9`
- `digits[i].length == 1`
- `digits[i]` 是从 `'1'` 到 `'9'` 的数
- `digits` 中的所有值都 **不同** 
- `digits` 按 **非递减顺序** 排列
- `1 <= n <= 109`

```
class Solution {
    char[] s;
    int[] dp;

    public int atMostNGivenDigitSet(String[] digits, int n) {
        s = Integer.toString(n).toCharArray();
        dp = new int[s.length];
        Arrays.fill(dp, -1);

        return count(0, false, true, digits);
    }

    public int count(int i, boolean isFilledNum, boolean isLimit, String[] digits) {
        if (i == s.length) {
            return isFilledNum ? 1 : 0;
        }

        if (!isLimit && isFilledNum && dp[i] != -1) {
            return dp[i];
        }

        int ans = 0;
        if (!isFilledNum) {
            ans += count(i + 1, false, false, digits);
        }
        int up = isLimit ? s[i] : '9';
        for (int d = 0; d < digits.length; d++) {
            if (digits[d].charAt(0) > up) {
                break;
            }
            ans += count(i + 1, true, isLimit && up == digits[d].charAt(0), digits);
        }
        
        if (!isLimit && isFilledNum) {
            dp[i] = ans;
        }

        return ans;
    }
}
```

#### [600. 不含连续1的非负整数](https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/)

给定一个正整数 `n` ，请你统计在 `[0, n]` 范围的非负整数中，有多少个整数的二进制表示中不存在 **连续的 1** 。

**示例 1:**

> 输入: n = 5
> 输出: 5
> 解释: 
> 下面列出范围在 [0, 5] 的非负整数与其对应的二进制表示：
> 0 : 0
> 1 : 1
> 2 : 10
> 3 : 11
> 4 : 100
> 5 : 101
> 其中，只有整数 3 违反规则（有两个连续的 1 ），其他 5 个满足规则。

**示例 2:**

> 输入: n = 1
> 输出: 2

**示例 3:**

> 输入: n = 2
> 输出: 3

 

**提示:**

- `1 <= n <= 109`

```
class Solution {
    char[] s;
    int[][] dp;

    public int findIntegers(int n) {
        s = Integer.toBinaryString(n).toCharArray();
        dp = new int[s.length][2];
        for(int i = 0; i < s.length; i++) {
            Arrays.fill(dp[i], -1);
        }

        return count(0, 0, true);
    }
    
    public int count(int i, int pre, boolean isLimit) {
        if (i == s.length) {
            return 1;
        }

        if (!isLimit && dp[i][pre] != -1) {
            return dp[i][pre];
        }

        int ans = 0;
        int up = isLimit ? s[i] - '0' : 1;
        ans += count(i + 1, 0, isLimit && up == 0);
        if (pre == 0 && up == 1) {
            ans += count(i + 1, 1, isLimit);
        }

        if (!isLimit) {
            dp[i][pre] = ans;
        }

        return ans;
    }
}
```

#### [233. 数字 1 的个数](https://leetcode.cn/problems/number-of-digit-one/)

给定一个整数 `n`，计算所有小于等于 `n` 的非负整数中数字 `1` 出现的个数。

 

**示例 1：**

> 输入：n = 13
> 输出：6

**示例 2：**

> 输入：n = 0
> 输出：0

 

**提示：**

- `0 <= n <= 109`

```
class Solution {
    char[] s;
    int[][] dp;

    public int countDigitOne(int n) {
        s = Integer.toString(n).toCharArray();
        dp = new int[s.length][s.length];
        for(int i = 0; i < s.length; i++) {
            Arrays.fill(dp[i], -1);
        }

        return count(0, 0, true);
    }

    public int count(int i, int sum, boolean isLimit) {
        if (i == s.length) {
            return sum;
        }

        if (!isLimit && dp[i][sum] != -1) {
            return dp[i][sum];
        }

        int ans = 0;
        int up = isLimit ? s[i] - '0' : 9;
        for (int d = 0; d <= up; d++) {
            ans += count(i + 1, sum + (d == 1 ? 1 : 0), isLimit && d == up);
        }

        if (!isLimit) {
            dp[i][sum] = ans;
        }

        return ans;
    }
}
```

#### [1012. 至少有 1 位重复的数字](https://leetcode.cn/problems/numbers-with-repeated-digits/)

正整数 `n`，返回在 `[1, n]` 范围内具有 **至少 1 位** 重复数字的正整数的个数。

 

**示例 1：**

> 输入：n = 20
> 输出：1
> 解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

**示例 2：**

> 输入：n = 100
> 输出：10
> 解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

**示例 3：**

> 输入：n = 1000
> 输出：262

 

**提示：**

- `1 <= n <= 109`

```
class Solution {
    char[] s;
    int[][] dp;

    public int numDupDigitsAtMostN(int n) {
        s = Integer.toString(n).toCharArray();
        dp = new int[s.length][1 << 10];
        for(int i = 0; i < s.length; i++) {
            Arrays.fill(dp[i], -1);
        }
        
        return n - countNoDupNum(0, 0, true, false);
    }

    public int countNoDupNum(int i, int mask, boolean isLimit, boolean isFilledNum) {
        if(i == s.length) {
            return isFilledNum ? 1 : 0;
        }
           
        // 前面既没有填n对应位上的数，又填了数，那么后面填的都不受限
        if(!isLimit && isFilledNum && dp[i][mask] != -1) {
            return dp[i][mask];
        }
            
        
        int ans = 0;
        if(!isFilledNum) {
            ans += countNoDupNum(i + 1, mask, false, false);
        }
            
        int up = isLimit ? (s[i] - '0') : 9 ;
        int low = isFilledNum ? 0 : 1;
        for(int d = low; d <= up; d++) {
            if((mask >> d & 1) == 0) {
                ans += countNoDupNum(i + 1, mask | (1 << d), isLimit && d == up, true);
            }        
        }
        if (!isLimit && isFilledNum) {
            dp[i][mask] = ans;
        }
            
        return ans;
    }
}
```

