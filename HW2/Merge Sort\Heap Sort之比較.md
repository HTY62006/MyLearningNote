# Merge Sort/Heap Sort之比較

排序       | 時間複雜度
-----------|----------
Merge Sort | NlogN
Heap Sort  | NlogN

就時間複雜度而言，merge sort和heap sort是一致的，不過merge sort會占用更多的記憶體，因為在實現時我以一個額外空間來將正確排序的值取代原先額外空間內的值。

另外，我參考這篇文章 [Analysis of Algorithms](http://www-cs-students.stanford.edu/~rashmi/projects/Sorting.pdf) 中對於各種排序方式的比較，可以得知merge sort和heap sort的特性與優缺點：
1. heap sort是最慢的一種排序方式，但它不需要大量的遞迴或是多個Array就可以實現。
2. 應用在較大的Array時，merge sort的速度會比heap sort來得快一些，但因為要用額外空間所以它會需要heap sort所需記憶體的兩倍。

