class Solution:
    def minimumCost(self, n, edges: List[List[int]], queries):
        node_union_map = {}
        component_cost = {}
        uid_set = {}
        result = []
        uid = 1

        def helper(uid: int, mx_set: set, mn_set: set):
            for v in mn_set:
                node_union_map[v] = uid
                mx_set.add(v)
            return mx_set

        for edge in edges:
            u, v, w = edge
            cuid = None
            if u in node_union_map and v in node_union_map:
                u_uid = node_union_map[u]
                v_uid = node_union_map[v]
                if u_uid == v_uid:
                    component_cost[u_uid] &= w
                    continue
                u_set = uid_set[u_uid]
                v_set = uid_set[v_uid]

                if len(u_set) >= len(v_set):
                    u_set = helper(u_uid, u_set, v_set)
                    uid_set[u_uid] = u_set
                    component_cost[u_uid] &= component_cost[v_uid]
                    component_cost[u_uid] &= w
                    del uid_set[v_uid]
                    del component_cost[v_uid]
                else:
                    v_set = helper(v_uid, v_set, u_set)
                    uid_set[v_uid] = v_set
                    component_cost[v_uid] &= component_cost[u_uid]
                    component_cost[v_uid] &= w
                    del uid_set[u_uid]
                    del component_cost[u_uid]
            elif u in node_union_map:
                node_union_map[v] = node_union_map[u]
                cuid = node_union_map[u]
                component_cost[cuid] &= w
                set_u = uid_set[cuid]
                set_u.add(v)
                uid_set[cuid] = set_u
            elif v in node_union_map:
                node_union_map[u] = node_union_map[v]
                cuid = node_union_map[v]
                component_cost[cuid] &= w
                set_v = uid_set[cuid]
                set_v.add(u)
                uid_set[cuid] = set_v
            else:
                node_union_map[u], node_union_map[v] = uid, uid
                cuid = uid
                component_cost[cuid] = w
                uid += 1
                uid_set[cuid] = set([u, v])
        for s, t in queries:
            if (
                s in node_union_map
                and t in node_union_map
                and node_union_map[s] == node_union_map[t]
            ):
                cuid = node_union_map[s]
                result.append(component_cost[cuid])
            else:
                result.append(-1)
        return result