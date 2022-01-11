from collections import Counter, defaultdict


def find_word_concatenation(strng, words):
    result_indices = []
    words_count = Counter(words)
    for i in range(len(strng)):
        flag = True
        cur_count = defaultdict(int)
        cur_index = i

        count = 0
        while flag and count < len(words):
            cur_word = strng[cur_index:cur_index + len(words[0])]
            if cur_word in words_count:
                cur_count[cur_word] += 1
                cur_index += len(words[0])
                count += 1
            else:
                flag = False
        if cur_count == words_count:
            result_indices.append(i)
    return result_indices


s = "foobarbarfoo"
words = ["foo", "bar"]
print(find_word_concatenation(s, words))


def find_word_concatenation2(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str1) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = str1[next_word_index: next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:  # Store index if we have found all the words
                result_indices.append(i)

    return result_indices
