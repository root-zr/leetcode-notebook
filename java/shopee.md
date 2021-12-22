### Shopee的办公室（二）

shopee的办公室非常大，小虾同学的位置坐落在右上角，而大门却在左下角，可以把所有位置抽象为一个网格（门口的坐标为0，0），小虾同学很聪明，每次只向上，或者向右走，因为这样最容易接近目的地，但是小虾同学不想让自己的boss们看到自己经常在他们面前出没，或者迟到被发现。他决定研究一下如果他不通过boss们的位置，他可以有多少种走法？

##### **输入描述:**

```
第一行 x,y,n (0<x<=30, 0<y<=30, 0<=n<= 20) 表示x,y小虾的座位坐标,n 表示boss的数量（ n <= 20）

接下来有n行, 表示boss们的坐标(0<xi<= x, 0<yi<=y，不会和小虾位置重合)

x1, y1

x2, y2

……

xn, yn
```

##### **输出描述:**

```
输出小虾有多少种走法
```

**示例1**

```
输入
3 3 2
1 1
2 2
输出
4
```

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        //用动态规划，状态转移方程dp[i][j] = dp[i-1][j] + dp[i][j-1];
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int bossNum = sc.nextInt();
      
        long[][] dp = new long[m+1][n+1]; //测试用例中有超过int范围的用例
        
        dp[0][0] = 1; //赋初值,门口的坐标
        
        for(int i = 1 ; i<= m ; i++) 
            dp[i][0] = dp[i-1][0]; //边界位置只能走一边
        for(int i = 1 ; i<= n ; i++)
            dp[0][i] = dp[0][i-1];
        
        for(int i=0;i<bossNum;i++) {
            dp[sc.nextInt()][sc.nextInt()]=-1;  //boss位置设置为-1
        }
        
        
        for(int i = 1 ; i <= m ; i ++ ){
            for(int j = 1; j <= n ; j++){
                if(dp[i][j] == -1) //老板位置不能走
                    dp[i][j] = 0;
                else
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
 
        System.out.println(dp[m][n]);
    }
} 
```

### Shopee的零食柜

shopee的零食柜，有着各式各样的零食，但是因为贪吃，小虾同学体重日益增加，终于被人叫为小胖了，他终于下定决心减肥了，他决定每天晚上去操场跑两圈，但是跑步太累人了，他想转移注意力，忘记痛苦，正在听着音乐的他，突然有个想法，他想跟着音乐的节奏来跑步，音乐有7种音符，对应的是1到7，那么他对应的步长就可以是1-7分米，这样的话他就可以转移注意力了，但是他想保持自己跑步的速度，在规定时间m分钟跑完。为了避免被累死，他需要规划他每分钟需要跑过的音符，这些音符的步长总和要尽量小。下面是小虾同学听的歌曲的音符，以及规定的时间，你能告诉他每分钟他应该跑多少步长？

##### **输入描述:**

```
输入的第一行输入 n（1 ≤ n ≤ 1000000，表示音符数），m（1<=m< 1000000, m <= n）组成，

第二行有 n 个数，表示每个音符（1<= f <= 7）
```

##### **输出描述:**

```
输出每分钟应该跑的步长
```

**示例1**

```
输入: 8 
      5 6 5 6 7 6 6 3 1
输出: 11
```

题目等同于https://leetcode-cn.com/problems/split-array-largest-sum/

解法一：动态规划

```java
import java.util.Arrays;

public class Solution {

    public int splitArray(int[] nums, int m) {
        int len = nums.length;
        // 前缀和，preSum[i] = sum[0..i)
        int[] preSum = new int[len + 1];
        preSum[0] = 0;
        for (int i = 0; i < len; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }

        // 区间 [i..j] 的和 preSum(j + 1) - preSum(i)
        int[][] dp = new int[len][m + 1];
        // 初始化：由于要找最小值，初值赋值成为一个不可能达到的很大的值
        for (int i = 0; i < len; i++) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);
        }
        // 分割数为 1 ，即不分割的情况，所有的前缀和就是依次的状态值
        for (int i = 0; i < len; i++) {
            dp[i][1] = preSum[i + 1];
        }

        // 从分割数为 2 开始递推
        for (int k = 2; k <= m; k++) {
            // 还未计算出的 i 是从 j 的最小值的下一位开始，因此是 k - 1
            for (int i = k - 1; i < len; i++) {
                // j 表示第 k - 1 个区间的最后一个元素额下标，最小值为 k - 2，最大值为 len - 2（最后一个区间至少有 1 个元素）
                for (int j = k - 2; j < i; j++) {
                    dp[i][k] = Math.min(dp[i][k], Math.max(dp[j][k - 1], preSum[i + 1] - preSum[j + 1]));
                }
            }
        }
        return dp[len - 1][m];
    }

```

复杂度分析：

时间复杂度：O(N^2M)
空间复杂度：O(N^2)

解法二： 二分查找

```java
public class Solution {

    public int splitArray(int[] nums, int m) {
        int max = 0;
        int sum = 0;

        // 计算「子数组各自的和的最大值」的上下界
        for (int num : nums) {
            max = Math.max(max, num);
            sum += num;
        }

        // 使用「二分查找」确定一个恰当的「子数组各自的和的最大值」，
        // 使得它对应的「子数组的分割数」恰好等于 m
        int left = max;
        int right = sum;
        while (left < right) {
            int mid = left + (right - left) / 2;

            int splits = split(nums, mid);
            if (splits > m) {
                // 如果分割数太多，说明「子数组各自的和的最大值」太小，此时需要将「子数组各自的和的最大值」调大
                // 下一轮搜索的区间是 [mid + 1, right]
                left = mid + 1;
            } else {
                // 下一轮搜索的区间是上一轮的反面区间 [left, mid]
                right = mid;
            }
        }
        return left;
    }

    /***
     *
     * @param nums 原始数组
     * @param maxIntervalSum 子数组各自的和的最大值
     * @return 满足不超过「子数组各自的和的最大值」的分割数
     */
    private int split(int[] nums, int maxIntervalSum) {
        // 至少是一个分割
        int splits = 1;
        // 当前区间的和
        int curIntervalSum = 0;
        for (int num : nums) {
            // 尝试加上当前遍历的这个数，如果加上去超过了「子数组各自的和的最大值」，就不加这个数，另起炉灶
            if (curIntervalSum + num > maxIntervalSum) {
                curIntervalSum = 0;
                splits++;
            }
            curIntervalSum += num;
        }
        return splits;
    }
}
```

实现字通配符*

在Linux Shell命令下通配符'*'表示0个或多个字符, 现编写一段代码实现通配符'*'的功能，注意只需要实现'*', 不用实现其他通配符。

##### **输入描述:**

```
第一行输入通配字符串
第二行输入要匹配查找的字符串
```

##### **输出描述:**

```
输出所有匹配的字串起始位置和长度，每行一个匹配输出
如果不匹配，则输出 -1 0
如果有多个按照起始位置和长度的正序输出。
```

**示例1**

```
输入
shopee*.com
shopeemobile.com
输出
0 16
说明
0 起始位置，16长度
```

**示例2**

```
输入
*.com
shopeemobile.com
输出
0 16
1 15
2 14
3 13
4 12
5 11
6 10
7 9
8 8
9 7
10 6
11 5
12 4
```

**示例3**

```
输入
o*m
shopeemobile.com
输出
2 5
2 14
7 9
14 2
```

```java
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer> res = new ArrayList<>(); //存放适配成功的地址
    static char[] regularExpression ;
    static char[] target;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();
        regularExpression = str1.toCharArray();
        target = str2.toCharArray();
        boolean flag = false;

        for(int i = 0 ; i < target.length ; i ++){

            if(target[i] == regularExpression[0] || regularExpression[0] == '*'){
                DFS(i,0);
                if(!res.isEmpty()) flag = true;
                for(int num:res){

                    if(regularExpression[regularExpression.length -1] == '*')
                        System.out.println(i + " " + (num- i +1));
                    else
                        System.out.println(i + " " + (num- i));
                }
                res.clear();
            }
        }

        if(flag == false)
            System.out.println(-1 + " " + 0);
    }

    private static void DFS(int i, int regularIndex) {
        if(regularIndex == regularExpression.length){
            res.add(i); //条件满足i就要+1
            return;
        }

        if(i == target.length) return; //匹配完了

        if(target[i] == regularExpression[regularIndex]){
            DFS(i+1,regularIndex+1);
        }else if(regularExpression[regularIndex] == '*'){//虽然字符不匹配，但是正则表达式是*
            DFS(i,regularIndex + 1); //*代表0个字符
            DFS(i+1,regularIndex);//*代表1个或多个字符
        }
    }


}
```

### 建物流中转站

Shopee物流会有很多个中转站。在选址的过程中，会选择离用户最近的地方建一个物流中转站。    

 假设给你一个二维平面网格，每个格子是房子则为1，或者是空地则为0。找到一个空地修建一个物流中转站，使得这个物流中转站到所有的房子的距离之和最小。 能修建，则返回最小的距离和。如果无法修建，则返回 -1。      

若范围限制在100*100以内的网格，如何计算出最小的距离和？        

当平面网格非常大的情况下，如何避免不必要的计算？           

**输入描述:**

```
4
0 1 1 0
1 1 0 1
0 0 1 0
0 0 0 0

先输入方阵阶数，然后逐行输入房子和空地的数据，以空格分隔。
```

##### **输出描述:**

```
8

能修建，则返回最小的距离和。如果无法修建，则返回 -1。
```

**示例1**

```
输入
4
0 1 1 0
1 1 0 1
0 0 1 0
0 0 0 0
输出
8
```

**示例2**

```
输入
4
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
输出
-1
```

```java
//直接暴力破解
import java.util.ArrayList;
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int[][] matrix = new int[n][n];
        ArrayList<int[][]> al = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = sc.nextInt();
                if(matrix[i][j]==1){
                    int[][] xy = new int[1][2];
                    xy[0][0]=i;
                    xy[0][1]=j;
                    al.add(xy);
                }
            }
        }
        
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int temp=0;
                if(matrix[i][j]==0){
                    for (int k = 0; k < al.size(); k++) {
                        temp+=Math.abs(al.get(k)[0][0]-i)+Math.abs(al.get(k)[0][1]-j);
                    }
                    res = res>temp?temp:res;
                }
            }
        }
        System.out.println(res==Integer.MAX_VALUE?-1:res);
        
    }
}
```

### Shopee的Orange Day

Shopee每个月都有属于大家的节日，每到这个时候，大家都会穿着橙色的T恤，吃着水果蛋糕，做着游戏。瞧，今天又是Orange Day了，吃货小虾同学早早的来到现场，看看有没有什么吃的，刚刚走进去就发现我们的前台mm愁眉苦脸的看着挂满礼物的发财树，细看发现，发财树的树枝因为承重不均，东倒西歪。是时候展现真正的技术啦，小虾同学，马上走上去，让前台mm把挂礼物的方案拿出来，前台mm拿出一大叠方案，小虾同学顿时傻眼了，但是他马上想到了一个方法，写一个程序判断每种方案的承重误差，把不合格的都干掉就行了。经过分析，把发财树抽象为一颗树。只要发财树的从顶部到各个叶子的各个路径上面的最大最小重量的差值在方案的误差范围内，就可以正常承重。

![](E:\大三下\leetcode\leetcode\img\313965_1560322338006_AB33537227D69FD077466CE827873748.png)

输入第一行表示数据样例数T，表示接下来会有T个相同格式的样例输入

每个样例输入如下

输入的第一行输入 n,（2 ≤ n ≤ 100000，节点的编号为0到n-1,0为根节点）组成，

第二行有 n 个数，表示每个节点挂的礼物的重量 w（1<= w<= 1000）
下面是n-1行，每行有两个整数，第一个数表示父节点的编号，第二个数表示子节点的编号

输出最大差值。

```java
public class ChristmasTree {
    static int sum = 0;
    static int max = Integer.MIN_VALUE;
    static class Node{
        int val;
        List<Node> children;
        Node(int val){
            this.val = val;
            children = new ArrayList<>();
        }
        public void addChild(Node node){
            children.add(node);
        }
    }
 
    public static void dfs(Node node){
        sum += node.val;
        if(node.children.size()==0){
            max = Math.max(max,sum);
        }else{
            for(int i=0;i<node.children.size();i++){
                dfs(node.children.get(i));
            }
        }
        sum-=node.val;
 
    }
 
    public static void main(String[] args) {
        System.out.println("请输入节点总数：");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        Node[] nodes = new Node[n];
        System.out.println("请输入每个结点的重量：");
        for(int i=0;i<n;i++){
            int val = scanner.nextInt();
            nodes[i] = new Node(val);
        }
 
        //构建树
        System.out.println("请输入父子节点编号：");
        for(int i=0;i<n-1;i++){
            int parentNum = scanner.nextInt();
            int childNum = scanner.nextInt();
            nodes[parentNum].addChild(nodes[childNum]);
        }
        dfs(nodes[0]);
        System.out.println("最大重量为："+max);
    }
}
```

