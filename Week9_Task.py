import nltk
from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('stopwords')


class WorkingSentence:

    def __init__(self, sentence: str):
        self.originalSentence = sentence
        self.tokens = nltk.word_tokenize(sentence)
        self.tokensCount = len(nltk.word_tokenize(sentence))
        self.totalScore = 0
        self.normalizedScore = 0.0

    # if token is stopword than currentTokenScore = 0 and go to the next token
    def calculate_total_score(self, originalText):
        for token in self.tokens:
            if token not in set(stopwords.words('english')):  # checking for stopwords
                self.totalScore += nltk.word_tokenize(originalText).count(token)  # <- currentTokenScore
                # 'word_tokenize(originalText)' gives us all tokens from originalText
                # 'count(token)' gives us number of occurrences for token

        if self.tokensCount != 0:  # if tokensCount in current sentence is 0 than 'division by 0' error, need to check
            self.normalizedScore = self.totalScore / self.tokensCount


def main():
    originalText = ""
    # file with text should be in the same folder
    # or just put the full path
    with open('TextSample.txt', 'r') as originalFile:
        originalText = originalFile.read()  # read txt file and write its content into a variable 'originalText'

    sentences = []  # empty list for future sentences (WorkingSentence class)
    for sentence in nltk.tokenize.sent_tokenize(originalText):  # <- str sentences from 'originalText' via nltk
        s = WorkingSentence(sentence)  # create WorkingSentence object
        s.calculate_total_score(originalText)  # start 'Score stuff'
        sentences.append(s)  # add current WorkingSentence object to list

    sentencesCount = len(sentences)  # need to know the maximum possible value of N
    N = int(input("Enter a number (N): "))
    if N >= sentencesCount:  # if this occurs then end program
        print("Error! N shouldn't be greater that sentences count")
        return

    # now we need to sort out 'sentences' list using 'normalizedScore' value
    sortedSentences = sorted(sentences, key=lambda x: x.normalizedScore)

    # now we need to get N sentences with greatest normalizedScore
    bestSentences = sortedSentences[0:N]

    # and final print =)
    for sentence in sentences:
        if sentence in bestSentences:  # we need to use 'bestSentences' just to print them in original order
            print(sentence.originalSentence)


main()
