# Set Mismatch
Leetcode練習題：645. Set Mismatch

這是我練習的[完整程式碼](https://github.com/HTY62006/MyLearningNote/blob/master/Leetcode/week4/645.%20Set%20Mismatch.py)

## [回首頁](https://github.com/HTY62006/MyLearningNote)
## 需求
nums應為一個內容為1~n的list：nums = [1, 2, 3, 4,..., n]。
1. 回傳nums的重複項
2. 回傳nums的缺失值
* Example:
```Text
Input: nums = [1,2,2,4]
Output: [2,3]
```
## 實作與想法
假設nums = [1,2,2,4]
1. 由於正確的內容一定是[1,2,3,...,n]，所以先以`set()`來將輸入的nums去除重複值後輸出成non_dup。
   > 此時non_dup = {1,2,4}
   ```Python
   non_dup = set(nums)
   ```
2. 將nums與non_dup各自加總，相減後可得到重複的值(dup)。
   > 此時dup = 2
   ```Python
   dup = sum(nums) - sum(non_dup)
   ```
3. 創建一擁有正確內容的list。
   > 此時correct = [1,2,3,4]
   ```Python
   correct = []
   for i in range(1, len(nums)+1):
       correct.append(i)
   ```
4. 以`set()`將coorect與nums去除重複值後相減。
   > 因此時資料型態為<class 'set'>，再加上結果只會有一數字，故以將相減的結果加總的方式將值轉為int。
   >> 此時miss = 3
   ```Python
   miss = sum(set(correct) - set(nums))
   ```
5. 最後可回傳結果為[2,3]
## [回首頁](https://github.com/HTY62006/MyLearningNote)
