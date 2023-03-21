from collections import Counter
from typing import Counter as CounterType, Tuple, List


def compute_words_frequency(sentence: str, limit: int) -> List[Tuple[str, int]]:
    if limit < 0:
        raise ValueError("The limit should be positive")

    words = sentence.split()

    words_frequency: CounterType[str] = Counter(words)

    words_frequency_results = list(words_frequency.items())
    words_frequency_results.sort(key=lambda x: (-x[1], x[0]))

    return words_frequency_results[:limit]
