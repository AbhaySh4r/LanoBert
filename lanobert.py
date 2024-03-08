import numpy as np
from transformers import BertTokenizer, BertForMaskedLM

sentences = [
    "The sky turned a fiery orange as the sun dipped below the horizon, casting long shadows across the tranquil meadow.",
    "Lost in thought, she wandered through the labyrinth of bustling streets, each alleyway revealing a new adventure waiting to unfold.",
    "With a flicker of hesitation, he reached out and grasped the ancient artifact, feeling its power surge through his veins.",
    "Laughter echoed through the halls as friends gathered around the crackling fireplace, swapping stories late into the night.",
    "Time seemed to stand still as they danced beneath the twinkling stars, their hearts beating in perfect harmony.",
    "The aroma of freshly brewed coffee filled the air, awakening her senses with each comforting sip.",
    "Thunder rumbled ominously in the distance, signaling an approaching storm that would soon unleash its fury upon the unsuspecting town.",
    "In the quiet solitude of the forest, she found solace among the towering trees, their gentle whispers soothing her troubled mind.",
    "With a flourish of his pen, he signed his name at the bottom of the contract, sealing the deal with a sense of satisfaction.",
    "As dawn broke over the horizon, painting the sky in hues of pink and gold, she knew that today held endless possibilities waiting to be discovered."
]

N = len(sentences) #length of log file messages

KEY = []
DICT = []

for n in np.arange(0, N):
    str = sentences[n]
    if str not in DICT:
        score_loss, score_prob = [], []
        words = str.split()
        for i in np.arange(0, len(words)):
            temp = words[i]
            words[i] = '[MASK]'
            loss = f'loss{i}'
            prob = f'prob{i}'
            score_loss.append(loss)
            score_prob.append(prob)

            words[i] = temp
        
    else:
        print('else')