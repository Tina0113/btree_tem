# -*- coding: utf-8 -*-

# B-Tree 作業樣板檔
# 最後更新：2025年10月8日

class BTreeNode:
    """
    B-Tree 的節點結構。
    
    Attributes:
        leaf (bool): 如果節點是葉節點則為 True。
        t (int): B-Tree 的最小階數 (Minimum Degree)。
        keys (list): 節點中儲存的鍵值列表。
        children (list): 指向子節點的指標列表。
    """
    def __init__(self, t, leaf=False):
        self.leaf = leaf
        self.t = t
        self.keys = []
        self.children = []

    def traverse(self):
        """
        以中序走訪的方式印出此節點為根的子樹的所有鍵值。
        這是一個遞迴函式。
        """
        # TODO: 實作節點的中序走訪
        # 提示：
        # 1. 如果不是葉節點，遞迴走訪第一個子節點 (children[0])
        # 2. 依序印出 (鍵值, 遞迴走訪下一個子節點)
        #    例如： print(key), traverse(children[1]), print(key), traverse(children[2]), ...
        pass


class BTree:
    """
    B-Tree 的主結構。

    Attributes:
        root (BTreeNode): B-Tree 的根節點。
        t (int): B-Tree 的最小階數 (Minimum Degree)。
    """
    def __init__(self, t):
        """
        BTree 的建構函式。
        """
        self.root = BTreeNode(t, leaf=True)
        self.t = t

    def search(self, k):
        """
        在 B-Tree 中搜尋鍵值 k。

        Args:
            k (int): 要搜尋的鍵值。
        
        Returns:
            bool: 如果找到鍵值 k 則回傳 True，否則回傳 False。
        """
        # TODO: 實作 B-Tree 的搜尋功能
        # 提示：從根節點開始，遞迴地往下尋找
        return self._search_recursive(self.root, k)

    def _search_recursive(self, x, k):
        """
        在以 x 為根的子樹中搜尋 k 的遞迴輔助函式。
        """
        # TODO: 實作遞迴搜尋的邏輯
        pass

    def insert(self, k):
        """
        在 B-Tree 中插入一個新的鍵值 k。
        """
        root = self.root
        # 如果根節點已滿，樹需要向上生長
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(self.t, leaf=False)
            self.root = new_root
            new_root.children.insert(0, root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, x, k):
        """
        在一個非滿的節點 x 中插入鍵值 k 的輔助函式。
        """
        # TODO: 實作在非滿節點中插入的邏輯
        # 提示：
        # 1. 如果 x 是葉節點，直接將 k 插入到 keys 中並保持排序。
        # 2. 如果 x 不是葉節點，找到 k 應該被插入的子節點。
        # 3. 如果該子節點已滿，先分裂它。
        # 4. 判斷 k 應該進入分裂後的哪個子節點，然後遞迴呼叫本函式。
        pass

    def _split_child(self, x, i):
        """
        分裂節點 x 的第 i 個已滿的子節點。
        """
        # TODO: 實作節點分裂的邏輯
        # 提示：
        # 1. y 是要分裂的節點 (x.children[i])
        # 2. z 是分裂後產生的新節點
        # 3. 將 y 中間的鍵值提升到父節點 x
        # 4. 將 y後半段的鍵值和子節點移動到 z
        pass

    def print_traversal(self):
        """
        公開的走訪方法，從根節點開始。
        """
        keys_list = []
        self._collect_keys_recursive(self.root, keys_list)
        print(" ".join(map(str, keys_list)))
    
    def _collect_keys_recursive(self, x, keys_list):
        """
        遞迴地收集所有鍵值到一個列表中。
        """
        if x is not None:
            i = 0
            while i < len(x.keys):
                if not x.leaf:
                    self._collect_keys_recursive(x.children[i], keys_list)
                keys_list.append(x.keys[i])
                i += 1
            
            if not x.leaf:
                self._collect_keys_recursive(x.children[i], keys_list)

def main():
    """
    主函式，用於讀取輸入並執行對應操作。
    """
    # 讀取 B-Tree 的最小階數 t
    try:
        t_input = input()
        t = int(t_input)
        if t < 2:
            # 根據 B-Tree 定義, t 必須 >= 2
            return
        btree = BTree(t)

        # 讀取後續指令
        while True:
            try:
                line = input()
                parts = line.split()
                command = parts[0]

                if command == "insert":
                    key = int(parts[1])
                    btree.insert(key)
                elif command == "search":
                    key = int(parts[1])
                    # 輸出 True 或 False
                    print(btree.search(key))
                elif command == "print":
                    btree.print_traversal()
                else:
                    # 可忽略無法識別的指令
                    pass
            except (EOFError, IndexError):
                # 讀到檔案結尾或空行時結束
                break
    except (ValueError, IndexError):
        # 處理 t 不是數字或空檔案的情況
        return


if __name__ == "__main__":
    main()
