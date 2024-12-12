class ScoreLimitExceedError(Exception):
    """Исключение, выбрасываемое при попытке добавить очки, превышающие лимит."""
    def __init__(self):
        super().__init__("Очки не могут быть больше 1000.")


class GameScore:
    """Класс для отслеживания очков игрока с ограничениями."""
    def __init__(self):
        """Инициализируем начальное значение очков."""
        self.score = 0

    def add_score(self, points):
        """Добавляет очки к текущему счету, проверяя лимит."""
        if self.score + points > 1000:
            raise ScoreLimitExceedError()
        self.score += points


    def subtract_score(self, points):
        """Уменьшает очки, проверяя, чтобы счёт не стал отрицательным."""
        if self.score - points < 0:
            raise ValueError("Очки не могут быть отрицательными.")
        self.score -= points


game_score = GameScore()

try:
    game_score.add_score(500)
    print(f"Текущий счет: {game_score.score}")

    game_score.add_score(600)
except ScoreLimitExceedError as e:
    print(e)

try:
    game_score.subtract_score(600)
except ValueError as e:
    print(e)

try:
    game_score.subtract_score(100)
    print(f"Текущий счёт после вычитания: {game_score.score}")
except ValueError as e:
    print(e)
