# main.py
import chess
from engine import ChessEngine

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.engine = ChessEngine()

    def play(self):
        player_starts = self.ask_player_starts()

        while not self.board.is_game_over():
            self.display_board()

            if (player_starts and self.board.turn == chess.WHITE) or (not player_starts and self.board.turn == chess.BLACK):
                move_uci = self.get_player_move()
                move = chess.Move.from_uci(move_uci)
                self.board.push(move)
            else:
                engine_move = self.engine.get_best_move(self.board)
                print(f"\nStockfish plays: {engine_move.uci()}")
                self.board.push(engine_move)

        self.display_result()
        self.engine.close()

    def ask_player_starts(self):
        while True:
            choice = input("Do you want to play first? (yes/no): ").lower()
            if choice == 'yes':
                return True
            elif choice == 'no':
                return False
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    def display_board(self):
        print("\n    a  b  c  d  e  f  g  h")
        print("  +------------------------+")
        for i in range(8, 0, -1):
            row = f"{i} |"
            for j in range(1, 9):
                piece = self.board.piece_at(chess.square(j - 1, i - 1))
                if piece:
                    row += f" {piece.symbol()} "
                else:
                    row += " . "
            print(row + f"| {i}")
        print("  +------------------------+")
        print("    a  b  c  d  e  f  g  h")

    def get_player_move(self):
        legal_moves = [move.uci() for move in self.board.legal_moves]
        while True:
            try:
                move_str = input("\nEnter your move (e.g., e2e4): ")
                if move_str in legal_moves:
                    return move_str
                else:
                    print("Invalid move. Please enter a legal move.")
            except:
                print("Invalid move format. Please enter a move in UCI format.")

    def display_result(self):
        result = self.board.result()
        print("\nGame Over")
        if result == '1-0':
            print("White wins!")
        elif result == '0-1':
            print("Black wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    game = ChessGame()
    game.play()
