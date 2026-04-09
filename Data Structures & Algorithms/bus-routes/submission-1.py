class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        n = len(routes)
        stops = defaultdict(list)
        for bus in range(n):
            for stop in routes[bus]:
                stops[stop].append(bus) 
        
        seen_bus = set()
        seen_stop = set([source])
        res = 0
        queue = deque([source])
        while queue:
            for _ in range(len(queue)):
                stop = queue.popleft()
                if stop == target:
                    return res
                for bus in stops[stop]:
                    if bus in seen_bus:
                        continue
                    seen_bus.add(bus)
                    for nxtStop in routes[bus]:
                        if nxtStop in seen_stop:
                            continue
                        seen_stop.add(nxtStop)
                        queue.append(nxtStop)
            res += 1
        return -1

       
