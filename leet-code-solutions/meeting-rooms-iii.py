class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        minHeap = []
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        used = {}
    

        for s, e in meetings:
            while minHeap and minHeap[0][0] <= s:
                end,r = heapq.heappop(minHeap)
                heapq.heappush(rooms, r)

            if rooms:
                room = heapq.heappop(rooms)
                heapq.heappush(minHeap, (e, room))
                used[room] = used.get(room, 0) + 1

            else:
                end, r = heapq.heappop(minHeap)
                heapq.heappush(minHeap, (end + (e - s), r))
                used[r] = used.get(r, 0) + 1

        v, res = 0, 0
        for key, val in used.items():
            if val > v:
                res = key
                v = val
            if val == v:
                res = min(res, key)

        return res