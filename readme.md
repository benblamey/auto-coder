# Auto-Coder

Auto-generate Bash programs for pre-processing given keywords:

# Examples:

Input:
```
auto_generate('uniq', 'count')
```

Output:
```
running...
uniq -c <input.txt
   1 1
   1 67
   1 3
   1 5
   1 8
   1 3
   1 79
   1 alice
   1 charlie
   1 bob
exit value: 0
```



Input:

```
auto_generate('sort', 'reverse')
```

Output:
```
running...
sort -r <input.txt
charlie
bob
alice
8
79
67
5
3
3
1
exit value: 0
```

Input:
```
auto_generate('sort', 'numeric')
```

Output:
```
running...
sort -g --dictionary-order --numeric-sort <input.txt
alice
bob
charlie
1
3
3
5
8
67
79
exit value: 0
```