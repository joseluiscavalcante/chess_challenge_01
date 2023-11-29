import chess
from engine import ChessEngine
from colorama import Fore, Style

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
                print("\n Hum... Estou pensando...")
                engine_move = self.engine.get_best_move(self.board)
                print(f"🤖 Essa é a melhor jogada, chefe!: {engine_move.uci()}")
                self.board.push(engine_move)

        self.display_result()
        self.engine.close()

    def ask_player_starts(self):
        while True:
            choice = input("Nosso oponente vai jogar primeiro? (S/N): ").lower()
            if choice in 'Ss':
                return True
            elif choice in 'Nn':
                return False
            else:
                print("Escolha inválida. Por favor, escolha 'S' ou 'N'.")

    def display_board(self):
        print("\n", end="")
        print(Fore.WHITE + "    a  b  c  d  e  f  g  h" + Style.RESET_ALL)
        print(Fore.BLACK + "  +------------------------+" + Style.RESET_ALL)
        for i in range(8, 0, -1):
            row = f"{i} |"
            for j in range(1, 9):
                square = chess.square(j - 1, i - 1)
                piece = self.board.piece_at(square)
                if piece:
                    colored_piece = self.color_piece(piece)
                    row += f" {colored_piece} "
                else:
                    row += " . "
            print(row + f"| {i}")
        print(Fore.BLACK + "  +------------------------+" + Style.RESET_ALL)
        print(Fore.WHITE + "    a  b  c  d  e  f  g  h" + Style.RESET_ALL)

    def color_piece(self, piece):
        if piece.color == chess.WHITE:
            return Fore.WHITE + piece_to_emoji(piece) + Style.RESET_ALL
        else:
            return Fore.BLACK + piece_to_emoji(piece) + Style.RESET_ALL

    def get_player_move(self):
        legal_moves = [move.uci() for move in self.board.legal_moves]
        while True:
            try:
                move_str = input("\nInsira a jogada do oponente (Ex.: e2e4): ")
                if move_str in legal_moves:
                    return move_str
                else:
                    print("Movimento inválido. Por favor faça um movimento válido!")
            except:
                print("Formato de movimento inválido. Utilize o formato UCI.")

    def display_result(self):
        result = self.board.result()
        print("\nFim de jogo!")
        if result == '1-0':
            print("Brancas venceram!")
        elif result == '0-1':
            print("Pretas venceram!")
        else:
            print("Deu empate!")

def piece_to_emoji(piece):
    piece_map = {
        chess.PAWN: "♙" if piece.color == chess.WHITE else "♟",
        chess.ROOK: "♖" if piece.color == chess.WHITE else "♜",
        chess.KNIGHT: "♘" if piece.color == chess.WHITE else "♞",
        chess.BISHOP: "♗" if piece.color == chess.WHITE else "♝",
        chess.QUEEN: "♕" if piece.color == chess.WHITE else "♛",
        chess.KING: "♔" if piece.color == chess.WHITE else "♚",
    }
    return piece_map.get(piece.piece_type, " ")

if __name__ == "__main__":
    game = ChessGame()
    game.play()
