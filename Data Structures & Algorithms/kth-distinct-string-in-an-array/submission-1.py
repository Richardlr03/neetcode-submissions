class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        duplicates = set()
        seen = set()

        for ch in arr:
            if ch not in seen:
                seen.add(ch)
            else:
                duplicates.add(ch)

        count = 0
        for ch in arr:
            if ch not in duplicates:
                count += 1
            if count == k:
                return ch

        return ""