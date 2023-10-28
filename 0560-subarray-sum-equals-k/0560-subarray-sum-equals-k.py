class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0  # 결과를 저장할 변수
        prefix_sum = 0  # 현재까지의 누적 합을 저장하는 변수
        d = {0: 1}  # 누적 합의 빈도수를 저장하는 딕셔너리 (0을 1로 초기화)

        for num in nums:  # 주어진 배열을 순회
            prefix_sum += num  # 현재 숫자를 누적 합에 추가

            # 만약 (누적 합 - k)가 딕셔너리에 존재한다면, 그 값은 현재까지의 부분 배열 합이 k와 같아질 수 있는 경우입니다.
            if prefix_sum - k in d:
                result += d[prefix_sum - k]
                


            # 현재 누적 합을 딕셔너리에 저장하거나, 이미 존재한다면 빈도수를 증가시킵니다.
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] += 1

        return result  # 최종 결과 반환