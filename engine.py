# engine.py
import chess
import chess.engine

class ChessEngine:
    def __init__(self, 
                 stockfish_path = "C:\\Users\\jose_\\OneDrive\\Área de Trabalho\\chess01\\chess_challenge_01\\stockfish\\stockfish-windows-x86-64-modern.exe"):
        self.stockfish_path = stockfish_path
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        
        # Configurar o Stockfish para o nível mais avançado
        self.engine.configure({"Skill Level": 20, "Threads": 4, "Hash": 4096, "Use NNUE": True,
                               "Move Overhead": 30, "Slow Mover": 80, "UCI_LimitStrength": False, "UCI_Elo": 3000})

    def get_best_move(self, board):
        result = self.engine.play(board, chess.engine.Limit(time=10.0))  # Aumentando o tempo limite para melhor análise
        return result.move

    def close(self):
        self.engine.quit()

