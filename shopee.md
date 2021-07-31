Shopee的办公室（二）

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

