"""
有向图相关的基本算法
"""
from graph_alg.graph import Graph, init_graph


class DiGraph(Graph):
    def add_edge(self, v1, v2):
        if not self.adj_table.get(v1):
            self.add_vex(v1)
        if not self.adj_table.get(v2):
            self.add_vex(v2)
        self.adj_table[v1].append(v2)
        self.num_e += 1


def reverse_graph(g):
    """
    有向图取反
    :param g: 有向图
    :return:
    """
    g_reverse = DiGraph()
    for v in g.vex_set():
        for w in g.get_adj_vexs(v):
            g_reverse.add_edge(w, v)
    return g_reverse


def find_cycle(g):
    """
    寻找有向环，若存在则返回一个，不存在返回空list
    :param g:
    :return:
    """
    cycle = []
    visited_stack = []

    def do_dfs(v):
        """
        dfs寻路 利用栈进行回溯
        :param v:
        :return:
        """
        visited_stack.append(v)
        for w in g.get_adj_vexs(v):
            if cycle:
                return
            if w in visited_stack:  # 找到有向环
                cycle.append(w)
                p = visited_stack.pop()
                while not p == w:
                    cycle.append(p)
                    p = visited_stack.pop()
                return
            else:
                do_dfs(w)
        visited_stack.pop()

    for v in g.vex_set():
        do_dfs(v)
        if cycle:
            return cycle
    return cycle


def post_reverse_order(g):
    """
    逆后序
    :param g:
    :return:
    """
    order = []
    visited = set()

    def do_dfs(v):
        """
        后序遍历
        :param v: dfs遍历完成后，加入order序列
        :return:
        """
        if v in visited:
            return
        visited.add(v)
        for w in g.get_adj_vexs(v):
            do_dfs(w)
        order.append(v)

    for v in g.vex_set():
        do_dfs(v)
    order.reverse()
    return order


def topological_order(g):
    """
    拓扑排序 若是有向无环图，返回一个排序序列，否则返回空list
    :param g:
    :return:
    """
    if find_cycle(g):
        return []
    return post_reverse_order(g)


def strong_conn_component(g):
    """
    强连通分量
    :param g:
    :return:
    """
    visited = set()
    conn_components = {}
    count = 0
    g_reverse = reverse_graph(g)
    order_g_reverse = post_reverse_order(g_reverse)
    print(order_g_reverse)

    def do_dfs(v):
        if v in visited:
            return
        visited.add(v)
        conn_components[count].append(v)
        for w in g.get_adj_vexs(v):
            do_dfs(w)

    for v in order_g_reverse:
        if v not in visited:
            count += 1
            conn_components[count] = []
            do_dfs(v)
    return conn_components



def init_digraph(path):
    """
    初始化并返回一个图
    :return:
    """
    file = open(path, 'r')
    vex_num = file.readline()
    edge_num = file.readline()
    graph = DiGraph()
    while True:
        line = file.readline()
        if not line:
            break
        vex_list = line.split()
        graph.add_edge(vex_list[0], vex_list[1])
    return graph


if __name__ == '__main__':
    digraph = init_digraph('/Users/zyb/IdeaProjects/data_structure&algorithm/data/tinyDG.txt')
    # print(find_cycle(digraph))
    # print(topological_order(digraph))
    print(strong_conn_component(digraph))