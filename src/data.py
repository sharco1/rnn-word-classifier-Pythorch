import torch
import glob
import unicodedata
import string
import os


all_letters = string.ascii_letters + " .,;'-"
n_letters = len(all_letters)


def findFiles(path):
    return glob.glob(path)


def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )
print(unicodeToAscii('Ślusàrski'))


def readLines(filename):
    lines = open(filename, encoding="utf8").read().strip().split('\n')
    return [unicodeToAscii(line) for line in lines]


category_lines = {}
all_categories = []
for filename in findFiles('../input/data/names/*.txt'):
    category = os.path.splitext(os.path.basename(filename))[0]
    all_categories.append(category)
    lines = readLines(filename)
    category_lines[category] = lines

n_categories = len(all_categories)
print(category_lines['English'][:5])


def letterToIndex(letter):
    return all_letters.find(letter)


def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor

def letterToIndex(letter):
    return all_letters.find(letter)

def letterToTensor(letter):
    tensor = torch.zeros(1, n_letters)
    tensor[0][letterToIndex(letter)] = 1
    return tensor

def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor

print(letterToTensor('A'))
print(lineToTensor('Abel').size())
