class MinStack:
    
    # 如果list = [1,2,3] 作為stack由上至下其實是3、2、1

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        # 移除頂部項
        self.items.pop()

    def top(self) -> int:
        # 取top需取最後一位
        return self.items[-1]
    
    def getMin(self) -> int:
        return min(self.items)
