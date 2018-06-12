"""
并查集
API:
1.union(p, q)   在p, q中添加一条连接
2.find(p)   寻找p所在连通分量的标识符（名称）
3.connected(p, q)    p, q是否连通
4.count()   连通分量的数量

实现有以下几种思路：
1.quick-find 即find操作在O(1)时间内完成
2.quick-union 即union操作在O(1)时间内完成
对于2 还有两种改善的思路
2.1 加权合并 执行union操作时，将小子树合并到大子树上
2.2 路径压缩 在执行find操作时，更新relation数组为根节点
核心api是1和2 我们希望我们的数据结构使得1和2尽可能的快
"""


class UnionFindSet(object):
    def __init__(self, input_set):
        """
        并查集在初始化时，每个点都是孤立点，所以每个点所在联通分类的标示为它自己
        :param input_set: 输入集合（点集）
        """
        self.input_set = input_set
        self.__relaction_dict__ = {}
        for i in input_set:
            self.__relaction_dict__[i] = i

    def union(self, p, q):
        """
        将p,q两点连一条线（合并到同一个连通分量）
        这里为quick-union的算法实现
        :param p:
        :param q:
        :return:
        """
        self.__relaction_dict__[p] = q

    def find(self, p):
        """
        寻找p所在的连通分量
        这里为quick-union的算法实现
        :param p:
        :return:
        """
        while not p == self.__relaction_dict__[p]:
            # p = self.__relaction_dict__[p]
            # 路径压缩
            p = self.find(self.__relaction_dict__[p])
        return p

    def connected(self, p, q):
        """
        判断p q是否连通
        :param p:
        :param q:
        :return:
        """
        p_type = self.find(p)
        q_type = self.find(q)
        return p_type == q_type

    def count(self):
        """
        求图中连通分量个数
        :return:
        """
        return len(set(self.__relaction_dict__.values()))


if __name__ == '__main__':
    dict = {}
    dict[1] = 1
    dict[2] = 1
