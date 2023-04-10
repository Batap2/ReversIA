import copy
from othello.board_variable import *

Nb_exploration = [0]


class Node:
    board = None

    def __init__(self, board):
        self.board = board

    def computeHeuristic_cout(self, color: bool) -> int:
        count = 0
        for square in self.board.board:
            if square == 0:
                continue
            if square.color == color:
                count = count + 1
            else:
                count = count - 1
        return count

    # black pawns, black corners, black weightValue, white pawns, white corners, white weightValue
    def countPawnCornersWeightMap(self) -> (int, int, int, int, int, int):
        w = 0
        b = 0
        wc = 0
        bc = 0
        ww = 0
        bw = 0

        weightMap = [
            20, -3, 11, 8, 8, 11, -3, 20,
            -3, -7, -4, 1, 1, -4, -7, -3,
            11, -4, 2, 2, 2, 2, -4, 11,
            8, 1, 2, -3, -3, 2, 1, 8,
            8, 1, 2, -3, -3, 2, 1, 8,
            11, -4, 2, 2, 2, 2, -4, 11,
            -3, -7, -4, 1, 1, -4, -7, -3,
            20, -3, 11, 8, 8, 11, -3, 20
        ]

        for i in range(len(self.board.board)):
            piece = self.board.board[i]

            if piece != 0:
                if piece.color:
                    w = w + 1
                    ww = ww + weightMap[i]
                    if i == 0 or i == SIZE or i == (SIZE * SIZE - SIZE) or i == SIZE * SIZE:
                        wc = wc + 1
                else:
                    b = b + 1
                    bw = bw + weightMap[i]
                    if i == 0 or i == SIZE or i == (SIZE * SIZE - SIZE) or i == SIZE * SIZE:
                        bc = bc + 1

        return b, bc, bw, w, wc, ww

    def computeHeuristic2(self, color: bool):
        res = self.countPawnCornersWeightMap()

        # index pour retrouver les corners dans res
        if color:
            indexMaxPawn = 3
            indexMaxCorner = 4
            indexMaxWeightValue = 5
            indexMinPawn = 0
            indexMinCorner = 1
            indexMinWeightValue = 2
        else:
            indexMaxPawn = 0
            indexMaxCorner = 1
            indexMaxWeightValue = 2
            indexMinPawn = 3
            indexMinCorner = 4
            indexMinWeightValue = 5

        coinParityHeuristicValue = 100 * (res[indexMaxPawn] - res[indexMinPawn]) / (
                res[indexMaxPawn] + res[indexMinPawn])

        maxPlayerMoves = len(self.board.getPossiblePlay(color))
        minPlayerMoves = len(self.board.getPossiblePlay(not color))

        if maxPlayerMoves + minPlayerMoves != 0:
            mobilityHeuristicValue = 100 * (maxPlayerMoves - minPlayerMoves) / (maxPlayerMoves + minPlayerMoves)
        else:
            mobilityHeuristicValue = 0

        if res[indexMaxCorner] + res[indexMinCorner] != 0:
            cornerHeuristicValue = 100 * (res[indexMaxCorner] - res[indexMinCorner]) / (
                    res[indexMaxCorner] + res[indexMinCorner])
        else:
            cornerHeuristicValue = 0

        return coinParityHeuristicValue + mobilityHeuristicValue + cornerHeuristicValue

    def computeHeuristic3(self, color: bool):
        res = self.countPawnCornersWeightMap()

        # index pour retrouver les corners dans res
        if color:
            indexMaxPawn = 3
            indexMaxCorner = 4
            indexMaxWeightValue = 5
            indexMinPawn = 0
            indexMinCorner = 1
            indexMinWeightValue = 2
        else:
            indexMaxPawn = 0
            indexMaxCorner = 1
            indexMaxWeightValue = 2
            indexMinPawn = 3
            indexMinCorner = 4
            indexMinWeightValue = 5

        coinParityHeuristicValue = 100 * (res[indexMaxPawn] - res[indexMinPawn]) / (
                res[indexMaxPawn] + res[indexMinPawn])

        maxPlayerMoves = len(self.board.getPossiblePlay(color))
        minPlayerMoves = len(self.board.getPossiblePlay(not color))

        if maxPlayerMoves + minPlayerMoves != 0:
            mobilityHeuristicValue = 100 * (maxPlayerMoves - minPlayerMoves) / (maxPlayerMoves + minPlayerMoves)
        else:
            mobilityHeuristicValue = 0

        if res[indexMaxCorner] + res[indexMinCorner] != 0:
            cornerHeuristicValue = 100 * (res[indexMaxCorner] - res[indexMinCorner]) / (
                    res[indexMaxCorner] + res[indexMinCorner])
        else:
            cornerHeuristicValue = 0

        if res[indexMaxWeightValue] + res[indexMinWeightValue] != 0:
            weightParity = 100 * (res[indexMaxWeightValue] - res[indexMinWeightValue]) / (
                        res[indexMaxWeightValue] + res[indexMinWeightValue])
        else:
            weightParity = 0
        # weightParity = res[indexMaxWeightValue] - res[indexMinWeightValue]

        return coinParityHeuristicValue + mobilityHeuristicValue + cornerHeuristicValue + weightParity

    def isLeaf(self) -> bool:
        return self.board.isGameFinished()


# Retourne le score et le coup (le déplacement)
def minimax(node, depth, current_player: bool, maximizingPlayer: bool) -> (int, int):
    # Pour faire des mesures
    Nb_exploration[0] = Nb_exploration[0] + 1

    if depth == 0 or node.isLeaf():
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


def alpha_beta_minimax(node,
                       depth,
                       alpha,
                       beta,
                       current_player: bool,
                       maximizingPlayer: bool,
                       heuristic: int,
                       maxPlayerMoves: int = 0,
                       minPlayerMoves: int = 0) -> (int, int):
    # Pour faire des mesures
    Nb_exploration[0] = Nb_exploration[0] + 1

    if depth == 0 or node.isLeaf():
        if heuristic == 0:
            return node.computeHeuristic_cout(maximizingPlayer), None
        elif heuristic == 1:
            return node.computeHeuristic2(maximizingPlayer), None
        elif heuristic == 2:
            return node.computeHeuristic3(maximizingPlayer), None

    returnMove = None

    if current_player:
        value = float('-inf')

        availableMoves = node.board.getPossiblePlay(maximizingPlayer)

        for move in availableMoves:
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = alpha_beta_minimax(Node(newBoard), depth - 1, alpha, beta, False, maximizingPlayer, heuristic)

            # pour pas que ça renvoie un move null
            if returnMove == None:
                returnMove = move

            if result[0] > value:
                value = result[0]
                returnMove = move

            # beta cutoff
            if value >= beta:
                break
            alpha = max(alpha, value)

    else:
        value = float('inf')

        availableMoves = node.board.getPossiblePlay(not maximizingPlayer)

        for move in availableMoves:
            newBoard = copy.deepcopy(node.board)
            newBoard.applyMove(move, current_player)

            result = alpha_beta_minimax(Node(newBoard), depth - 1, alpha, beta, True, maximizingPlayer, heuristic)

            # pour pas que ça renvoie un move null
            if returnMove == None:
                returnMove = move

            if result[0] < value:
                value = result[0]
                returnMove = move

            # alpha cutoff
            if alpha >= value:
                break
            beta = min(beta, value)

    return value, returnMove

# le negaMax est bizarre, le resultat n'est pas le même qu'avec minimax
def negaMax(node,
            depth,
            alpha,
            beta,
            current_player: bool,
            maximizingPlayer: bool,
            heuristic: int,
            maxPlayerMoves: int = 0,
            minPlayerMoves: int = 0) -> (int, int):
    # Pour faire des mesures
    Nb_exploration[0] = Nb_exploration[0] + 1

    if depth == 0 or node.isLeaf():
        if heuristic == 0:
            return node.computeHeuristic_cout(maximizingPlayer), None
        elif heuristic == 1:
            return node.computeHeuristic2(maximizingPlayer), None
        elif heuristic == 2:
            return node.computeHeuristic3(maximizingPlayer), None

    returnMove = None

    value = float('-inf')

    availableMoves = node.board.getPossiblePlay(maximizingPlayer)

    for move in availableMoves:
        newBoard = copy.deepcopy(node.board)
        newBoard.applyMove(move, current_player)

        result = negaMax(Node(newBoard), depth - 1, -beta, -alpha, not current_player, maximizingPlayer, heuristic)

        # pour pas que ça renvoie un move null
        if returnMove == None:
            returnMove = move

        # value = max(value, -negamax)
        if -result[0] > value:
            value = -result[0]
            returnMove = move

        if -result[0] >= alpha:
            alpha = -result[0]
            returnMove = move
            if alpha >= beta:
                break

    return value, returnMove
