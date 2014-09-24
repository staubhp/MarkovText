import random
inputText = open('input.txt', 'r').read()
inputWords = inputText.split()


def createFrequencyTable():
	frequencyTable = {}
	i = 0;
	for inputWord in inputWords:
		if i+1 == len(inputWords):
			break

		nextWord = inputWords[i+1]
		frequencies = frequencyTable.get(inputWord,{})
		occurenceCount = frequencies.get(nextWord, 0)  
		occurenceCount += 1
		frequencies[nextWord] = occurenceCount 
		frequencyTable[inputWord] = frequencies
		i += 1
	return frequencyTable

def markov(frequencyTable):
	markov_list = []
	currentWord = inputWords[random.randrange(0, len(inputWords))] 
	while (len(markov_list) < 100):
		markov_list.append(currentWord)
		frequencies = frequencyTable[currentWord]
		weightedList = []
		for key in frequencies:
			for i in range (0, frequencies[key]):
				weightedList.append(key)
		currentWord = weightedList[random.randrange(0, len(weightedList))]
	return ' '.join(markov_list)

frequencyTable = createFrequencyTable()
print(markov(frequencyTable))
