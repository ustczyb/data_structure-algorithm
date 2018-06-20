"""
有向图的数据结构和基本操作
"""


class Graph(object):
    """
    图的邻接表表示方式
    """

    def __init__(self):
        """
        初始化图，我们用邻接表来表示图
        """
        self.num_v = 0
        self.num_e = 0
        self.adj_table = {}  # 邻接表

    def __repr__(self):
        return "num_v:" + str(self.num_v) + " num_e:" + str(self.num_e) + " adj_table:" + str(self.adj_table)

    def add_vex(self, v):
        self.num_v += 1
        self.adj_table[v] = []

    def add_edge(self, v1, v2):
        if not self.adj_table.get(v1):
            self.add_vex(v1)
        if not self.adj_table.get(v2):
            self.add_vex(v2)
        self.adj_table[v1].append(v2)
        self.adj_table[v2].append(v1)
        self.num_e += 1

    def get_adj_vexs(self, v):
        """
        获取v相邻的顶点 返回一个list
        :param v:
        :return:
        """
        return self.adj_table[v]

    def vex_set(self):
        return self.adj_table.keys()

    def edge_set(self):
        return self.adj_table.values()


def dfs(g, v):
    """
    1.深度优先遍历
    :param g: 图g
    :param v: 遍历的起始顶点
    :return: 深度优先遍历顺序
    """
    dfs_order = []
    visited_set = set()

    def do_dfs(v):
        if v in visited_set:
            return
        dfs_order.append(v)
        visited_set.add(v)
        for w in g.get_adj_vexs(v):
            do_dfs(w)

    do_dfs(v)
    return dfs_order


def dfs_path_to(g, start, end):
    """
    1.1 dfs寻路
    :param g:
    :param start: 起点
    :param end: 终点
    :return: start->end的一条路径
    """
    visited_set = set()
    path = [end]

    def next_node_on_path(start_vex, end_vex):
        if start_vex in visited_set:
            return None
        visited_set.add(start_vex)
        if end_vex in g.get_adj_vexs(start_vex):    # 找到路径，返回
            path.append(start_vex)
            return start_vex
        for adj_vex in g.get_adj_vexs(start_vex):   # 未找到，递归寻找
            if next_node_on_path(adj_vex, end_vex):
                path.append(start_vex)
                return start_vex
        return None

    next_node_on_path(start, end)
    path.reverse()
    return path


def bfs(g, v):
    """
    2.广度优先遍历
    :param g: 图g
    :param v: 遍历的起始顶点
    :return: 广度优先遍历顺序
    """
    bfs_order = []
    vex_queue = [v]
    visited_set = set()
    while vex_queue:
        w = vex_queue.pop(0)
        if w in visited_set:
            continue
        bfs_order.append(w)
        visited_set.add(w)
        for w_adj in g.get_adj_vexs(w):
            if w_adj not in visited_set:
                vex_queue.append(w_adj)
    return bfs_order


def bfs_path(g, start, end):
    """
    2.1 bfs寻路
    :param g:
    :param start:
    :param end:
    :return: start->end的路径 类型为list
    """
    path_previes_vex = {}

    def bfs_path_init(v):
        path_previes_vex[v] = v
        vex_queue = [v]
        marked = set([v])
        while vex_queue:
            w = vex_queue.pop(0)
            for w_adj in g.get_adj_vexs(w):
                if w_adj not in marked:
                    vex_queue.append(w_adj)
                    path_previes_vex[w_adj] = w
                    marked.add(w_adj)

    if not path_previes_vex:
        bfs_path_init(start)
    path = [end]
    p = end
    while path_previes_vex[p] and not p == path_previes_vex[p]:
        path.append(path_previes_vex[p])
        p = path_previes_vex[p]
    path.reverse()
    return path


def connected_component(g):
    """
    3.图g的连通分量个数
    :param g:
    :return:
    """
    visited_set = set()
    conn_components = {}
    count = 0

    def do_dfs(v):
        if v in visited_set:
            return
        visited_set.add(v)
        conn_components[count].append(v)
        for w in g.get_adj_vexs(v):
            do_dfs(w)

    for v in g.vex_set():
        if v not in visited_set:
            count += 1
            conn_components[count] = []
            do_dfs(v)
    return conn_components


def init_graph(path):
    """
    初始化并返回一个图
    :return:
    """
    file = open(path, 'r')
    vex_num = file.readline()
    edge_num = file.readline()
    graph = Graph()
    while True:
        line = file.readline()
        if not line:
            break
        vex_list = line.split()
        graph.add_edge(vex_list[0], vex_list[1])
    return graph


if __name__ == '__main__':
    graph = init_graph('/Users/zyb/IdeaProjects/data_structure&algorithm/data/tinyG.txt')
    # print(graph)
    # print(dfs(graph, '0'))
    # print(bfs(graph, '0'))
    # print(dfs_path_to(graph, '0', '3'))
    print(connected_component(graph))
    # print(bfs_path(graph, '0', '3'))
