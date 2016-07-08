if (use_tone_prefixes):
    to_remove = [], i = 0
    while i < len(terms)-1:
        bigram = terms[i] + ' ' + terms[i+1]
        if (bigram in prefix) and (i < len(terms)-2):
            terms[i+2] = prefix[bigram] + terms[i+2]
            to_remove.append(i), to_remove.append(i+1), i += 3
        else:
            unigram = terms[i]
            if (unigram in prefix):
                terms[i+1] = prefix[unigram] + terms[i+1]
                to_remove.append(i), i += 2
            else:
                i += 1
