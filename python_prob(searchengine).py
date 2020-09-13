
def match_string(string1, string2):
    words1 = string1.split(' ')
    words2 = string2.split(' ')
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1

    return score


if __name__ == '__main__':
    Sentences = ["Python is cool", "python is good",
                 "python is not python snake"]
    user = input('Enter your string\n')
    scores = [match_string(user, sentence) for sentence in Sentences]
    sortedlist = [sort for sort in sorted(
        zip(scores, Sentences), reverse=True)]

    for item, list in sortedlist:
        print(f'{item} results found in: {list}')
