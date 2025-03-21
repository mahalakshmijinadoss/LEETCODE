class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True
        #create adjacency dictionary
        adj_list=defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        bfs_queue=deque([source])
        visited=set()
        visited.add(source)
        while bfs_queue:
            node=bfs_queue.pop()
            for neig_node in adj_list[node]:
                if neig_node== destination:
                    return True
                if neig_node not in visited:
                    visited.add(neig_node)
                    bfs_queue.append(neig_node)
        return False





        




























    