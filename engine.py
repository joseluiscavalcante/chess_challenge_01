# engine.py
import chess
import chess.engine

class ChessEngine:
    def __init__(self, stockfish_path="C:\\Users\\usuario1\\Documents\\Cavalcante\\Projects\\chess_ia\\stockfish\\stockfish-windows-x86-64-modern.exe"):
        self.stockfish_path = stockfish_path
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        
        # Configurar o Stockfish para a dificuldade máxima com limitação de força
        self.engine.configure({"Skill Level": 20, "Threads": 4, "Hash": 1024, "UCI_LimitStrength": True, "UCI_Elo": 2000})

    def get_best_move(self, board):
        result = self.engine.play(board, chess.engine.Limit(time=2.0))
        return result.move

    def close(self):
        self.engine.quit()
