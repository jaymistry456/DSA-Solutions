class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        # TC: O(n^2), SC: O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

        # better approach
        # Sort the array and then use 2-pointer
        # TC: O(nlogn), SC: O(n)
        temp_arr = []   # Stores (num, index)
        for i in range(len(nums)):
            temp_arr.append((nums[i], i))
        temp_arr.sort(key=lambda x:x[0])
        
        l, r = 0, len(temp_arr) - 1
        while l != r:
            curr_sum = temp_arr[l][0] + temp_arr[r][0]
            if curr_sum == target:
                return [temp_arr[l][1], temp_arr[r][1]]
            elif curr_sum < target:
                l += 1
            else:
                r -= 1

        # optimal approach
        # hashmap key -> number, value: index of number
        # TC: O(n), SC: O(n)
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap[target - nums[i]]]
            hashmap[nums[i]] = i