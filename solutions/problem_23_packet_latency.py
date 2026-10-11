"""23. Packet Broadcast Latency — see problems/23_packet_latency.md"""

from __future__ import annotations
import heapq

def dikstra(links: list[tuple[int, int, int]], src: int, n: int):
    #Making the graph 
    graph = {}
    for src_, dst_, ms in links:
        if src_ not in graph:
            graph[src_] = []
        graph[src_].append([dst_, ms])
    print("graph: ", graph)

    #Initializing values. 
    minDstToSrc= {
        i: float("inf") for i in range(n)
    }
    minPathToSrc = {
        i: [] for i in range(n)
    }
    minQue = [[0, src, []]]

    #Creating minimum distance to source dictionary 
    num = 1
    while minQue:
        dst, node, path = heapq.heappop(minQue)

        if dst <= minDstToSrc[node]:
            minDstToSrc[node] = dst
            minPathToSrc[node] = path
        else:
            continue

        for neighbour, neigh_dist in graph.get(node, {}): 
            newDist = dst + neigh_dist
            heapq.heappush(minQue, [newDist, neighbour, path + [neighbour]])
        # print("{} :For node {} we added this to min que {}".format(num, node, minQue))
        num+= 1
    return minDstToSrc, minPathToSrc


def broadcast_time(n: int, links: list[tuple[int, int, int]], source: int) -> int:
    minDstToSrc, _ =  dikstra(links, source, n)
    ans = max(values for key, values in minDstToSrc.items())
    return ans if ans != float("inf") else -1

def fastest_route(
    n: int, links: list[tuple[int, int, int]], src: int, dst: int
) -> tuple[int, list[int]] | None:
    minDstToSrc, minPathToSrc =  dikstra(links, src, n)
    return (minDstToSrc[dst], [src] + minPathToSrc[dst])

links = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
assert broadcast_time(4, links, 0) == 4  # -> 4   (node 3 is last, via 0->2->1->3)
print("✅")
assert fastest_route(4, links, 0, 3) ==  (4, [0, 2, 1, 3])# -> (4, [0, 2, 1, 3])
print("✅")
assert broadcast_time(3, [(0, 1, 1)], 0) == -1 # -> -1 (node 2 unreachable)
print("✅")

# print("Min Dist", dikstra(links, 0, 4))