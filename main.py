from typing import Dict, Tuple, List


def compute_words_frequency(sentence: str, limit: int) -> List[Tuple[str, int]]:
    if limit < 0:
        raise ValueError("The limit should be positive")

    words = sentence.split()

    words_frequency: Dict[str, int] = {}
    for word in words:
        if word in words_frequency:
            words_frequency[word] += 1
        else:
            words_frequency[word] = 1

    words_frequency_results = list(words_frequency.items())
    words_frequency_results.sort(key=lambda x: x[0])
    words_frequency_results.sort(key=lambda x: x[1], reverse=True)

    return words_frequency_results[:limit]
