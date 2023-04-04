import copy


class Node:
    board = None

    def __init__(self, board):
        self.board = board

    def computeHeuristic_cout(self, color: bool) -> int:
        count = 0
        for square in self.board.board:
                if square == 0:
                    break;
                if square.color == color:
                    count = count + 1
                else:
                    count = count - 1
        return count

    def isLeaf(self) -> bool:
        return self.board.isGameFinished()


# Retourne le score et le coup (le déplacement)
# TODO : faut élaguer
def getMoveMinimax(node, depth, current_player: bool, maximizingPlayer: bool) -> (int, int):
    if depth == 0 or node.isLeaf():
        return node.computeHeuristic_cout(maximizingPlayer), None

    returnMove = None

    if current_player:
        value = float('-inf')

        for move in node.board.getPossiblePlay(maximizingPlayer):
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = getMoveMinimax(Node(newBoard), depth - 1, False, maximizingPlayer)
            if result[0] > value:
                value = result[0]
                returnMove = move

    else:
        value = float('inf')
        for move in node.board.getPossiblePlay(not maximizingPlayer):
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = getMoveMinimax(Node(newBoard), depth - 1, True, maximizingPlayer)
            if result[0] < value:
                value = result[0]
                returnMove = move

    return value, returnMove
