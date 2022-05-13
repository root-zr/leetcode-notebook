# 🔥 LeetCode 热题 HOT 100



#### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

**示例 1：**

> 输入：nums = [2,7,11,15], target = 9
> 输出：[0,1]
> 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

**示例 2：**

> 输入：nums = [3,2,4], target = 6
> 输出：[1,2]

**示例 3：**

> 输入：nums = [3,3], target = 6
> 输出：[0,1]

**提示：**

- $2 <= nums.length <= 10^3$
-  $-10^9 <= nums[i] <= 10^9$
- $-10^9 <= target <= 10^9$
- **只会存在一个有效答案**

```c
#define BUCKET_SIZE 100

typedef struct NewList {
    int key;
    int val;
    struct NewList *next;
} List;

void listPush(List *head, int key, int val) {
    List* tmp = malloc(sizeof(List));
    tmp->key = key;
    tmp->val = val;
    tmp->next = head->next;
    head->next = tmp;
}

void listDelete(List* head, int key) {
    for (List* it = head; it->next; it = it->next) {
        if (it->next->key == key) {
            List* tmp = it->next;
            it->next = tmp->next;
            free(tmp);
            break;
        }
    }
}

List* listFind(List* head, int key) {
   
    List *tmp = head->next;
    while (tmp != NULL) {
        if (tmp->key == key) {
            return tmp;
        }
        tmp = tmp->next;
    }

    
    return NULL;
}

void listFree(List* head) {
    while (head->next) {
        List* tmp = head->next;
        head->next = tmp->next;
        free(tmp);
    }
}

int hash(int key) {
    return abs(key) % BUCKET_SIZE;
}

typedef struct {
    List* bucket;
} MyHashMap;

MyHashMap* myHashMapCreate() {
    MyHashMap* ret = malloc(sizeof(MyHashMap));
    ret->bucket = malloc(sizeof(List) * BUCKET_SIZE);
    for (int i = 0; i < BUCKET_SIZE; i++) {
        ret->bucket[i].key = 0;
        ret->bucket[i].val = 0;
        ret->bucket[i].next = NULL;
    }
    return ret;
}

void myHashMapPut(MyHashMap* obj, int key, int value) {
    int h = hash(key);
  
    List* rec = listFind(&(obj->bucket[h]), key);

    if (rec == NULL) {
        listPush(&(obj->bucket[h]), key, value);
    } else {
        rec->val = value;
    }
}

int myHashMapGet(MyHashMap* obj, int key) {
    int h = hash(key);
    List* rec = listFind(&(obj->bucket[h]), key);
    if (rec == NULL) {
        return -1;
    } else {
        return rec->val;
    }
}

void myHashMapRemove(MyHashMap* obj, int key) {
    int h = hash(key);
    listDelete(&(obj->bucket[h]), key);
}

void myHashMapFree(MyHashMap* obj) {
    for (int i = 0; i < BUCKET_SIZE; i++) {
        listFree(&(obj->bucket[i]));
    }
    free(obj->bucket);
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *res = (int *)malloc(2 * sizeof(int));
    if (res == NULL) {
        return NULL;
    }
    memset(res, 0, 2 * sizeof(int));
    *returnSize = 2;

    MyHashMap *map = myHashMapCreate();
    for (int i = 0; i < numsSize; i++) {   
        myHashMapPut(map, nums[i], i);      
    }

    for (int i = 0; i < numsSize; i++) {
        int tmp = myHashMapGet(map, target - nums[i]);
       
        if (tmp != -1 && tmp != i) {
            res[0] = i;
            res[1] = tmp;
            myHashMapFree(map);
            return res;
        }
    }
    
    return res;
}
```

#### [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

![](img/addtwonumber1.jpg)



> 输入：l1 = [2,4,3], l2 = [5,6,4]
> 输出：[7,0,8]
> 解释：342 + 465 = 807.

**示例 2：**

> 输入：l1 = [0], l2 = [0]
> 输出：[0]

**示例 3：**

> 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
> 输出：[8,9,9,9,0,0,0,1]

**提示：**

- 每个链表中的节点数在范围 `[1, 100]` 内
- `0 <= Node.val <= 9`
- 题目数据保证列表表示的数字不含前导零

```c
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *res = (struct ListNode *)malloc(sizeof(struct ListNode));
    if (res == NULL) {
        return NULL;
    } 
    memset(res, 0, sizeof(struct ListNode));

    struct ListNode *p = res;
    int carry = 0;

    while (l1 != NULL && l2 != NULL) {
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (node == NULL) {
            return NULL;
        } 
        memset(node, 0, sizeof(struct ListNode));
        node->val = (l1->val + l2->val + carry) % 10 ;
        carry = (l1->val + l2->val + carry) / 10;
        p->next = node;
        p = p->next;

        l1 = l1->next;
        l2 = l2->next;
        
    }

    while (l1 == NULL && l2 != NULL) {
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (node == NULL) {
            return NULL;
        } 
        memset(node, 0, sizeof(struct ListNode));
        node->val = (l2->val + carry) % 10 ;
        carry = (l2->val + carry) / 10;
        p->next = node;
        p = p->next;
        l2 = l2->next;
    } 

    while (l1 != NULL && l2 == NULL) {
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (node == NULL) {
            return NULL;
        } 
        memset(node, 0, sizeof(struct ListNode));
        node->val = (l1->val + carry) % 10 ;
        carry = (l1->val + carry) / 10;
        p->next = node;
        p = p->next;
        l1 = l1->next;
    }

    if (carry != 0) {
        struct ListNode *node = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (node == NULL) {
            return NULL;
        } 
        memset(node, 0, sizeof(struct ListNode));
        node->val = carry;
        p->next = node;
    }

    return res->next;
}
```



#### [3. 无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

给定一个字符串，请你找出其中不含有重复字符的 **最长子串** 的长度。

**示例 1:**

> 输入: s = "abcabcbb"
> 输出: 3 
> 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

**示例 2:**

> 输入: s = "bbbbb"
> 输出: 1
> 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

**示例 3:**

> 输入: s = "pwwkew"
> 输出: 3
> 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
>      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

**示例 4:**

> 输入: s = ""
> 输出: 0

```c
#define ASCII_LEN 128

int lengthOfLongestSubstring(char * s)
{
    int sLen = strlen(s);
    if (sLen == 0 || sLen == 1) {
        return sLen;
    }
    int arr[ASCII_LEN];
    memset(arr, -1, ASCII_LEN * sizeof(int));

    int maxLen = 0;
    int l = 0;
    for (int i = 0; i < sLen; i++) {
        if (arr[s[i]] != -1) {
            l = fmax(l, arr[s[i]] + 1);
        }
       
        maxLen = fmax(maxLen, i - l + 1);
        arr[s[i]] = i;
       
    }

    return maxLen;
}
```

#### [4. 寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/)

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

**示例 1：**

> 输入：nums1 = [1,3], nums2 = [2]
> 输出：2.00000
> 解释：合并数组 = [1,2,3] ，中位数 2

**示例 2：**

> 输入：nums1 = [1,2], nums2 = [3,4]
> 输出：2.50000
> 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

**示例 3：**

> 输入：nums1 = [0,0], nums2 = [0,0]
> 输出：0.00000

**示例 4：**

> 输入：nums1 = [], nums2 = [1]
> 输出：1.00000


**示例 5：**

> 输入：nums1 = [2], nums2 = []
> 输出：2.00000

**提示：**

* nums1.length == m
* nums2.length == n
* 0 <= m <= 1000
* 0 <= n <= 1000
* 1 <= m + n <= 2000
* $-10^6 <= nums1[i], nums2[i] <= 10^6$

**进阶：**   你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

```c
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int *arr = (int *)malloc((nums1Size + nums2Size) * sizeof(int));
    if (arr == NULL) {
        return -1;
    }
    memset(arr, 0, (nums1Size + nums2Size) * sizeof(int));
    int l1 = 0;
    int l2 = 0;
    int count = 0;
    while (l1 < nums1Size && l2 < nums2Size) {
        if (nums1[l1] < nums2[l2]) {
            arr[count] = nums1[l1];
            count++;
            l1++;
        } else {
            arr[count] = nums2[l2];
            count++;
            l2++;
        }        
    }

    if (l1 == nums1Size && l2 < nums2Size) {
        while (count < nums1Size + nums2Size) {
            arr[count] = nums2[l2];
            count++;
            l2++;
        }
    } else if (l1 < nums1Size && l2 == nums2Size)  {
        while (count < nums1Size + nums2Size) {
            arr[count] = nums1[l1];
            count++;
            l1++;
        }
    }

    int mid = (nums1Size + nums2Size) / 2;
    bool isEven = (nums1Size + nums2Size) % 2 == 0 ? true : false;

    if (isEven) {
        return (arr[mid] + arr[mid - 1]) / 2.0;
    } else {
        return arr[mid];
    }
}
```

#### [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

**示例 1：**

> 输入：s = "babad"
> 输出："bab"
> 解释："aba" 同样是符合题意的答案。

**示例 2：**

> 输入：s = "cbbd"
> 输出："bb"


**示例 3：**

> 输入：s = "a"
> 输出："a"


**示例 4：**

> 输入：s = "ac"
> 输出："a"

**提示：**

* 1 <= s.length <= 1000
* s 仅由数字和英文字母（大写和/或小写）组成

从回文串的定义展开讨论：

* 如果一个字符串的头尾两个字符都不相等，那么这个字符串一定不是回文串；
* 如果一个字符串的头尾两个字符相等，才有必要继续判断下去。
  * 如果里面的子串是回文，整体就是回文串；
  * 如果里面的子串不是回文串，整体就不是回文串。

```c
char * longestPalindrome(char * s)
{
    int len = strlen(s);
    bool dp[len][len];
    memset(dp, false, len * len * sizeof(bool));

    int maxLen = 0;
    int begin = 0; 
    int end = 0;

    for (int i = 0; i < len; i++) {
        dp[i][i] = true;
    }
    for (int i = len - 1; i >= 0; i--) {
        for (int j = i + 1; j < len; j++) {
            dp[i][j] = (s[i] == s[j]) && (j - i <= 2 || dp[i + 1][j - 1]);

            if (dp[i][j] && j - i + 1 > maxLen) {
                maxLen = j - i + 1;
                begin = i;
                end = j;
            }   
        }
    }
    s[end + 1] = '\0';
    
    return &s[begin];
}
```

#### [6. Z 字形变换](https://leetcode-cn.com/problems/zigzag-conversion/)

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

> P   A   H   N
> A P L S I I G
> Y   I   R

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"PAHNAPLSIIGYIR"`。

请你实现这个将字符串进行指定行数变换的函数：

> string convert(string s, int numRows);

**示例 1：**

> 输入：s = "PAYPALISHIRING", numRows = 3
> 输出："PAHNAPLSIIGYIR"

**示例 2：**

> 输入：s = "PAYPALISHIRING", numRows = 4
> 输出："PINALSIGYAHRPI"
> 解释：
> P     I    N
> A   L S  I G
> Y A   H R
> P     I

**示例 3：**

> 输入：s = "A", numRows = 1
> 输出："A"

**提示：**

* 1 <= s.length <= 1000
* s 由英文字母（小写和大写）、',' 和 '.' 组成
* 1 <= numRows <= 1000

```c
char * convert(char * s, int numRows){
    if (numRows == 1) {
        return s;
    }
    int len = strlen(s);
    char arr[numRows][len];
    memset(arr,0, numRows * len * sizeof(char));

    int row = 0;
    int col = 0;
    bool isAcc = false;
    int count = 0;
    for (int i = 0; i < len; i++) {
        if (row == 0 || row == numRows - 1) {
            isAcc = !isAcc;
        }

        if (row < numRows - 1 && isAcc) {
            arr[row][col] = s[i];
            row++;
        } 

        if (row >= 0 && !isAcc) {
            arr[row][col] = s[i];
            if (row > 0) {
                row--;
            }
            col++;    
        } 
      
    }

    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < len; j++) {
            if (arr[i][j] != 0) {
                s[count++] = arr[i][j];
            }
        }
    }

    return s;
}
```

#### [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer/)

给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

**假设环境不允许存储 64 位整数（有符号或无符号）。**

**示例 1：**

> 输入：x = 123
> 输出：321

**示例 2：**

> 输入：x = -123
> 输出：-321


**示例 3：**

> 输入：x = 120
> 输出：21


**示例 4：**

> 输入：x = 0
> 输出：0

**提示：**

* $-2^{31} <= x <= 2^{31} - 1$

```c
int reverse(int x)
{
    int res = 0;
    while (x != 0) {
        if (res < INT_MIN / 10 || res > INT_MAX / 10) {
            return 0;
        }

        res = res * 10 + x % 10;
        x = x / 10;
    }

    return res;
}	
```

#### [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

* 读入字符串并丢弃无用的前导空格
* 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
* 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
  将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
* 如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
* 返回整数作为最终结果。

**注意：**

* 本题中的空白字符只包括空格字符 ' ' 。
* 除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。

**示例 1：**

> 输入：s = "42"
> 输出：42
> 解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
> 第 1 步："42"（当前没有读入字符，因为没有前导空格）
>          ^
> 第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
>          ^
> 第 3 步："42"（读入 "42"）
>            ^
> 解析得到整数 42 。
> 由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。

**示例 2：**

> 输入：s = "   -42"
> 输出：-42
> 解释：
> 第 1 步："   -42"（读入前导空格，但忽视掉）
>             ^
> 第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
>              ^
> 第 3 步："   -42"（读入 "42"）
>                ^
> 解析得到整数 -42 。
> 由于 "-42" 在范围 [-231, 231 - 1] 内，最终结果为 -42 。

**示例 3：**

> 输入：s = "4193 with words"
> 输出：4193
> 解释：
> 第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
>          ^
> 第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
>          ^
> 第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
>              ^
> 解析得到整数 4193 。
> 由于 "4193" 在范围 [-231, 231 - 1] 内，最终结果为 4193 。

**示例 4：**

> 输入：s = "words and 987"
> 输出：0
> 解释：
> 第 1 步："words and 987"（当前没有读入字符，因为没有前导空格）
>          ^
> 第 2 步："words and 987"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
>          ^
> 第 3 步："words and 987"（由于当前字符 'w' 不是一个数字，所以读入停止）
>          ^
> 解析得到整数 0 ，因为没有读入任何数字。
> 由于 0 在范围 [-231, 231 - 1] 内，最终结果为 0 。

**示例 5：**

> 输入：s = "-91283472332"
> 输出：-2147483648
> 解释：
> 第 1 步："-91283472332"（当前没有读入字符，因为没有前导空格）
>          ^
> 第 2 步："-91283472332"（读入 '-' 字符，所以结果应该是负数）
>           ^
> 第 3 步："-91283472332"（读入 "91283472332"）
>                      ^
> 解析得到整数 -91283472332 。
> 由于 -91283472332 小于范围 [-231, 231 - 1] 的下界，最终结果被截断为 -231 = -2147483648 。

**提示：**

- `0 <= s.length <= 200`
- `s` 由英文字母（大写和小写）、数字（`0-9`）、`' '`、`'+'`、`'-'` 和 `'.'` 组成

```c
int myAtoi(char * s)
{
   
    int len = strlen(s);
    int res = 0;

    int i = 0;
    while (s[i] == ' ') {
        i++;
    }

    bool isNegitive = false;
    if (s[i] == '-') {
        isNegitive = true;
        i++;
    }  else if (s[i] == '+') {
        i++;
    }

    for (i; i < len; i++) {
        if (!(s[i] >= '0' && s[i] <= '9')) {
            break;
        }

        if ( res > INT_MAX / 10 || 
                (res == INT_MAX / 10 && s[i] - '0' > INT_MAX % 10)) {
            
            return isNegitive ? INT_MIN : INT_MAX;
        }  

        res = res * 10 + (s[i] - '0');
    }

    if (isNegitive) {
        res = -res;
    }

    return res;
}
```

#### [9. 回文数](https://leetcode-cn.com/problems/palindrome-number/)

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

 **示例 1：**

> 输入：x = 121
> 输出：true


**示例 2：**

> 输入：x = -121
> 输出：false
> 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。


**示例 3：**

> 输入：x = 10
> 输出：false
> 解释：从右向左读, 为 01 。因此它不是一个回文数。


**示例 4：**

> 输入：x = -101
> 输出：false

**提示：**

- 2^31^ <= x <= 2^31^ - 1

```c
#define MAX_INT_SIZE 33
bool isPalindrome(int x){
    char s[MAX_INT_SIZE];
    memset(s, 0, MAX_INT_SIZE * sizeof(char));

    sprintf(s, "%d", x);
    int l = 0;
    int r = strlen(s) - 1;
    while (l < r) {
        if (s[l] != s[r]) {
            return false;
        }

        l++;
        r--;
    }

    return true; 
}
```

#### [10. 正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/)

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

* '.' 匹配任意单个字符
* '*' 匹配零个或多个前面的那一个元素

所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

**示例 1：**

> 输入：s = "aa" p = "a"
> 输出：false
> 解释："a" 无法匹配 "aa" 整个字符串。


**示例 2:**

> 输入：s = "aa" p = "a*"
> 输出：true
> 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。


**示例 3：**

> 输入：s = "ab" p = ".*"
> 输出：true
> 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。


**示例 4：**

> 输入：s = "aab" p = "c*a*b"
> 输出：true
> 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。


**示例 5：**

> 输入：s = "mississippi" p = "mis*is*p*."
> 输出：false

**提示：**

* 0 <= s.length <= 20
* 0 <= p.length <= 30
* s 可能为空，且只包含从 a-z 的小写字母。
* p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
* 保证每次出现字符 * 时，前面都匹配到有效的字符

```c
bool isMatch(char *s, char *p){
    int lenOfS = strlen(s);
    int lenOfP = strlen(p);

    bool dp[lenOfS + 1][lenOfP + 1];

    memset(dp, false, (lenOfS +1) * (lenOfP + 1) * sizeof(bool));
    
    dp[0][0] = true;
    for( int i = 0 ; i <= lenOfS; i++ ) {
        for(int j = 0 ; j <= lenOfP; j++ ) {       
            if (j > 0 && p[j - 1] != '*') {
                if (i > 0 && (s[i - 1] == p[j - 1] || p[j - 1] == '.')) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            } else if (j - 2 >= 0) { 
    
                dp[i][j] = dp[i][j - 2];
                if (i > 0 && (s[i - 1] == p[j - 2] || p[j - 2] == '.')) {
                    dp[i][j] |= dp[i - 1][j];
                }
            }                  
        }
    }

    return dp[lenOfS][lenOfP];
}
```

#### [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

**示例 1：**

![](img/question_11.jpg)

> 输入：[1,8,6,2,5,4,8,3,7]
> 输出：49 
> 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

**示例 2：**

> 输入：height = [1,1]
> 输出：1

**示例 3：**

> 输入：height = [4,3,2,1,4]
> 输出：16

**示例 4：**

> 输入：height = [1,2,1]
> 输出：2

**提示：**

* n = height.length
*  $2 <= n <= 3 * 10^4$
* $0 <= height[i] <= 3 * 10^4$

```c
int maxArea(int* height, int heightSize){
    int maxVal = 0;
    int l = 0;
    int r = heightSize - 1;

    while (l < r) {
        int area = fmin(height[l], height[r]) * (r - l);
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }

        if (area > maxVal) {
            maxVal = area;
        }
    }

    return maxVal;
}
```

#### [12. 整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/)

罗马数字包含以下七种字符： `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

> 字符          数值
> I             1
> V             5
> X             10
> L             50
> C             100
> D             500
> M             1000

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

* I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
* X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
* C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

**示例 1:**

> 输入: 3
> 输出: "III"


**示例 2:**

> 输入: 4
> 输出: "IV"


**示例 3:**

> 输入: 9
> 输出: "IX"


**示例 4:**

> 输入: 58
> 输出: "LVIII"
> 解释: L = 50, V = 5, III = 3.


**示例 5:**

> 输入: 1994
> 输出: "MCMXCIV"
> 解释: M = 1000, CM = 900, XC = 90, IV = 4.

**提示：**

* 1 <= num <= 3999

```c
#define MAX_SIZE 100

char * intToRoman(int num)
{
    char *res = (char *)malloc(MAX_SIZE * sizeof(char));
    if (res == NULL) {
        return NULL;
    }
    memset(res, 0, MAX_SIZE * sizeof(char));

    int nums[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char *romans[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    int count = 0;
    while (num > 0) {
        for (int i = 0; i < 13; i++) {
            if (num >= nums[i]) {
                strcpy(&res[count],romans[i]);
                count += strlen(romans[i]);
                num -= nums[i];
                break;
            }
        }
    }

    return res;
}
```

#### [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

> 字符          数值
> I             1
> V             5
> X             10
> L             50
> C             100
> D             500
> M             1000


例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

* I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
* X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
* C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

**示例 1:**

> 输入: "III"
> 输出: 3


**示例 2:**

> 输入: "IV"
> 输出: 4


**示例 3:**

> 输入: "IX"
> 输出: 9


**示例 4:**

> 输入: "LVIII"
> 输出: 58
> 解释: L = 50, V= 5, III = 3.


**示例 5:**

> 输入: "MCMXCIV"
> 输出: 1994
> 解释: M = 1000, CM = 900, XC = 90, IV = 4.

**提示：**

* 1 <= s.length <= 15
* s 仅含字符 ('I', 'V', 'X', 'L', 'C', 'D', 'M')
* 题目数据保证 s 是一个有效的罗马数字，且表示整数在范围 [1, 3999] 内
* 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
* IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
* 关于罗马数字的详尽书写规则，可以参考 [罗马数字 - Mathematics](https://b2b.partcommunity.com/community/knowledge/zh_CN/detail/10753/罗马数字#knowledge_article)。

```c
int romanToInt(char* s) {
    int symbolValues[26];
    symbolValues['I' - 'A'] = 1;
    symbolValues['V' - 'A'] = 5;
    symbolValues['X' - 'A'] = 10;
    symbolValues['L' - 'A'] = 50;
    symbolValues['C' - 'A'] = 100;
    symbolValues['D' - 'A'] = 500;
    symbolValues['M' - 'A'] = 1000;
    int ans = 0;
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        int value = symbolValues[s[i] - 'A'];
        if (i < n - 1 && value < symbolValues[s[i + 1] - 'A']) {
            ans -= value;
        } else {
            ans += value;
        }
    }
    return ans;
}

```

#### [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。 

**示例 1：**

> 输入：strs = ["flower","flow","flight"]
> 输出："fl"


**示例 2：**

> 输入：strs = ["dog","racecar","car"]
> 输出：""
> 解释：输入不存在公共前缀。

**提示：**

* 0 <= strs.length <= 200
* 0 <= strs[i].length <= 200
* strs[i] 仅由小写英文字母组成

```c
char * longestCommonPrefix(char ** strs, int strsSize)
{
    if (strsSize == 1) {
        return strs[0];
    }
    
    int max_len = strlen(strs[0]);
    for (int i = 1; i < strsSize; i++) {
        int j;
        for (j = 0; j < fmin(strlen(strs[i]), max_len); j++) {
            if (strs[i][j] != strs[0][j] ) {
                break;
            }       
        }

        if (max_len > j) {
            max_len = j;
        }
        if (max_len == 0) {
            return "";
        }
    }

    strs[0][max_len] = '\0';
    return strs[0];
}
```

#### [15. 三数之和](https://leetcode-cn.com/problems/3sum/)

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

**示例 1：**

> 输入：nums = [-1,0,1,2,-1,-4]
> 输出：[[-1,-1,2],[-1,0,1]]


**示例 2：**

> 输入：nums = []
> 输出：[]


**示例 3：**

> 输入：nums = [0]
> 输出：[]

**提示：**

* 0 <= nums.length <= 3000
* $-105 <= nums[i] <= 10^5$

```c
int Cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes)
{
    qsort(nums, numsSize, sizeof(int), Cmp);

    int **res = (int **)malloc(numsSize  * numsSize * sizeof(int *));
    if (res == NULL) {
        return NULL;
    }
    memset(res, 0,numsSize  * numsSize * sizeof(int *));
    int size = 0;

    *returnColumnSizes = (int *)malloc(numsSize  * numsSize * sizeof(int));
    if (*returnColumnSizes == NULL) {
        return NULL;
    }

    for (int i = 0; i < numsSize - 2; i++) {
        if (nums[i] > 0) {
            break;
        }
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }
        int l = i + 1;
        int r = numsSize - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
         
            if (sum == 0) {
                int *tmp = (int *)malloc(3 * sizeof(int));
                if (tmp == NULL) {
                    return NULL;
                }
                tmp[0] = nums[i];
                tmp[1] = nums[l];
                tmp[2] = nums[r];
                
               
                res[size] = tmp;
                (*returnColumnSizes)[size] = 3;
                size++;

                while (l < r && nums[l] == nums[l + 1]) {
                    l++;
                }
                l++;
                r--;
            } else if (sum > 0) {
                r--;
            } else {
                l++;
            }
        }
    }
    
    *returnSize = size;
    
    return res;
}
```

#### [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 **示例：**

> 输入：nums = [-1,2,1,-4], target = 1
> 输出：2
> 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

**提示：**

* 3 <= nums.length <= 10^3^
* -10^3^ <= nums[i] <= 10^3^
* -10^4^ <= target <= 10^4^

```c
int Cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int threeSumClosest(int* nums, int numsSize, int target){
    qsort(nums, numsSize, sizeof(int), Cmp);

    int res = nums[0] + nums[1] + nums[2];

    for (int i = 0; i < numsSize - 2; i++) {
        int l = i + 1;
        int r = numsSize - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];

            if (abs(sum - target) < abs(res - target)) {
                res = sum;
            }
            if (sum > target) {
                r--;
            } else if (sum < target){
                l++;
            } else {
                return target;
            }
        }
    }
    
    return res; 
}
```

#### [17. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](img/17_telephone_keypad.png)

**示例 1：**

> 输入：digits = "23"
> 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]


**示例 2：**

> 输入：digits = ""
> 输出：[]


**示例 3：**

> 输入：digits = "2"
> 输出：["a","b","c"]

**提示：**

> 0 <= digits.length <= 4
> digits[i] 是范围 ['2', '9'] 的一个数字。

```c
#define MAX_SIZE 4*4*4*4

char *words[] = 
{
    "",
    "",
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
};

void Dfs(char *digits, char *cur, int index, char **res, int *sizeOfRes)
{
    if (index == strlen(digits)) {
        char *tmp = (char *)malloc((index + 1) * sizeof(char));
        for (int i = 0; i < index; i++) {
            tmp[i] = cur[i];
        }
        tmp[index] = '\0';

        res[(*sizeOfRes)++] = tmp;
        return;
    }

    char *word = words[digits[index] - '0'];
    for (int i = 0; i < strlen(word); i++) {
        cur[index] = word[i];
        Dfs(digits, cur, index + 1, res, sizeOfRes);
    }
}

char ** letterCombinations(char * digits, int* returnSize){

    char **res = (char **)malloc(MAX_SIZE * sizeof(char *));
    if (res == NULL) {
        return NULL;
    }
    int sizeOfRes = 0;
    
    char *cur = (char *)malloc(5 * sizeof(char));
    int index = 0;
    
    if (strlen(digits) == 0) {
       *returnSize = 0;
       return NULL;
    }

    Dfs(digits, cur, index, res, &sizeOfRes);
    *returnSize = sizeOfRes;

    return res;
}
```

#### [18. 四数之和](https://leetcode-cn.com/problems/4sum/)

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

**注意：**答案中不可以包含重复的四元组。

**示例 1：**

> 输入：nums = [1,0,-1,0,-2,2], target = 0
> 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


**示例 2：**

> 输入：nums = [], target = 0
> 输出：[]

**提示：**

* 0 <= nums.length <= 200
* -10^9^<= nums[i] <= 10^9^
* -10^9^ <= target <= 10^9^

```c
#define MAX_SIZE 200 * 4

int Cmp(const void *a, const void *b)
{
    return *(int *)a - *(int *)b;
}

int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes){
    int **res = (int **)malloc(MAX_SIZE * sizeof(int *));
    if (res == NULL) {
        return NULL;
    }
    int sizeOfRes = 0;

    *returnColumnSizes = (int *)malloc(MAX_SIZE * sizeof(int));
    if (*returnColumnSizes == NULL) {
        return NULL;
    }

    qsort(nums, numsSize, sizeof(int), Cmp);

    for (int i = 0; i < numsSize - 3; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) {
            continue;
        }

        if((long long)nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) {
            break;
        }

        for (int j = i + 1; j < numsSize - 2; j++) {
            if (j > i + 1 && nums[j] == nums[j - 1]) {
                continue;
            }
            int l = j + 1;
            int r = numsSize - 1;

            while (l < r) {

                long long sum = (long long)nums[i] + nums[j] + nums[l] + nums[r];

                if (sum == target) {
                    int *tmp = (int *) malloc(4 * sizeof(int));
                    if (tmp == NULL) {
                        return NULL;
                    }

                    tmp[0] = nums[i];
                    tmp[1] = nums[j];
                    tmp[2] = nums[l];
                    tmp[3] = nums[r];

                    res[sizeOfRes] = tmp;
                    (*returnColumnSizes)[sizeOfRes] = 4;
                    sizeOfRes++;

                    while (l < r && nums[l] == nums[l + 1]) {
                        l++;
                    }
                    l++;
                    r--;
                } else if (sum > target) {
                    r--;
                } else {
                    l++;
                }
            }
        }
    }

    *returnSize = sizeOfRes;
    return res;
}
```

#### [19. 删除链表的倒数第 N 个结点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

**进阶：**你能尝试使用一趟扫描实现吗？

**示例 1：**

![](img/remove_ex1.jpg)

> 输入：head = [1,2,3,4,5], n = 2
> 输出：[1,2,3,5]


**示例 2：**

> 输入：head = [1], n = 1
> 输出：[]


**示例 3：**

> 输入：head = [1,2], n = 1
> 输出：[1]

**提示：**

* 链表中结点的数目为 sz
* 1 <= sz <= 30
* 0 <= Node.val <= 100
* 1 <= n <= sz

```c
struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *fast = head;
    for (int i = 0; i < n; i++) {
        fast = fast->next;
    }

    if(fast == NULL) {
        return head->next;   //说明删除的是头节点
    }
    struct ListNode *slow = head;
    struct ListNode *pre = NULL;
    while (fast != NULL) {
        fast = fast->next;
        pre = slow;
        slow = slow ->next;
    }

    
    pre->next = pre->next->next;
    
    return head;
}
```

#### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

**示例 1：**

> 输入：s = "()"
> 输出：true


**示例 2：**

> 输入：s = "()[]{}"
> 输出：true


**示例 3：**

> 输入：s = "(]"
> 输出：false


**示例 4：**

> 输入：s = "([)]"
> 输出：false


**示例 5：**

> 输入：s = "{[]}"
> 输出：true

**提示：**

* 1 <= s.length <= 10^4^
* s 仅由括号 '()[]{}' 组成

```c
# define MAX_SIZE 10001
char GetPairs(char a) {
    if (a == '}') return '{';
    if (a == ']') return '[';
    if (a == ')') return '(';
    return 0;
}

bool isValid(char * s){
    char stack[MAX_SIZE];
    memset(stack, 0, MAX_SIZE * sizeof(char));
    int top = 0;

    int len = strlen(s);
     if (len % 2 == 1) {
        return false;
    }
    for (int i = 0; i < len; i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            stack[top++] = s[i];
        } else {
            char tmp = GetPairs(s[i]);
       
            if (tmp != 0 && top > 0 && tmp == stack[top - 1]) {
                top--;
            } else {
                return false;
            }
        }
        
        
    }

    if (top != 0) {
        return false;
    } 
    
    return true;
   
}
```

#### [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例 1：**

![](img/merge_ex1.jpg)

> 输入：l1 = [1,2,4], l2 = [1,3,4]
> 输出：[1,1,2,3,4,4]

**示例 2：**

> 输入：l1 = [], l2 = []
> 输出：[]


**示例 3：**

> 输入：l1 = [], l2 = [0]
> 输出：[0]

**提示：**

* 两个链表的节点数目范围是 [0, 50]
* -100 <= Node.val <= 100
* l1 和 l2 均按 非递减顺序 排列

```c
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode * res = (struct ListNode *)malloc(sizeof(struct ListNode));
    if (res == NULL) {
        return NULL;
    }
    memset(res, 0, sizeof(struct ListNode));

    struct ListNode *p = res;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val < list2->val) {
            p->next = list1;
            list1 = list1->next;
        } else {
            p->next = list2;
            list2 = list2->next;
        }
        p = p->next;
    }

    if (list1 == NULL && list2 != NULL) {
        p->next = list2;
    } else if (list1 != NULL && list2 == NULL) {
        p->next = list1;
    }

    return res->next;
}
```

#### [22. 括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。 

**示例 1：**

> 输入：n = 3
> 输出：["((()))","(()())","(())()","()(())","()()()"]

**示例 2：**

> 输入：n = 1
> 输出：["()"]

**提示：**

* 1 <= n <= 8

```c
#define MAX_SIZE 10001

void GetParenthesis(char *str,int left, int right, int len, char **res, int *sizeofRes)
{
    if(left == 0 && right == 0 ){
        char *tmp = (char *)malloc((len + 1) * sizeof(char));
        for (int i = 0; i < len; i++) {
            tmp[i] = str[i];
        }
        tmp[len] = '\0';

        res[(*sizeofRes)++] = tmp;
        return;
    }
    if(left == right){
        //剩余左右括号数相等，下一个只能用左括号
        str[len] = '(';
        GetParenthesis(str,left-1, right, len + 1, res, sizeofRes);
    }else if(left < right){
        //剩余左括号小于右括号，下一个可以用左括号也可以用右括号
        if(left > 0){
            str[len] = '(';
            GetParenthesis(str,left-1, right, len + 1, res, sizeofRes);
        }
        str[len] = ')';
        GetParenthesis(str, left, right-1, len + 1, res, sizeofRes);
    }
}

char ** generateParenthesis(int n, int* returnSize){
    char **res = (char **)malloc(MAX_SIZE * sizeof(char *));
    int sizeofRes = 0;

    char *s = (char *)malloc((n * 2 + 1) * sizeof(char));
    memset(s, 0, (n * 2 + 1) * sizeof(char));
    GetParenthesis(s, n, n, 0, res, &sizeofRes);

    *returnSize = sizeofRes;
    return res;
}
```

#### [23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

**示例 1：**

> 输入：lists = [[1,4,5],[1,3,4],[2,6]]
> 输出：[1,1,2,3,4,4,5,6]
> 解释：链表数组如下：
> [
>   1->4->5,
>   1->3->4,
>   2->6
> ]
> 将它们合并到一个有序链表中得到。
> 1->1->2->3->4->4->5->6

**示例 2：**

> 输入：lists = []
> 输出：[]


**示例 3：**

> 输入：lists = [[]]
> 输出：[]

**提示：**

* k == lists.length
* 0 <= k <= 10^4^
* 0 <= lists[i].length <= 500
* -10^4^ <= lists[i ]  [ j ] <= 10^4^
* lists[i] 按 升序 排列
* lists[i].length 的总和不超过 10^4^

```c
struct ListNode * MergeTwoList(struct ListNode *a, struct ListNode *b)
{
    if (a == NULL || b == NULL) {
        return a == NULL ? b : a;
    }

    struct ListNode *tmpA = a;
    struct ListNode *tmpB = b;

    struct ListNode *dummy = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *p = dummy;
    while (tmpA != NULL && tmpB != NULL) {
        if (tmpA->val < tmpB->val) {
            p->next = tmpA;
            tmpA = tmpA->next;
        } else {
            p->next = tmpB;
            tmpB = tmpB->next;  
        }
        p = p->next;
    }

    if (tmpA == NULL) {
        p->next = tmpB;
    } else {
        p->next = tmpA;
    }

    return dummy->next;
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize){
    struct ListNode *p = NULL;

    for (int i = 0; i < listsSize; i++) {
        p = MergeTwoList(p, lists[i]);
    }

    return p;
}
```

#### [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

**你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

**示例 1：**

![](img/swap_ex1.jpg)

> 输入：head = [1,2,3,4]
> 输出：[2,1,4,3]

**示例 2：**

> 输入：head = []
> 输出：[]

**示例 3：**

> 输入：head = [1]
> 输出：[1]

**提示：**

   * 链表中节点的数目在范围 [0, 100] 内
   * 0 <= Node.val <= 100

```c
struct ListNode* swapPairs(struct ListNode* head){

    struct ListNode *dummy = (struct ListNode *)malloc(sizeof(struct ListNode));
    dummy->next = head;
    struct ListNode *cur = dummy;

    while (head != NULL && head->next != NULL) {
        cur->next = head->next;
        struct ListNode *tmp = head->next->next;
        head->next->next = head;
        head->next = tmp;
       
        cur = head;
        head = tmp;
    }

    return dummy->next;
}
```

#### [25. K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

**进阶：**

* 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
* 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**示例 1：**

![](img/reverse_ex1.jpg)

> 输入：head = [1,2,3,4,5], k = 2
> 输出：[2,1,4,3,5]

**示例 2：**

![](img/reverse_ex2.jpg)

> 输入：head = [1,2,3,4,5], k = 3
> 输出：[3,2,1,4,5]

**示例 3：**

> 输入：head = [1,2,3,4,5], k = 1
> 输出：[1,2,3,4,5]


**示例 4：**

> 输入：head = [1], k = 1
> 输出：[1]


**提示：**

*  列表中节点的数量在范围 sz 内
*  1 <= sz <= 5000
*  0 <= Node.val <= 1000
*  1 <= k <= sz

```c
struct ListNode * ReverseListNode(struct ListNode * head)
{
    if (head == NULL || head->next == NULL) {
        return head;
    }

    struct ListNode *pre = NULL;
    struct ListNode *cur = head;

    while (cur != NULL) {
        struct ListNode *tmp = cur->next;
        cur->next = pre;
        pre = cur;
        cur = tmp;
    }

    return pre;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k){
    if (head == NULL || head->next == NULL){
        return head;
    }
        
    struct ListNode *dummy = (struct ListNode *)malloc(sizeof(struct ListNode));
    dummy->next=head;
  
    struct ListNode *pre = dummy;
    struct ListNode *end = dummy;

    while (end->next != NULL) {
        
        for (int i = 0; i < k && end != NULL; i++) {
            end=end->next;
        }
       
        if (end == NULL) {
            break;
        }
        
        struct ListNode *next = end->next;
        end->next=NULL;
        
        struct ListNode *start = pre->next;
       
        pre->next = ReverseListNode(start);
        start->next = next;
        
        pre = start;
        end = start;
    }
    return dummy->next;
}
```

#### [26. 删除有序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

给你一个有序数组 nums ，请你 **原地** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 **原地 修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以**「引用」**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

**示例 1：**

> 输入：nums = [1,1,2]
> 输出：2, nums = [1,2]
> 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。


**示例 2：**

> 输入：nums = [0,0,1,1,1,2,2,3,3,4]
> 输出：5, nums = [0,1,2,3,4]
> 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

**提示：**

*  0 <= nums.length <= 3 * 10^4^
*  -10^4^ <= nums[i] <= 10^4^
*  nums 已按升序排列

```c
int removeDuplicates(int* nums, int numsSize){
    if (numsSize == 0) {
        return 0;
    }

    int l = 1;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == nums[i - 1]) {
            continue;
        }
        nums[l] = nums[i];
        l++;
    }

    return l;
}
```

#### [27. 移除元素](https://leetcode-cn.com/problems/remove-element/)

给你一个数组 nums 和一个值 val，你需要 **原地** 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 **原地 修改输入数组**。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以**「引用」**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

**示例 1：**

> 输入：nums = [3,2,2,3], val = 3
> 输出：2, nums = [2,2]
> 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。


**示例 2：**

> 输入：nums = [0,1,2,2,3,0,4,2], val = 2
> 输出：5, nums = [0,1,4,0,3]
> 解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

**提示：**

*  0 <= nums.length <= 100
* 0 <= nums[i] <= 50
* 0 <= val <= 100

```c
int removeElement(int* nums, int numsSize, int val){
    int l = 0;
    
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == val) {
            continue;
        }
        nums[l++] = nums[i];
    }

    return l;
}
```

#### [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

**示例 1:**

> 输入: haystack = "hello", needle = "ll"
> 输出: 2

**示例 2:**

> 输入: haystack = "aaaaa", needle = "bba"
> 输出: -1


**说明:**

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

```c
int * kmpNext(char * haystack) {
    
    int len = strlen(haystack);
    int *next = (int *)malloc(len * sizeof(int));
   
    next[0] = 0; 
    for(int i = 1, j = 0; i < len; i++) {
        while(j > 0 &&haystack[i] != haystack[j]) {
            j = next[j - 1];
        }

        if(haystack[i] == haystack[j]) {
            j++;
        }
        next[i] = j; 
    }
    return next;
}

int strStr(char * haystack, char * needle){
    int *next = kmpNext(needle); //先得到next数组
    int lenOfHaystack = strlen(haystack);
    int lenOfneedle = strlen(needle);
    int i, j = 0;
    for( i = 0 ; i < lenOfHaystack && j < lenOfneedle; i++){
        
        while( j > 0 && haystack[i] != needle[j]) {
            j = next[j-1]; 
        }
        
        if (haystack[i] == needle[j]){ 
            j++;
        }

        if (j == lenOfneedle) {
            return i - j + 1;
        }
    }
    
    return -1;
}
```

#### [29. 两数相除](https://leetcode-cn.com/problems/divide-two-integers/)

给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

示例 1:

> 输入: dividend = 10, divisor = 3
> 输出: 3
> 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:

> 输入: dividend = 7, divisor = -3
> 输出: -2
> 解释: 7/-3 = truncate(-2.33333..) = -2


提示：

* 被除数和除数均为 32 位有符号整数。
* 除数不为 0。
* 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

```c
int divide(int dividend, int divisor){
    bool isPositive = true; //全都转为负数计算，因为负数比正数多一个，负转正不好转

    if (dividend > 0) {
        dividend = -dividend;
        isPositive = !isPositive;
    }

    if (divisor > 0) {
        divisor = -divisor;
        isPositive = !isPositive;
    }

    long count = 0;    // 这里有可能是2147483647 + 1
    long douCount = 1; // 这里可能是2147483647 * 2
    while (dividend <= douCount * divisor) {
        dividend -= douCount * divisor;
        count += douCount;
        douCount *= 2;
    }
    
    while (dividend <= divisor) {
        dividend -= divisor;
        count++;
    }

    if (!isPositive) {
        return (int)-1 * count;
    }
    
    return count > INT_MAX ? INT_MAX : count;
}
```

#### [30. 串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。

 示例 1：

> 输入：s = "barfoothefoobarman", words = ["foo","bar"]
> 输出：[0,9]
> 解释：
> 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
> 输出的顺序不重要, [9,0] 也是有效答案。

示例 2：

> 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
> 输出：[]

示例 3：

> 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
> 输出：[6,9,12]


提示：

* 1 <= s.length <= 104
* s 由小写英文字母组成
* 1 <= words.length <= 5000
* 1 <= words[i].length <= 30
* words[i] 由小写英文字母组成

```

```

#### [31. 下一个排列](https://leetcode-cn.com/problems/next-permutation/)

整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

* 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。

整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

* 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
* 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
* 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。

给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。

示例 1：

> 输入：nums = [1,2,3]
> 输出：[1,3,2]

示例 2：

> 输入：nums = [3,2,1]
> 输出：[1,2,3]

示例 3：

> 输入：nums = [1,1,5]
> 输出：[1,5,1]


提示：

* 1 <= nums.length <= 100
* 0 <= nums[i] <= 100

这个题目的意思就是说从一个深度优先的排列中找它的下一个排列，如下图所示：
![](E:/大三下/leetcode/leetcode-notebook/java/img/image-20210918164850606.png)

对于一个深度优先的全排列来说，可以很明显的看到bac的下一个排列就是bca，而且满足关系bac < bca。

从右往左找到第一个破坏降序序列的元素i，然后从右往左找到第一个比i大的元素j，j也是整个降序序列中最接近i的元素，然后将它们交换。这时j后面的元素还是降序的，需要将它们转为升序。

整体的时间复杂度是O(n)

```c
void Swap(int *nums, int i, int j){
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp; 
}

void Reverse(int *nums, int l, int r) {
    while(l < r){
        Swap(nums, l, r);
        l++;
        r--;
    }
}

void nextPermutation(int* nums, int numsSize){
    int i = numsSize - 2;

    while(i >= 0 && nums[i] >= nums[i + 1]) 
        i--;
    if (i >= 0) {
        int j = numsSize - 1;

        while( j >= 0 && nums[j] <= nums[i])
            j--;                 
        Swap(nums,i,j);
        
    }

    Reverse(nums, i + 1, numsSize - 1);
}
```

#### [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 

示例 1：

> 输入：s = "(()"
> 输出：2
> 解释：最长有效括号子串是 "()"

示例 2：

> 输入：s = ")()())"
> 输出：4
> 解释：最长有效括号子串是 "()()"

示例 3：

> 输入：s = ""
> 输出：0


提示：

* 0 <= s.length <= 3 * 104
* s[i] 为 '(' 或 ')'

```c
//正向逆向结合
int longestValidParentheses(char * s)
{
    int l = 0;
    int r = 0;
    int maxLen = 0;

    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            l++;
        }

        if (s[i] == ')') {
            r++;
        }
    
        if (l < r) {
            r = 0;
            l = 0;
        } else if (l == r && maxLen < l + r) {
            maxLen = l + r;
        }
    }

    l = r = 0;
    for (int i = len - 1; i >= 0; i--) {
        if (s[i] == ')') {
            r++;
        }

        if (s[i] == '(') {
            l++;
        }

        if (r < l) {
            r = 0;
            l = 0;
        } else if (l == r && maxLen < l + r) {
            maxLen = l + r;
        }
    }

    return maxLen;
}
```

```c
//栈
int longestValidParentheses(char * s)
{
    int stack[3 * 10000];
    int size = 0;

    stack[size++] = -1;  // 表示s被下标为-1的位置分成了两部分
    int len = strlen(s);

    int maxLen = 0;
    for (int i = 0; i < len; i++) {
        if (s[i] == '(') {
            stack[size++] = i;
        }
        if (s[i] == ')') {
            size--;

            if (size > 0) {
                int curLen = i - stack[size - 1];
                if (maxLen < curLen) {
                    maxLen = curLen;
                }
            } else { //当前栈为空，说明这个')'就是用来分割的，将它入栈
                stack[size++] = i;
            }
        }
    }

    return maxLen;
}
```

#### [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。 

示例 1：

> 输入：nums = [4,5,6,7,0,1,2], target = 0
> 输出：4

示例 2：

> 输入：nums = [4,5,6,7,0,1,2], target = 3
> 输出：-1

示例 3：

> 输入：nums = [1], target = 0
> 输出：-1


提示：

* 1 <= nums.length <= 5000
* -10^4 <= nums[i] <= 10^4
* nums 中的每个值都 独一无二
* 题目数据保证 nums 在预先未知的某个下标上进行了旋转
* -10^4 <= target <= 10^4


进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？



**这道题的整体思路如下：**

​				如果mid在第一段的升序序列：

​							如果 target < mid，target可能在前半段，也可能在后半段；

​							否则，target只能在后半段。				

​             mid在第二段的升序序列：

​							如果target > mid，target可能在后半段也可能在前半段；

​							否则，target只能在前半段。

代码如下：

```c
int search(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize - 1;

    while (l <= r) {
        int mid = l + (r - l) / 2;

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] >= nums[l]) {
            if (nums[mid] > target) { // target可能在左，也可能在右
                if(target < nums[l]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } else {
                l = mid + 1;
            }
        } else {
            if (nums[mid] < target) { // target可能在左，也可能在右
                if(target < nums[l]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } else {
                r = mid - 1;
            }
        }
    }

    return -1;
}
```

我们观察上面的代码块会发现，有很多的判断语句可以合并起来，使得代码看上去更加简洁。但是可读性将会变差，如下所示：

```c
int search(int* nums, int numsSize, int target){
    int l = 0;
    int r = numsSize - 1;

    while (l <= r) {
        int mid = l + (r - l) / 2;

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] >= nums[l]) {
            if (nums[mid] > target && target >= nums[l]) {                
                r = mid - 1;          
            } else {
                l = mid + 1;
            }
        } else {
            if (nums[mid] < target && target < nums[l]) { 
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
    }

    return -1;
}
```

#### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


示例 1：

> 输入：nums = [5,7,7,8,8,10], target = 8
> 输出：[3,4]

示例 2：

> 输入：nums = [5,7,7,8,8,10], target = 6
> 输出：[-1,-1]

示例 3：

> 输入：nums = [], target = 0
> 输出：[-1,-1]


提示：

* 0 <= nums.length <= 105
* -109 <= nums[i] <= 109
* nums 是一个非递减数组
* -109 <= target <= 109

```c
int BinarySearch(int *nums, int l, int r,int target)
{
    int ans = r;
    while (l <= r) {
        int mid = l + (r -l) / 2;
        if (nums[mid] >= target) {
            ans = mid;
            r = mid - 1;
        } else {
            l++;
        }
    }
    return ans;
}

int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    int *res = (int *)malloc(*returnSize * sizeof(int));
    if (res == NULL) {
        return NULL;
    } 
    memset(res, -1, *returnSize *sizeof(int));

    if (numsSize == 0) {
        return res;
    }
    int left = BinarySearch(nums, 0, numsSize - 1, target);
    int right = BinarySearch(nums, 0, numsSize - 1, target + 1);
    
    if (nums[left] == target) {
        res[0] = left;
    }
   
    if (res[0] != -1 ) {
        if (right == numsSize - 1) {
            res[1] = nums[right] == target ? right : right - 1; 
        } else {
            res[1] = right - 1;
        }
       
    }
    
    return res;
}
```

#### [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 示例 1:

> 输入: nums = [1,3,5,6], target = 5
> 输出: 2

示例 2:

> 输入: nums = [1,3,5,6], target = 2
> 输出: 1

示例 3:

> 输入: nums = [1,3,5,6], target = 7
> 输出: 4


提示:

* 1 <= nums.length <= 104
* -104 <= nums[i] <= 104
* nums 为 无重复元素 的 升序 排列数组
* -104 <= target <= 104

```c
int searchInsert(int* nums, int numsSize, int target)
{
    int ans = numsSize - 1;
    int l = 0;
    int r = numsSize - 1;

    int mid;
    while (l <= r) {
        mid = l + (r - l) / 2;
        if (nums[mid] >= target) {
            ans = mid;
            r = mid - 1;
        } else {
            l = l + 1;
        }
    }

    if (ans == numsSize - 1 && target > nums[numsSize - 1]) {
        ans = numsSize;
    }

    return ans;
}
```

#### [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)

请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）


注意：

* 一个有效的数独（部分已被填充）不一定是可解的。
* 只需要根据以上规则，验证已经填入的数字是否有效即可。
* 空白格用 '.' 表示。

示例 1：

![](img/250px-sudoku-by-l2g-20050714svg.png)

> 输入：board = 
> [["5","3",".",".","7",".",".",".","."]
> ,["6",".",".","1","9","5",".",".","."]
> ,[".","9","8",".",".",".",".","6","."]
> ,["8",".",".",".","6",".",".",".","3"]
> ,["4",".",".","8",".","3",".",".","1"]
> ,["7",".",".",".","2",".",".",".","6"]
> ,[".","6",".",".",".",".","2","8","."]
> ,[".",".",".","4","1","9",".",".","5"]
> ,[".",".",".",".","8",".",".","7","9"]]
> 输出：true

示例 2：

> 输入：board = 
> [["8","3",".",".","7",".",".",".","."]
> ,["6",".",".","1","9","5",".",".","."]
> ,[".","9","8",".",".",".",".","6","."]
> ,["8",".",".",".","6",".",".",".","3"]
> ,["4",".",".","8",".","3",".",".","1"]
> ,["7",".",".",".","2",".",".",".","6"]
> ,[".","6",".",".",".",".","2","8","."]
> ,[".",".",".","4","1","9",".",".","5"]
> ,[".",".",".",".","8",".",".","7","9"]]
> 输出：false
> 解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。


提示：

* board.length == 9
* board[i].length == 9
* board[i]  [j] 是一位数字（1-9）或者 '.'

```c
bool isValidSudoku(char** board, int boardSize, int* boardColSize)
{
    int rowArr[boardSize][9];
    memset(rowArr, 0, boardSize * 9 * sizeof(int));
    int colArr[boardColSize[0]][9];
    memset(colArr, 0, boardColSize[0] * 9 * sizeof(int));
    int subArr[boardSize / 3][boardColSize[0] / 3][9];
    memset(subArr, 0, (boardSize / 3) * (boardColSize[0] / 3) * 9 * sizeof(int));

    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < boardColSize[i]; j++) {
            if (board[i][j] == '.') {
                continue;
            }
            int index = board[i][j] - '0' - 1; // 下标0-8表示1-9
            rowArr[i][index] += 1;
            colArr[j][index] += 1;
            subArr[i / 3][j / 3][index] += 1;

            if (rowArr[i][index] > 1 || colArr[j][index] > 1 
                	|| subArr[i / 3][j / 3][index] > 1) {
                return false;
            }
        }
    }

    return true;
}
```

#### [37. 解数独](https://leetcode-cn.com/problems/sudoku-solver/)

编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

* 数字 1-9 在每一行只能出现一次。
* 数字 1-9 在每一列只能出现一次。
* 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1：

![](img/250px-sudoku-by-l2g-20050714svg (1).png)

> 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
> 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
> 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
>
> ![](img/250px-sudoku-by-l2g-20050714_solutionsvg.png)


提示：

* board.length == 9
* board[i].length == 9
* board[i][j] 是一位数字或者 '.'
* 题目数据 保证 输入数独仅有一个解

```c
bool Dfs(char **board, bool rowArr[9][9], bool colArr[9][9], bool subArr[3][3][9], int row, int col)
{
    if (col == 9) {
        col = 0;
        row += 1;
        if (row == 9) {
            return true;
        }
    }

    if (board[row][col] == '.') {
        for (int index = 0; index < 9; index++) {
            if (rowArr[row][index] == true || colArr[col][index] == true 
                	|| subArr[row / 3][col / 3][index] == true) {
                continue;
            }
        
            board[row][col] = (char)('0' + index + 1);
            
            rowArr[row][index] = true;
            colArr[col][index] = true;
            subArr[row / 3][col / 3][index] = true;

            bool isTrue = Dfs(board, rowArr, colArr, subArr, row, col + 1);
            if (isTrue) {
                return true;
            }

            board[row][col] = '.';
            rowArr[row][index] = false;
            colArr[col][index] = false;
            subArr[row / 3][col / 3][index] = false;
        }   
    } else {
        return Dfs(board, rowArr, colArr, subArr, row, col + 1);
    }
    
    return false;
}
void solveSudoku(char** board, int boardSize, int* boardColSize){
    
    bool rowArr[boardSize][9];
    memset(rowArr, false, boardSize * 9 * sizeof(bool));
    bool colArr[boardColSize[0]][9];
    memset(colArr, false, boardColSize[0] * 9 * sizeof(bool));
    bool subArr[3][3][9];
    memset(subArr, false, 3 * 3 * 9 * sizeof(bool));

    for (int i = 0; i < boardSize; i++) {
        for (int j = 0; j < boardColSize[0]; j++) {
            if (board[i][j] == '.') {
                continue;
            }

            int index = board[i][j] - '0' - 1; // 下标0-8表示1-9
            rowArr[i][index] = true;
            colArr[j][index] = true;
            subArr[i / 3][j / 3][index] = true;
        }
    }

    Dfs(board, rowArr, colArr, subArr, 0, 0);
}
```

#### [38. 外观数列](https://leetcode-cn.com/problems/count-and-say/)

给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

* countAndSay(1) = "1"
* countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

前五项如下：

> 1.     1
> 2.     11
> 3.     21
> 4.     1211
> 5.     111221
> 第一项是数字 1 
> 描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
> 描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
> 描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
> 描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
>

要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。

例如，数字字符串 "3322251" 的描述如下图：

![](img/1629874763-TGmKUh-image.png)


示例 1：

> 输入：n = 1
> 输出："1"
> 解释：这是一个基本样例。

示例 2：

> 输入：n = 4
> 输出："1211"
>
> 解释：
> countAndSay(1) = "1"
> countAndSay(2) = 读 "1" = 一 个 1 = "11"
> countAndSay(3) = 读 "11" = 二 个 1 = "21"
> countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"


提示：

* 1 <= n <= 30

```c
char * countAndSay(int n)
{
    char *result = malloc(sizeof(char) * 10000);
    int size = 0;
  
    if (n == 1) {
        return "1";
    }
        
    char *tmp = countAndSay(n - 1);
    int len = strlen(tmp);
   
    int count = 1;
    for (int i = 0; i < len; i++) {
       
        if (i < len && tmp[i] == tmp[i + 1]) {
            count++;
        } else {       
            result[size++] = count + '0';
            result[size++] = tmp[i];
            count = 1;
        }
    }

    result[size] = '\0';
    return result;

}
```

#### [39. 组合总和](https://leetcode-cn.com/problems/combination-sum/)

给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 示例 1：

> 输入：candidates = [2,3,6,7], target = 7
> 输出：[[2,2,3],[7]]
> 解释：
> 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
> 7 也是一个候选， 7 = 7 。
> 仅有这两种组合。


示例 2：

> 输入: candidates = [2,3,5], target = 8
> 输出: [[2,2,2,2],[2,3,3],[3,5]]

示例 3：

> 输入: candidates = [2], target = 1
> 输出: []


提示：

* 1 <= candidates.length <= 30
* 1 <= candidates[i] <= 200
* candidate 中的每个元素都 互不相同
* 1 <= target <= 500

```c
int ansSize;

int combineSize;

int* ansColumnSize;

void dfs(int* candidates, int candidatesSize, int target, int** ans, int* combine, int idx) {
    if (idx == candidatesSize || target < 0) {
        return;
    }
    if (target == 0) {
        int* tmp = malloc(sizeof(int) * combineSize);
        for (int i = 0; i < combineSize; ++i) {
            tmp[i] = combine[i];
        }
        ans[ansSize] = tmp;
        ansColumnSize[ansSize++] = combineSize;
        return;
    }
    
    dfs(candidates, candidatesSize, target, ans, combine, idx + 1);
 
    combine[combineSize++] = candidates[idx];
    dfs(candidates, candidatesSize, target - candidates[idx], ans, combine, idx);
    combineSize--;
   
}

int** combinationSum(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {

    ansSize = combineSize = 0;
    int** ans = malloc(sizeof(int*) * 1001);
    ansColumnSize = malloc(sizeof(int) * 1001);
    int combine[2001];
    dfs(candidates, candidatesSize, target, ans, combine, 0);
    *returnSize = ansSize;
    *returnColumnSizes = ansColumnSize;
    return ans;
}
```

#### [40. 组合总和 II](https://leetcode.cn/problems/combination-sum-ii/)

给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

 示例 1:

> 输入: candidates = [10,1,2,7,6,1,5], target = 8,
> 输出:
> [
> [1,1,6],
> [1,2,5],
> [1,7],
> [2,6]
> ]

示例 2:

> 输入: candidates = [2,5,2,1,2], target = 5,
> 输出:
> [
> [1,2,2],
> [5]
> ]


提示:

* 1 <= candidates.length <= 100
* 1 <= candidates[i] <= 50
* 1 <= target <= 30

```c
int ansSize;

int combineSize;

int* ansColumnSize;

void Dfs(int* candidates, int candidatesSize, int target, int** ans, int* combine, int idx) {

    if (target == 0) {

        int* tmp = malloc(sizeof(int) * combineSize);
        for (int i = 0; i < combineSize; ++i) {
            tmp[i] = combine[i];
        }
        ans[ansSize] = tmp;
        ansColumnSize[ansSize++] = combineSize;
        return;
    }
    
    for (int i = idx; i < candidatesSize && candidates[i] <= target; i++) {
        if (i > idx && candidates[i] == candidates[i - 1]) {
            continue;
        }

        combine[combineSize++] = candidates[i];
        Dfs(candidates, candidatesSize, target - candidates[i], ans, combine, i + 1);
        combineSize--;
    }
}

int Cmp(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}

int** combinationSum2(int* candidates, int candidatesSize, int target, int* returnSize, int** returnColumnSizes) {

    ansSize = combineSize = 0;
    int** ans = malloc(sizeof(int*) * 1001);
    ansColumnSize = malloc(sizeof(int) * 1001);
    int combine[2001];
    
    qsort(candidates, candidatesSize, sizeof(int), Cmp);

    Dfs(candidates, candidatesSize, target, ans, combine, 0);
    *returnSize = ansSize;
    *returnColumnSizes = ansColumnSize;
    return ans;
}
```

#### [41. 缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/)

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。


示例 1：

> 输入：nums = [1,2,0]
> 输出：3

示例 2：

> 输入：nums = [3,4,-1,1]
> 输出：2

示例 3：

> 输入：nums = [7,8,9,11,12]
> 输出：1
>


提示：

* 1 <= nums.length <= 5 * 105
* -231 <= nums[i] <= 231 - 1

```c
int firstMissingPositive(int* nums, int numsSize){
    
    int i;
    for (i = 0; i < numsSize; i++) {
        if (nums[i] == 1) {
            break;
        }
    }

    if (i == numsSize) {
        return 1;
    }

    for (i = 0; i < numsSize; i++) {
        if (nums[i] <= 0 || nums[i] > numsSize) {
            nums[i] = 1;
        }
    }

    for (i = 0; i < numsSize; i++) {
        int index = abs(nums[i]) - 1;
        nums[index] = -abs(nums[index]);
    }

    for (i = 0; i < numsSize; i++) {
        if (nums[i] > 0) {
            return i + 1;
        }
    }

    return numsSize + 1;
}
```

#### [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：

![](img/rainwatertrap.png)

> 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
> 输出：6
> 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

示例 2：

> 输入：height = [4,2,0,3,2,5]
> 输出：9


提示：

* n == height.length
* 1 <= n <= 2 * 104
* 0 <= height[i] <= 105

```c
void PreMax(int *nums, int size, int *preMax)
{
    preMax[0] = nums[0];
    for (int i = 1; i < size; i++) {
        preMax[i] = fmax(nums[i], preMax[i - 1]);
    }
}

void PostMax(int *nums, int size, int *postMax)
{
    postMax[size - 1] = nums[size - 1];
    for (int i = size - 2; i >= 0; i--) {
        postMax[i] = fmax(nums[i], postMax[i + 1]);
    }
}

int trap(int* height, int heightSize){
    int preMax[heightSize];
    int postMax[heightSize];

    PreMax(height, heightSize, preMax);
    PostMax(height, heightSize, postMax);

    int ans = 0;
    for (int i = 0; i < heightSize; i++) {
        ans += fmin(preMax[i], postMax[i]) - height[i];
    }

    return ans;
}
```

#### [43. 字符串相乘](https://leetcode.cn/problems/multiply-strings/)

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

 示例 1:

> 输入: num1 = "2", num2 = "3"
> 输出: "6"

示例 2:

> 输入: num1 = "123", num2 = "456"
> 输出: "56088"


提示：

* 1 <= num1.length, num2.length <= 200
* num1 和 num2 只能由数字组成。
* num1 和 num2 都不包含任何前导零，除了数字0本身。

```c
char * multiply(char * num1, char * num2)
{
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    if ((len1 == 1 && num1[0] == '0') || (len2 == 1 && num2[0] == '0')) {
        return "0";
    }
    int len = len1 + len2;
    int *arr = (int *)malloc(len * sizeof(int));
    memset(arr, 0, len * sizeof(int));

    for (int i = len1 - 1; i >= 0; i--) {
        int val1 = num1[i] - '0';
        for (int j = len2 - 1; j >= 0; j--) {
            int val2 = num2[j] - '0';
            int sum = arr[i + j + 1] + val1 * val2;
            arr[i + j + 1] = sum % 10;
            arr[i + j] += sum / 10;
        }
    }

    char *ans = (char *)malloc((len + 1) * sizeof(char));
    int size = 0;
    for (int i = 0; i < len; i++) {
        if (i == 0 && arr[i] == 0) {
            continue;
        }
        ans[size++] = arr[i] + '0';
    }
    ans[size] = '\0';

    return ans;
}
```

#### [44. 通配符匹配](https://leetcode.cn/problems/wildcard-matching/)

给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

> 输入:
> s = "aa"
> p = "a"
> 输出: false
> 解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:

> 输入:
> s = "aa"
> p = "*"
> 输出: true
> 解释: '*' 可以匹配任意字符串。

示例 3:

> 输入:
> s = "cb"
> p = "?a"
> 输出: false
> 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

示例 4:

> 输入:
> s = "adceb"
> p = "*a*b"
> 输出: true
> 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".

示例 5:

> 输入:
> s = "acdcb"
> p = "a*c?b"
> 输出: false

```c
bool isMatch(char * s, char * p){
    int m = strlen(s);
    int n = strlen(p);
    int dp[m + 1][n + 1];
    memset(dp, 0, sizeof(dp));
    dp[0][0] = true;
    for (int i = 1; i <= n; ++i) {
        if (p[i - 1] == '*') {
            dp[0][i] = true;
        } else {
            break;
        }
    }

    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (p[j - 1] != '*') {
                dp[i][j] = dp[i - 1][j - 1] && (p[j - 1] == '?' || s[i - 1] == p[j - 1]);
            } else {
                dp[i][j] = dp[i][j - 1] | dp[i - 1][j];
            }
        }
    }

    return dp[m][n];
}
```

#### [45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/)

给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

 示例 1:

> 输入: nums = [2,3,1,1,4]
> 输出: 2
> 解释: 跳到最后一个位置的最小跳跃数是 2。
>      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:

> 输入: nums = [2,3,0,1,4]
> 输出: 2


提示:

* 1 <= nums.length <= 104
* 0 <= nums[i] <= 1000

```c
int jump(int* nums, int numsSize){
    int arr[numsSize];
    for (int i = 0; i < numsSize; i++) {
        arr[i] = INT_MAX;
    }
    arr[0] = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j <= i + nums[i] && j < numsSize; j++) {
            arr[j] = fmin(arr[j], arr[i] + 1);
        }
    } 
    
    return arr[numsSize - 1];
}
```

```c
int jump(int* nums, int numsSize){
    int maxLoc = 0;
    int steps = 0;
    int end = 0;

    for (int i = 0; i < numsSize - 1; i++) {
        maxLoc = fmax(maxLoc, nums[i] + i);
        if (i == end) {
            end = maxLoc;
            steps++;
        }
    } 

    return steps;
}
```

#### [46. 全排列](https://leetcode.cn/problems/permutations/)

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 示例 1：

> 输入：nums = [1,2,3]
> 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：

> 输入：nums = [0,1]
> 输出：[[0,1],[1,0]]

示例 3：

> 输入：nums = [1]
> 输出：[[1]]


提示：

* 1 <= nums.length <= 6
* -10 <= nums[i] <= 10
* nums 中的所有整数 互不相同

```c
void Swap(int *nums, int i, int j)
{
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

void BackTrack(int *nums, int numsSize, int **res, int *sizeOfRes, int cur)
{
    if (cur == numsSize - 1) {
        int *tmp = (int *)malloc(numsSize * sizeof(int));
        if (tmp == NULL) {
            return;
        }
       
        for (int i = 0; i < numsSize; i++) {
            tmp[i] = nums[i];
        }

        res[*sizeOfRes] = tmp;
        (*sizeOfRes)++;
        return;
    }

    for (int i = cur; i < numsSize; i++) {
        Swap(nums, i, cur);
        BackTrack(nums, numsSize, res, sizeOfRes, cur + 1);
        Swap(nums, i, cur);
    }
}

int** permute(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int **res = (int **)malloc(pow(numsSize, numsSize) * sizeof(int *));
    if (res == NULL) {
        return NULL;
    }
    int sizeOfRes = 0;

    BackTrack(nums, numsSize, res, &sizeOfRes, 0);

    *returnColumnSizes = (int *)malloc(sizeOfRes * sizeof(int));
    if (*returnColumnSizes == NULL) {
        return NULL;
    }
    for (int i = 0; i < sizeOfRes; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }

    *returnSize = sizeOfRes;
    return res;

}
```

#### [47. 全排列 II](https://leetcode.cn/problems/permutations-ii/)

给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 示例 1：

> 输入：nums = [1,1,2]
> 输出：
> [[1,1,2],
>  [1,2,1],
>  [2,1,1]]

示例 2：

> 输入：nums = [1,2,3]
> 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


提示：

* 1 <= nums.length <= 8
* -10 <= nums[i] <= 10

```c
void Swap(int *nums, int i, int j)
{
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

void BackTrack(int *nums, int numsSize, int **res, int *sizeOfRes, int cur)
{
    if (cur == numsSize - 1) {
        int *tmp = (int *)malloc(numsSize * sizeof(int));
        if (tmp == NULL) {
            return;
        }
       
        for (int i = 0; i < numsSize; i++) {
            tmp[i] = nums[i];
        }

        res[*sizeOfRes] = tmp;
        (*sizeOfRes)++;
        return;
    }
 
    for (int i = cur; i < numsSize; i++) {
        bool flag = false;
        for (int j = cur; j < i; j++) {
            if (nums[j] == nums[i]) {
                flag = true;
                break;
            }
        }
        if (flag) {
            continue;
        }
        Swap(nums, i, cur);
        BackTrack(nums, numsSize, res, sizeOfRes, cur + 1);
        Swap(nums, i, cur);
    }
}

int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int **res = (int **)malloc(pow(numsSize, numsSize) * sizeof(int *));
    if (res == NULL) {
        return NULL;
    }
    int sizeOfRes = 0;

    BackTrack(nums, numsSize, res, &sizeOfRes, 0);

    *returnColumnSizes = (int *)malloc(sizeOfRes * sizeof(int));
    if (*returnColumnSizes == NULL) {
        return NULL;
    }
    for (int i = 0; i < sizeOfRes; i++) {
        (*returnColumnSizes)[i] = numsSize;
    }

    *returnSize = sizeOfRes;
    return res;

}
```

#### [48. 旋转图像](https://leetcode.cn/problems/rotate-image/)

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

 示例 1：

![](img/mat1.jpg)

> 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
> 输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：

![](img/mat2.jpg)

> 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
> 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


提示：

* n == matrix.length == matrix[i].length
* 1 <= n <= 20
* -1000 <= matrix[i][j] <= 1000

```c
void Swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    // 先转置，再左右翻转
    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < i; j++) {
            Swap(&matrix[i][j], &matrix[j][i]);
        }
    }

    for (int i = 0; i < matrixSize; i++) {
        for (int j = 0; j < matrixSize / 2; j++) {
            Swap(&matrix[i][j], &matrix[i][matrixSize - j - 1]);
        }
    }

    return matrix;
}
```

#### [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/)

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

 示例 1:

> 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
> 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:

> 输入: strs = [""]
> 输出: [[""]]

示例 3:

> 输入: strs = ["a"]
> 输出: [["a"]]


提示：

* 1 <= strs.length <= 104
* 0 <= strs[i].length <= 100
* strs[i] 仅包含小写字母

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        for (String str : strs) {
            char[] array = str.toCharArray();
            Arrays.sort(array);
            String key = new String(array);
            List<String> list = map.getOrDefault(key, new ArrayList<String>());
            list.add(str);
            map.put(key, list);
        }

        return new ArrayList<List<String>>(map.values());
    }
}
```

#### [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/)

实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn ）。

 示例 1：

> 输入：x = 2.00000, n = 10
> 输出：1024.00000

示例 2：

> 输入：x = 2.10000, n = 3
> 输出：9.26100

示例 3：

> 输入：x = 2.00000, n = -2
> 输出：0.25000
> 解释：2-2 = 1/22 = 1/4 = 0.25


提示：

* -100.0 < x < 100.0
* -231 <= n <= 231-1
* -104 <= xn <= 104

```c
double MyPowWithPositive(double x, long n)
{
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return x;
    }

    return pow(MyPowWithPositive(x, n / 2) , 2) * MyPowWithPositive(x, n % 2); 
}

double myPow(double x, int n){
    bool isNegtive = false;
    long N = n;
    if (N < 0) {
        isNegtive = true;
        N = -N;
    }

    double num = MyPowWithPositive(x, N);
    if (isNegtive) {
        return 1 / num;
    }
    return num;
}
```



#### [52. N皇后 II](https://leetcode.cn/problems/n-queens-ii/)

n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

 示例 1：

![](img/queens.jpg)

> 输入：n = 4
> 输出：2
> 解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：

> 输入：n = 1
> 输出：1


提示：

* 1 <= n <= 9

```c
bool IsValid(int **arr, int arrSize, int row, int col)
{
    for (int i = 0;  i < row; i++) {
        if (arr[i][col] == 1) {
            return false;
        }
    }

    for (int i = row - 1, j = col + 1; i >= 0 && j < arrSize; i--, j++) {
        if (arr[i][j] == 1) {
            return false;
        }
    }

    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
        if (arr[i][j] == 1) {
            return false;
        }
    }

    return true;
}

void BackTrack(int **arr, int arrSize, int cur, int *num)
{
    if (cur == arrSize) {
        (*num)++;
        return;
    }

    for (int i = 0; i < arrSize; i++) {
        
        if (!IsValid(arr, arrSize, cur, i)) {
           continue;
        }
        arr[cur][i] = 1;
        BackTrack(arr, arrSize, cur + 1, num);
        arr[cur][i] = 0;         
    }
}

int totalNQueens(int n)
{
    int **arr = (int **)malloc(n * sizeof(int *));
    if (arr == NULL) {
        return 0;
    }
    for (int i = 0; i < n; i++) {
        arr[i] = (int *)malloc(n * sizeof(int));
        if (arr[i] == NULL) {
            return 0;
        }
        memset(arr[i] , 0, n * sizeof(int));
    }

    int num = 0;
    BackTrack(arr, n, 0, &num);

    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }
    free(arr);
    
    return num;
}
```

#### [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/)

给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。

 示例 1：

> 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
> 输出：6
> 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：

> 输入：nums = [1]
> 输出：1

示例 3：

> 输入：nums = [5,4,-1,7,8]
> 输出：23


提示：

* 1 <= nums.length <= 105
* -104 <= nums[i] <= 104

```c
int maxSubArray(int* nums, int numsSize){
    int maxSum = nums[0];
    int arr[numsSize];

    arr[0] = nums[0];
    for (int i = 1; i < numsSize; i++) {
        arr[i] = fmax(arr[i - 1] + nums[i], nums[i]);
        if (maxSum < arr[i]) {
            maxSum = arr[i];
        }
    }
    return maxSum;
}
```

#### [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 示例 1：

![](img/spiral1.jpg)

> 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
> 输出：[1,2,3,6,9,8,7,4,5]

示例 2：

![](img/spiral.jpg)

> 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
> 输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：

* m == matrix.length
* n == matrix[i].length
* 1 <= m, n <= 10
* -100 <= matrix[i][j] <= 100

```c
int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    *returnSize = matrixSize * matrixColSize[0];
    int *res = (int *)malloc(*returnSize * sizeof(int));
    int size = 0;

    int l = 0; 
    int r = matrixColSize[0] - 1;
    int up = 0;
    int down = matrixSize - 1;

    while (size < *returnSize) {
       
        for (int i = l; i <= r && size < *returnSize; i++) {
            res[size++] = matrix[up][i];
        }
        up++;
        for (int i = up; i <= down && size < *returnSize; i++) {
            res[size++] = matrix[i][r];
        }
        r--;
        
        for (int i = r; i >= l && size < *returnSize; i--) {
            res[size++] = matrix[down][i];
        }
        down--;
        
        for (int i = down; i >= up && size < *returnSize; i--) {
            res[size++] = matrix[i][l];
        }
        l++;
       
    }

    return res;
}
```

#### [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/)

给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 示例 1：

> 输入：nums = [2,3,1,1,4]
> 输出：true
> 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：

> 输入：nums = [3,2,1,0,4]
> 输出：false
> 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。


提示：

* 1 <= nums.length <= 3 * 104
* 0 <= nums[i] <= 105

```c
bool canJump(int* nums, int numsSize)
{
    int maxLoc = 0;
    for (int i = 0; i < numsSize && maxLoc < numsSize; i++) {
        if (maxLoc < i) {
            return false;
        }
        maxLoc = fmax(i + nums[i], maxLoc);
    } 

    return maxLoc >= numsSize - 1 ? true : false;
}
```





#### [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。

 示例 1：

> 输入：prices = [7,1,5,3,6,4]
> 输出：7
> 解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
>      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
>      总利润为 4 + 3 = 7 。

示例 2：

> 输入：prices = [1,2,3,4,5]
> 输出：4
> 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
>      总利润为 4 。

示例 3：

> 输入：prices = [7,6,4,3,1]
> 输出：0
> 解释：在这种情况下, 交易无法获得正利润，所以不参与交易可以获得最大利润，最大利润为 0 。


提示：

* 1 <= prices.length <= 3 * 104
* 0 <= prices[i] <= 104

```c
int maxProfit(int* prices, int pricesSize){
    int profit = 0;
    for (int i = 1; i < pricesSize; i++) {
        if (prices[i] > prices[i - 1]) {
            profit += prices[i] - prices[i - 1];
        }
    }

    return profit;
}
```





#### [134. 加油站](https://leetcode.cn/problems/gas-station/)

在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 **唯一** 的。

示例 1:

> 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
> 输出: 3
> 解释:
> 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
> 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
> 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
> 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
> 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
> 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
> 因此，3 可为起始索引。

示例 2:

> 输入: gas = [2,3,4], cost = [3,4,3]
> 输出: -1
> 解释:
> 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
> 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
> 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
> 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
> 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
> 因此，无论怎样，你都不可能绕环路行驶一周。


提示:

* gas.length == n
* cost.length == n
* 1 <= n <= 105
* 0 <= gas[i], cost[i] <= 104

```c
int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize){
    int sumOfGas = 0;
    int sumOfCost = 0;

    for (int i = 0; i < gasSize; i++) {
        sumOfGas += gas[i];
        sumOfCost += cost[i];
    }

    if (sumOfGas < sumOfCost) {
        return -1;
    }

    // 如果sumOfGas大于等于sumOfCost，则必定有解，只需要遍历找解就行
    int res = 0;
    sumOfGas = 0;
    for (int i = 0; i < gasSize; i++) {
        sumOfGas = sumOfGas + gas[i] - cost[i];
        if (sumOfGas < 0) {
            sumOfGas = 0;
            res = i + 1;
        }
    }

    return res;
}
```
