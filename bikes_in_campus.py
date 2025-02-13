class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        hash_map = {}
        m = len(workers)
        n = len(bikes)
        result = [-1] * m

        mini = float("inf")
        maxi = float("-inf")

        for i in range(m):
            for j in range(n):
                distance = self.calculate_distance(workers[i], bikes[j])
                mini = min(mini, distance)
                maxi = max(maxi, distance)

                if distance not in hash_map:
                    hash_map[distance] = []
                hash_map[distance].append((i, j))

        assigned_workers = [False] * m
        assigned_bikes = [False] * n
        count = 0

        for i in range(mini, maxi + 1):
            if i not in hash_map:
                continue
            li = hash_map[i]

            for worker, bike in li:
                if not assigned_bikes[bike] and not assigned_workers[worker]:
                    result[worker] = bike  # Assign bike to worker
                    assigned_bikes[bike] = True
                    assigned_workers[worker] = True
                    count += 1
                if count == m:
                    return result

        return result

    def calculate_distance(self, worker, bike):
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])


# time complexity is O(m*n)
# space complexity is O(m*n)
