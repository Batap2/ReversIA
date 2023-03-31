class Node:
    board = None
    value = None

    def __init__(self, board):
        self.board = board

    def computeHeuristic_cout(self, color: bool):
        count = 0
        for row in self.board:
            for piece in row:
                if piece == 0:
                    break;
                if piece.color == color:
                    count = count + 1
                else:
                    count = count - 1
        self.value = count

    def isLeaf(self) -> bool:
        return self.board.isGameFinished()


def minimax(node, depth, maximizingPlayer: bool) -> int:
    if depth == 0 or node.isLeaf():
        return node.value

    if maximizingPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, minimax(child, depth-1, False))
    else:
        value = float('inf')
        for child in node.children:
            value = max(value, minimax(child, depth - 1, True))

    return value
