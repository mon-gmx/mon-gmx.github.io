# Big Ass Cheat Sheet

## Algorithms

1️⃣ Backtracking (Subset Generation)

Best For: Exploring all possible solutions while pruning invalid paths.

Example: Generating subsets

```
def backtrack_subsets(nums):
    def backtrack(start, path):
        result.append(path[:])  # Store subset
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)  # Recurse
            path.pop()  # Undo choice

    result = []
    backtrack(0, [])
    return result
```

✅ Use when:

Generating permutations, subsets, or combinations.

Solving constraint satisfaction problems (e.g., N-Queens, Sudoku).

2️⃣ N-Queens Problem (Backtracking)

Best For: Placing N queens on an NxN chessboard so that no two queens attack each other.

```
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True
    
    def backtrack(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Undo choice
    
    result = []
    board = [-1] * n
    backtrack(0)
    return result

print(solve_n_queens(4))
```

✅ Use when:

Solving constraint-based problems where valid placements must be checked.

Problems requiring exhaustive search with pruning (e.g., Sudoku, backtracking puzzles).

3️⃣ DFS (Depth-First Search)

Best For: Searching deep before broad in trees/graphs.

Recursive DFS (Cleaner but uses call stack)

```
def dfs_recursive(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs_recursive(graph, neighbor, visited)

# Example usage
graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
visited = set()
dfs_recursive(graph, 0, visited)
print(visited)
```

Iterative DFS (Uses explicit stack, avoids recursion depth issues)

```
def dfs_stack(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])  # Push neighbors onto the stack

    return visited
```

✅ Use when:

Exploring all paths in a tree or graph.

Checking connectivity (e.g., number of islands, connected components).

4️⃣ BFS (Breadth-First Search)

Best For: Finding the shortest path or processing in layers.

```
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

✅ Use when:

Finding the shortest path (e.g., word ladder, shortest path in a maze).

Level-order traversal in trees.

5️⃣ Bit Manipulation (Subsets Generation)

Best For: Efficient subset generation using bitwise operations.

```
def bitmask_subsets(nums):
    n = len(nums)
    result = []
    for i in range(1 << n):  # Loop from 0 to 2^n - 1
        subset = [nums[j] for j in range(n) if (i & (1 << j))]
        result.append(subset)
    return result
```

✅ Use when:

Dealing with subset problems efficiently.

Problems involving toggling elements (e.g., bitmask DP).

🔑 Rule of Thumb Summary

Backtracking: When exploring all possibilities with pruning (e.g., subsets, N-Queens).

DFS: When searching deep or solving recursive problems (e.g., connected components, islands).

BFS: When finding shortest paths or processing in layers (e.g., shortest path problems).

Bit Manipulation: When subset problems involve toggling elements efficiently.

---

🔹 Common Two-Pointer Patterns & Problems
1️⃣ Opposite Direction (Left & Right Pointers)

When to use?
If the problem asks for two elements that meet a sum condition or comparison.
If it involves finding a pair in a sorted array.

Example:

✅ Two Sum (sorted array variant) → Find if two numbers sum to a target.

```
def twoSumSorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1  # Move left pointer to increase sum
        else:
            right -= 1  # Move right pointer to decrease sum
    return []
```
Time Complexity: O(n) (single pass, no extra space).

2️⃣ Same Direction (Fast & Slow Pointers)

When to use?
If the problem involves removing elements in-place (modifying an array without extra space).
If there's a need to find cycles (e.g., in linked lists).

Example:

✅ Remove Duplicates from Sorted Array

```
def removeDuplicates(nums):
if not nums:
    return 0
slow = 0  # This will point to the last unique element
for fast in range(1, len(nums)):
    if nums[fast] != nums[slow]:  
        slow += 1
        nums[slow] = nums[fast]  
return slow + 1  # Return new length
```

Time Complexity: O(n), Space Complexity: O(1).

✅ Detect Cycle in Linked List (Floyd’s Cycle Algorithm)

```
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
Time Complexity: O(n), Space Complexity: O(1).


3️⃣ Sliding Window (Expanding & Contracting)

When to use?
    If the problem asks for the longest, shortest, or optimal subarray that meets a condition.
    If there's a need to minimize or maximize a window.

Example:

✅ Smallest Subarray with Sum ≥ Target
```
def minSubArrayLen(target, nums):
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return min_len if min_len != float('inf') else 0
```
Time Complexity: O(n), Space Complexity: O(1).

4️⃣ Merging Two Sorted Arrays or Lists

When to use?
    If you need to merge two sorted lists efficiently.

Example:

✅ Merge Two Sorted Arrays In-Place

```
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
```

Time Complexity: O(n + m), Space Complexity: O(1).

🔥 When Not to Use Two Pointers

🚫 When the input is not sorted and sorting doesn’t help

🚫 When you need all possible pairs (brute force may be needed)

🚫 When you require backtracking or more complex recursion

🎯 Summary Cheat Sheet

|Pattern|Use Case|Example|
|-----------|-----------|-------|
|**Left & Right Pointers**|Find a pair that meets a condition|Two Sum (Sorted)|
|**Fast & Slow Pointers**|Find cycles, modify arrays in place|Detect Cycle, Remove Duplicates|
|**Sliding Window**|Find min/max subarray that meets a condition|Smallest Subarray Sum|
|**Merge Pointers**|Merge two sorted lists efficiently	|Merge Sorted Arrays|


Kadane’s Algorithm (Maximum Subarray Sum)

Steps:

    Initialize:
        max_sum = -inf (or float('-inf') in Python)
        current_sum = 0
    Iterate through the array:
        Add the current element to current_sum.
        If current_sum is greater than max_sum, update max_sum.
        If current_sum becomes negative, reset it to 0.
    Return max_sum.

```
def kadane(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
```

---

## Data structures cheat-sheet

|Name   |Description                  |Use Cases           |Pros                    |Cons                     |Python Implementation|Golang Implementation|ASCII Diagram|Popular Project|
|------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|---------------------|----------------------|----------------------|----------------------|
|**Array**|Fixed-size or dynamic collection of elements stored in contiguous memory.|Storing ordered data, lookups, and iteration.|Fast lookups (O(1) for index-based access), simple implementation.|Slow insertions and deletions (O(n) in worst case).|`arr = [1, 2, 3]`|`arr := []int{1, 2, 3}`|`[1, 2, 3]`|NumPy
|**Linked List**|Sequential collection of nodes, where each node points to the next.|Dynamic memory allocation, stacks, and queues.|Efficient insertions and deletions (O(1) at head/tail).|Slower lookups (O(n)).|`class Node: ...`|`type Node struct {...}`|`1 -> 2 -> 3`|Linux Kernel Scheduler 
|**Doubly Linked List**|Each node has pointers to both previous and next nodes.|Efficient bidirectional traversal.|Easier deletion and insertion compared to singly linked lists.|Uses extra memory for pointers.|`class Node: ...`|`type Node struct {...}`|`1 <-> 2 <-> 3`|Web Browsers (Back/Forward) 
|**Stack**|LIFO (Last-In, First-Out) structure.|Backtracking, function calls, undo functionality.|Fast operations (O(1) push/pop).|Limited access (only top element available).|`stack = []`|`var stack []int`|`Top -> 3 -> 2 -> 1`|Function Call Stack 
|**Queue**|FIFO (First-In, First-Out) structure.|Task scheduling, BFS, buffering.|Fast enqueue/dequeue (O(1)).|Slow searching (O(n)).|`from collections import deque`|`var queue []int`|`1 -> 2 -> 3`|Print Spooler 
|**Priority Queue (Heap)**|A queue where elements are dequeued based on priority.|Scheduling, shortest path algorithms.|Efficient min/max retrieval (O(1)), insert/delete (O(log n)).|Requires balancing operations.|`import heapq`|`import "container/heap"`|`  1  \n / \ \n3   5`|Dijkstra’s Algorithm 
|**Skip List**|A linked list with hierarchical layers for fast searching.|Alternative to balanced trees.|O(log n) search, insert, delete.|Extra memory for multiple layers.|`class SkipList:`|`type SkipList struct {...}`|`1 -> 2 -> 3`|Redis 
|**Fenwick Tree (BIT)**|Binary Indexed Tree for prefix sum queries.|Range sum queries in O(log n).|Space-efficient, fast updates.|Only works on cumulative data.|`class FenwickTree:`|`type FenwickTree struct {...}`|`[1,2,3]`|Competitive Programming 
|**Segment Tree**|Tree structure for range queries and updates.|RMQ, range sums.|Fast range queries (O(log n)).|High memory usage.|`class SegmentTree:`|`type SegmentTree struct {...}`|`  5  \n / \ \n3   8`|Range Query Processing 
|**Suffix Tree**|Compact trie of suffixes for string search.|Fast pattern matching.|O(m) search time.|High memory usage.|`class SuffixTree:`|`type SuffixTree struct {...}`|`root -> ab`|Bioinformatics (Genome Search) 
|**Suffix Array**|Array of sorted suffixes.|String searching, text indexing.|More memory efficient than suffix trees.|Slower to construct.|`class SuffixArray:`|`type SuffixArray struct {...}`|`[0, 3, 5]`|Google Search Indexing 
|**Disjoint Set (Union-Find)**|Tracks elements partitioned into sets.|Kruskal's MST, connectivity checks.|Fast union/find (O(α(n))).|Extra memory for parent pointers.|`class DisjointSet:`|`type DisjointSet struct {...}`|`{A: A, B: A}`|Kruskal’s MST 
|**Van Emde Boas Tree**|Tree with fast integer key operations.|Fast membership testing.|O(log log n) operations.|Large memory overhead.|`class VEBTree:`|`type VEBTree struct {...}`|`root -> child`|Specialized Indexing 
|**Ternary Search Tree**|Trie optimized for dictionary storage.|Autocomplete, spell checkers.|More space-efficient than tries.|Slower than hash tables.|`class TST:`|`type TST struct {...}`|`root -> a?b`|Spell Checkers 
|**K-D Tree**|Spatial partitioning tree for multi-dimensional data.|Nearest neighbor search.|Efficient for k-dimensional queries.|Can become unbalanced.|`class KDTree:`|`type KDTree struct {...}`|`root -> (x,y)`|Computer Vision (Nearest Neighbor) 
|**Count-Min Sketch**|Probabilistic frequency estimation.|Data stream analysis.|Space-efficient.|Possible overestimation.|`class CMSketch:`|`type CMSketch struct {...}`|`[010110]`|Network Traffic Analysis 
|**Bloom Filter**|Probabilistic data structure for set membership testing.|Caching, avoiding unnecessary database queries.|Space-efficient.|False positives possible.|`import pybloom`|`github.com/willf/bloom`|`[010110]`|Google Bigtable 
|**Inverted Index**|Mapping from content to its location in documents.|Search engines, full-text search.|Fast text searches.|Requires preprocessing.|`class InvertedIndex: ...`|`type InvertedIndex struct {...}`|`{word -> [docs]}`|Elasticsearch 
|**Rainbow Table**|Precomputed hashes for fast password cracking.|Cryptanalysis, security auditing.|Speeds up hash cracking.|Requires significant storage.|`class RainbowTable:`|`type RainbowTable struct {...}`|`{hash -> password}`|Security Auditing 

---

## Caching and eviction strategies

|Name	|Type	|Description	|When to Use	|When Not to Use	|Where It Is Used	|Python Implementation|
|-------|-------|---------------|---------------|-------------------|-------------------|--------------|
|**Write-Through**|Caching Strategy|Writes data to both the cache and the backing store simultaneously.|When data consistency between cache and storage is crucial.|When high write latency is unacceptable.|Database caching, disk write caching.|Use a dictionary wrapper that updates both cache and DB.|
|**Write-Back**|Caching Strategy|Writes to the cache first and updates the backing store later.|When reducing write latency is important.|When data loss due to cache failure is unacceptable.|CPU caches, storage controllers.|Use a background write thread with a queue.|
|**Write-Around**|Caching Strategy|Writes directly to storage, bypassing the cache.|When write-heavy workloads exist, and cache pollution is a concern.|When read performance should be improved by keeping writes in cache.|Database storage caching.|Directly write to the DB while maintaining a read cache.|
|**Lazy Write**|Caching Strategy|Writes to cache first and writes to storage only when evicted.|When minimizing writes is necessary and occasional data loss is tolerable.|When strong consistency is needed.|Web applications, database buffers.|Combine an LRU cache with background flushing.|
|**Least Recently Used (LRU)**|Cache Eviction Policy|Removes the least recently accessed item first.|When recent data is more likely to be reused.|When all items have an equal chance of being accessed.|CPU caches, web browsers, Redis.|collections.OrderedDict or functools.lru_cache.|
|**Least Frequently Used (LFU)**|Cache Eviction Policy|Removes the least frequently accessed item first.|When frequently accessed items are more important.|When access patterns are unpredictable.|Database caches, web servers.|Use a counter-based approach with a heap.|
|**First-In-First-Out (FIFO)**|Cache Eviction Policy|Removes the oldest item first.|When freshness isn’t critical, but managing a fixed size is.|When newer items are more relevant.|Print spoolers, queue-based systems.|collections.deque or a simple list.|
|**Time-To-Live (TTL) Cache**|Cache Eviction Policy|Removes items after a set expiration time.|When data has a fixed validity period.|When access frequency matters more than age.|Web caches, API rate limiting.|Use cachetools.TTLCache.|
|**Random Replacement (RR)**|Cache Eviction Policy|Removes a random item when space is needed.|When all data has an equal chance of being used.|When some items are significantly more important.|Hardware caches, probabilistic caching.|random.choice() on a list or dictionary.|
|**Most Recently Used (MRU)**|Cache Eviction Policy|Removes the most recently accessed item first.|When older data is more useful.|When recent access usually means higher relevance.|Specialized database caching.|Use a stack-based approach.|
|**Segmented LRU (SLRU)**|Cache Eviction Policy|Combines LRU with multiple segments for better optimization.|When balancing short-term and long-term locality.|When memory constraints make multi-segmentation expensive.|High-performance storage systems.|Implement with two LRU caches.|

---

## Load Balancer Strategies

|Name|Description|When to Use|When Not to Use|Where It Is Used|Python Implementation|
|----|-----------|-----------|---------------|---------------|---------------------|
|**Round Robin**|Distributes requests evenly across all servers in sequence.|When all servers have equal capacity and performance.|When servers have varying workloads or performance levels.|DNS load balancing, simple web server clusters.|servers = ["A", "B", "C"]; i = 0; def get_server(): global i; server = servers[i % len(servers)]; i += 1; return server|
|**Weighted Round Robi**n|Assigns different weights to servers based on capacity.|When servers have different processing power or bandwidth.|When traffic patterns are highly dynamic.|Cloud load balancers, CDNs.|weights = [3, 2, 1]; servers = ["A", "B", "C"]; from itertools import cycle; weighted_servers = sum([[s] * w for s, w in zip(servers, weights)], []); server_cycle = cycle(weighted_servers); def get_server(): return next(server_cycle)|
|**Least Connections**|Routes requests to the server with the fewest active connections.|When some requests require long processing times.|When all requests are short-lived and equal in complexity.|API gateways, microservices.|import random; connections = {"A": 2, "B": 5, "C": 1}; def get_server(): return min(connections, key=connections.get)|
|**IP Hashing**|Assigns a client to a specific server based on their IP address.|When session persistence is needed.|When IP-based load balancing is unnecessary or unfair.|Gaming servers, user authentication services.|import hashlib; servers = ["A", "B", "C"]; def get_server(ip): return servers[int(hashlib.md5(ip.encode()).hexdigest(), 16) % len(servers)]|
|**Consistent Hashing**|Distributes requests based on a hash ring, reducing remapping when servers change.|When minimizing cache misses is critical.|When a simple round-robin approach suffices.|Distributed caching (Memcached, Redis), CDN routing.|from hashlib import md5; servers = ["A", "B", "C"]; def get_server(key): return servers[int(md5(key.encode()).hexdigest(), 16) % len(servers)]|
|**Least Response Time**|Routes requests to the server with the fastest response time.|When response time varies significantly.|When all servers perform equally.|Web applications, API gateways.|response_times = {"A": 100, "B": 200, "C": 50}; def get_server(): return min(response_times, key=response_times.get)|
|**Random**|Selects a random server for each request.|When simplicity is needed and servers are equally powerful.|When fairness and efficiency matter.|Simple load balancers, stateless applications.|import random; servers = ["A", "B", "C"]; def get_server(): return random.choice(servers)|

---

## Database Replication Strategies

|Strategy|Pros|Cons|When to Use|Example Implementations|
|--------|----|----|-----------|-----------------------|
|**Master-Slave Replication**|Read scalability, backups offloaded to slaves|Writes go only to master, risk of lag|High read workloads, backup redundancy|MySQL, PostgreSQL (Streaming Replication)|
|**Master-Master Replication**|Load balancing for writes, HA|Conflict resolution needed, complex setup|Write-heavy workloads needing HA|MySQL Group Replication, PostgreSQL BDR|
|**Logical Replication**|Flexible table-level replication|Slower than streaming replication, lag|Selective data replication|PostgreSQL Logical Replication|
|**Physical (Streaming) Replication**|Fast, real-time replication|Whole database replicated, no filtering|HA, disaster recovery|PostgreSQL Streaming Replication|
|**Asynchronous Replication**|No performance penalty on master|Risk of data loss on failover|High-latency networks, eventual consistency|MySQL async replication, PostgreSQL async replication|
|**Synchronous Replication**|Strong consistency, no data loss|Increased latency, impacts performance|Critical systems needing consistency|PostgreSQL synchronous replication, MySQL semi-sync|
|**Shared-Nothing Architecture (Sharding)**|Extreme scalability, independent nodes|Complex, requires partitioning logic|Massive distributed databases|MongoDB, Google Spanner|

---

## Write speeds in media

|Storage Type|Write Speed (Approx.)|Pros|Cons|Best Use Cases|Avg. Cost per GB|
|------------|---------------------|----|----|--------------|----------------|
|**L1 Cache (CPU Register Level)**|500–1000 GB/s|Ultra-low latency (~1ns), fastest memory|Extremely small (KBs), CPU-dependent|CPU instruction execution, immediate calculations|Embedded in CPU|
|**L2 Cache**|200–500 GB/s|Fast access, larger than L1|Still small, higher latency than L1|High-speed buffering between CPU and RAM|Embedded in CPU|
|**L3 Cache**|50–200 GB/s|Shared among cores, good for inter-core communication|Slower than L1/L2, limited size|Multi-core processing, reducing RAM fetches|Embedded in CPU|
|**NVMe (PCIe SSD)**|2000–7000 MB/s|Extremely fast, low latency, high IOPS|Expensive, requires PCIe lanes, limited capacity|High-performance databases, real-time analytics, gaming|$0.10–$0.25|
|**SATA SSD**|200–600 MB/s|Fast, reliable, lower power consumption|More expensive than HDD, limited write cycles|OS storage, general workloads, cloud VM disks|$0.08–$0.15|
|**HDD (7200 RPM)**|100–200 MB/s|Cheap, large capacity|Slow, high latency, mechanical failure risk|Large backups, archival storage, media storage|$0.02–$0.05|
|**HDD (5400 RPM)**|50–120 MB/s|Power-efficient, quiet|Even slower than 7200 RPM HDDs|Cold storage, long-term backups, low-access data|$0.02–$0.04|
|**Network Storage (NAS/SAN over 10GbE)**|1–3 GB/s (depends on protocol & infra)|Scalable, accessible by multiple systems|Network bottlenecks, requires tuning for low latency|Centralized storage, high-availability clusters|$0.05–$0.20 (depends on infra)|
|**Memory (RAM - DDR4/DDR5)**|50–80 GB/s (DDR4), 100–200 GB/s (DDR5)|Extremely fast, near-zero latency|Volatile, expensive, limited capacity|Active workloads, caching, in-memory databases|$5–$10|
|**Persistent Memory (Optane, NVDIMM)**|2–10 GB/s|Non-volatile, faster than SSDs|Expensive, niche use cases|Low-latency caching, hybrid memory systems|$10–$30|
