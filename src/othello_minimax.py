import copy
from variable import HEURISTIC_MODE

Nb_exploration = [0]


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
def minimax(node, depth, current_player: bool, maximizingPlayer: bool) -> (int, int):
    # Pour faire des mesures
    Nb_exploration[0] = Nb_exploration[0] + 1

    if depth == 0 or node.isLeaf():
        if HEURISTIC_MODE == 0:
            return node.computeHeuristic_cout(maximizingPlayer), None

    returnMove = None

    if current_player:
        value = float('-inf')

        for move in node.board.getPossiblePlay(maximizingPlayer):
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = minimax(Node(newBoard), depth - 1, False, maximizingPlayer)
            if result[0] > value:
                value = result[0]
                returnMove = move

    else:
        value = float('inf')
        for move in node.board.getPossiblePlay(not maximizingPlayer):
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = minimax(Node(newBoard), depth - 1, True, maximizingPlayer)
            if result[0] < value:
                value = result[0]
                returnMove = move

    return value, returnMove


def alpha_beta_minimax(node, depth, alpha, beta, current_player: bool, maximizingPlayer: bool) -> (int, int):
    # Pour faire des mesures
    Nb_exploration[0] = Nb_exploration[0] + 1

    if depth == 0 or node.isLeaf():
        if HEURISTIC_MODE == 0:
            return node.computeHeuristic_cout(maximizingPlayer), None

    returnMove = None

    if current_player:
        value = float('-inf')

        for move in node.board.getPossiblePlay(maximizingPlayer):
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = alpha_beta_minimax(Node(newBoard), depth - 1, alpha, beta, False, maximizingPlayer)

            if result[0] > value:
                value = result[0]
                returnMove = move

            if value >= beta:
                # print("beta cutoff")
                break
            alpha = max(alpha, value)

    else:
        value = float('inf')
        for move in node.board.getPossiblePlay(not maximizingPlayer):
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = alpha_beta_minimax(Node(newBoard), depth - 1, alpha, beta, True, maximizingPlayer)

            if result[0] < value:
                value = result[0]
                returnMove = move

            if alpha >= value:
                # print("alpha cutoff")
                break
            beta = min(beta, value)

    return value, returnMove
