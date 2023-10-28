class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 첫 번째 sort를 이용한 풀이
        # nums.sort()
        # return nums[-k]
        
        # 두번째 sort를 이용하지 않은 풀이
        # heap = nums[:k]
        # print(heap)
        # heapq.heapify(heap)
        
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        
        # return heap[0]
        
        # 내림차순
        return heapq.nlargest(k, nums)[-1]