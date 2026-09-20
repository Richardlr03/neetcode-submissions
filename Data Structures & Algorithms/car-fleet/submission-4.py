class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        count = n
        for i in range(n):
            cars.append((position[i], speed[i]))

        cars.sort(key=lambda x:x[0])
        cur_velo = None
        cur_pos = None

        for i in range(n-1, -1, -1):
            pos1, velo1 = cars[i]
            if not cur_velo:
                cur_velo = velo1
                cur_pos = pos1
                continue
            if cur_velo >= velo1:
                cur_velo = velo1
                cur_pos = pos1
                continue
            time = (cur_pos - pos1) / (velo1 - cur_velo)
            dest = time * velo1 + pos1
            if dest <= target:
                count -= 1
            else:
                cur_pos = pos1
                cur_velo = velo1

        return count