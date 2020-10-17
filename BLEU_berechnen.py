from nltk.translate.bleu_score import sentence_bleu 
import argparse

def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hypothesis" ,help="Your own translation/Translation you want to calculate BLEU score on")
    parser.add_argument("--reference", help="Reference file")
    
    args = parser.parse_args()
    return args

argument = argparser()
hypothesis = open(argument.hypothesis, "r").readlines()
reference = open(argument.reference, "r").readlines()
BLEU_score = 0

for i in range(len(reference)):
    BLEU_score += sentence_bleu([reference[i].strip().split()], hypothesis[i].strip().split())

BLEU_score /= len(reference) 
BLEU_score *= 100
print(f"Der BLEU-Score ist:{BLEU_score}")