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

    for (int r = 1; r < len; r++) {
        for (int l = 0; l < r; l++) {
            dp[l][r] = (s[l] == s[r]) && (r - l <= 2 || dp[l + 1][r - 1]);

            if (dp[l][r] && r - l + 1 > maxLen) {
                maxLen = r - l + 1;
                begin = l;
                end = r;
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
bool isMatch(char* s, char* p){
    int lenOfS = strlen(s);
    int lenOfP = strlen(p);

    bool dp[lenOfS +1 ][lenOfP +1];

    memset(dp,false,(lenOfS +1)* (lenOfP + 1)*sizeof(bool));
    
    dp[0][0] = true;
    for( int i = 0 ; i <= lenOfS; i++ ) {
        for(int j = 0 ; j <= lenOfP; j++ ) {
           if (j == 0) {
                dp[i][j] = (i == 0 ? true : false);
            }
            else {
                if (p[j - 1] != '*') {
                    if (i > 0 && (s[i - 1] == p[j - 1] || p[j - 1] == '.')) {
                        dp[i][j] = dp[i - 1][j - 1];
                    }
                }
                else { // 当p[j] == '*'时，由于'*'跟在一个字符后面，所以j必然大于等于2；
                    dp[i][j] = dp[i][j - 2];
                    if (i > 0 && (s[i - 1] == p[j - 2] || p[j - 2] == '.')) {
                        dp[i][j] |= dp[i - 1][j];
                    }
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

