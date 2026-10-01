# 🚀 GradStreet Exam Crusher: Strictly Optimal Handbook
**Tailored for Hasini | College 3-Round Placement Selection Exam**
**Criteria:** Maximum Performance — Strict $O(N)$ Time Complexity & $O(1)$ In-Place Space Complexity!

---

## 1. The Strict Grading Rubric (How Automated Graders Test You)

GradStreet test platforms (like Mettl, HackerRank, or proprietary portals) run **hidden test cases with $N = 100,000$ elements**:
* If you use sorting (`.sort()` on arrays) $\rightarrow$ **Time Limit Exceeded (TLE)** ($O(N \log N)$ vs $O(N)$).
* If you create new lists (`[x for x in nums]`) when in-place is asked $\rightarrow$ **Memory Limit Exceeded (MLE)** ($O(N)$ space vs $O(1)$).

Below are the **strictly optimal, 100% test-case-passing solutions** using **Two Pointers** and **Single-Pass $O(N)$ algorithms**.

---

## 2. The Top 10 Strictly Optimal Coding Patterns

---

### Pattern 1: Second Largest Element (Single-Pass $O(N)$ Time, $O(1)$ Space)
> **Problem:** Find the second largest number in `nums` without sorting. If no second largest exists, return `-1`.
> **Strict Rule:** Zero extra lists, single loop only!

```python
def second_largest(nums):
    first = float('-inf')
    second = float('-inf')
    
    for x in nums:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
            
    return second if second != float('-inf') else -1
```
* **Time Complexity:** $O(N)$ — Visits each element exactly once.
* **Space Complexity:** $O(1)$ — Only two variables used.

---

### Pattern 2: Move Zeroes to End In-Place ($O(N)$ Time, $O(1)$ Space)
> **Problem:** Given `nums = [0, 1, 0, 3, 12]`, move all `0`s to the end **in-place** without making a copy of the array.
> **Strict Rule:** Modify the original list directly using Two Pointers.

```python
def move_zeroes(nums):
    # insert_pos tracks where the next non-zero should land
    insert_pos = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            # Swap non-zero element with the element at insert_pos
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
            
    return nums
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$ (Strictly in-place!).

---

### Pattern 3: Remove Duplicates from Sorted Array ($O(N)$ Time, $O(1)$ Space)
> **Problem:** In a sorted array `nums`, remove duplicates **in-place** so each unique element appears once. Return the number of unique elements.

```python
def remove_duplicates(nums):
    if not nums:
        return 0
        
    # k is the boundary of unique elements
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
            
    return k  # nums[:k] contains the unique elements
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$

---

### Pattern 4: Valid Palindrome (Two Pointers, $O(N)$ Time, $O(1)$ Space)
> **Problem:** Check if a string is a palindrome, considering only alphanumeric characters and ignoring cases.
> **Strict Rule:** Do NOT create a reversed string copy. Use left/right pointers.

```python
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$

---

### Pattern 5: Leaders in an Array ($O(N)$ Time, $O(1)$ Auxiliary Space)
> **Problem:** An element is a "Leader" if it is strictly greater than all elements to its right. The rightmost element is always a leader.
> **Example:** `[16, 17, 4, 3, 5, 2]` $\rightarrow$ Leaders are `[17, 5, 2]`.
> **Strict Trick:** Scan from **RIGHT to LEFT**!

```python
def find_leaders(nums):
    n = len(nums)
    if n == 0:
        return []
        
    leaders = []
    max_from_right = nums[-1]
    leaders.append(max_from_right)
    
    # Traverse backwards from second-to-last element
    for i in range(n - 2, -1, -1):
        if nums[i] > max_from_right:
            leaders.append(nums[i])
            max_from_right = nums[i]
            
    # Reverse to keep original relative order
    leaders.reverse()
    return leaders
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$ auxiliary (ignoring output array).

---

### Pattern 6: Two Sum (Optimal One-Pass Hash Map)
> **Problem:** Find two indices such that `nums[i] + nums[j] == target`.

```python
def two_sum(nums, target):
    seen = {}  # { number : its_index }
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$

---

### Pattern 7: Rotate Array by K Positions (In-Place $O(N)$ Time, $O(1)$ Space)
> **Problem:** Rotate array `[1, 2, 3, 4, 5, 6, 7]` to the right by $k = 3$ positions $\rightarrow$ `[5, 6, 7, 1, 2, 3, 4]`.
> **Strict Trick:** The 3-Step Reverse Algorithm!

```python
def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle k > n
    
    # Helper to reverse elements in-place between start and end
    def reverse_slice(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    # 1. Reverse the entire array
    reverse_slice(0, n - 1)
    # 2. Reverse the first k elements
    reverse_slice(0, k - 1)
    # 3. Reverse the remaining n - k elements
    reverse_slice(k, n - 1)
    
    return nums
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$ (Zero extra memory!).

---

### Pattern 8: Maximum Subarray Sum (Kadane's Algorithm — $O(N)$ Time, $O(1)$ Space)
> **Problem:** Find the contiguous subarray with the largest sum in `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`.
> **Strict Trick:** If current sum drops below 0, reset it to 0!

```python
def max_sub_array(nums):
    max_sum = float('-inf')
    current_sum = 0
    
    for x in nums:
        current_sum += x
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
            
    return max_sum
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$

---

### Pattern 9: First Non-Repeating Character in a String ($O(N)$ Time)
> **Problem:** Find the index of the first character with frequency 1.

```python
def first_uniq_char(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
        
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
            
    return -1
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(1)$ (Because there are at most 26 lowercase English letters!).

---

### Pattern 10: Reverse Words in a String ($O(N)$ Time, Clean Tokenization)
> **Problem:** `"  the   sky  is   blue  "` $\rightarrow$ `"blue is sky the"`

```python
def reverse_words(s):
    # s.split() automatically handles multiple variable spaces!
    words = s.split()
    return " ".join(reversed(words))
```
* **Time Complexity:** $O(N)$
* **Space Complexity:** $O(N)$

---

## 3. Round 1 MCQ Traps: The 4 Big Traps

1. **Integer division `//` with negative numbers:**
   * In Python: `7 // 2 = 3`, BUT `-7 // 2 = -4`! (Floor division always rounds DOWN towards $-\infty$).
2. **Bitwise XOR properties:**
   * $x \oplus x = 0$
   * $x \oplus 0 = x$
   * To find the single non-repeated number in an array: XOR all numbers together!
3. **Loop Range Stop Condition:**
   * `range(2, 8, 3)` outputs `2, 5` (stops before 8!).
4. **String Immutability:**
   * Strings in Python **cannot be modified in-place**: `s[0] = 'a'` throws `TypeError`! You must create a new string or convert to a `list(s)`.
