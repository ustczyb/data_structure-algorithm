"""
红黑树
红黑树的本质是一棵2-3树
黑链接对应2-3树的普通链接，红链接对应2-3树中3-结点的链接
黑链接指向的结点称为黑结点，红链接指向的结点称为红结点 根节点是黑结点
为了方便起见 我们让红链接都为左链接
API:
1.insert
2.delete
3.contains
4.find_min

"""


class RedBlackNode(object):
    """
    红黑树的结点类
    我们用一个bool值表示颜色 False表示黑色 True表示红色 color表示这个节点是否是一个3-节点
    """

    def __init__(self, val):
        self.val = val
        self.color = True
        self.left = None
        self.right = None


def find_closest(root, val):
    if root.val < val and not root.right:
        return find_closest(root.right, val)
    if root.val > val and not root.left:
        return find_closest(root.left, val)
    return root


def r_rotate(node):
    """
    右旋操作
        A                 B
       /        ->         \
      B                     A
    :return:
    """
    l_child = node.left
    node.left = l_child.right
    l_child.right = node
    color = node.color
    node.color = l_child.color
    l_child.color = color
    return l_child


# 左旋操作
def l_rotate(node):
    r_child = node.right
    node.right = r_child.left
    r_child.left = node
    color = node.color
    node.color = r_child.color
    r_child.color = color
    return r_child


# 将一个4-结点分解为两个2-结点
def flip_color(node):
    node.color = not node.color
    node.left.color = not node.left.color
    node.right.color = not node.right.color


def is_red(node):
    if not node:
        return False
    return node.color


def insert(root, val):
    """
    向root所在的子树中插入值为val的节点，返回插入后子树的根节点
    :param root:
    :param val:
    :return:
    """
    if not root:
        return RedBlackNode(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    if is_red(root.right) and not is_red(root.left):
        root = l_rotate(root)
    if is_red(root.left) and is_red(root.left.left):
        root = r_rotate(root)
    # 4结点拆分为两个2-结点
    if is_red(root.left) and is_red(root.right):
        flip_color(root)
    return root


def print_tree(node, depth=0):
    for i in range(depth):
        print('\t', end='')
    # 叶子结点
    if not node:
        print('#')
        return
    # 当前结点
    if node.color:
        print(node.val, '*')
    else:
        print(node.val)
    # 孩子结点
    print_tree(node.left, depth + 1)
    print_tree(node.right, depth + 1)


class RedBlackTree(object):
    """
    红黑树
    """

    def __init__(self):
        self.root = None  # 根节点
        self.size = 0  # 红黑树结点个数

    def find_min(self, val):
        if not self.root:
            return None
        p_node = self.root

    def insert(self, val):
        # 输入合法性判断，这里略过
        self.size += 1
        # 空树插入根节点
        if not self.root:
            self.root = RedBlackNode(val)
            self.root.color = False
        else:
            self.root = insert(self.root, val)

    def print(self):
        print_tree(self.root)


if __name__ == '__main__':
    tree = RedBlackTree()
    for i in range(10):
        tree.insert(i)
    tree.print()