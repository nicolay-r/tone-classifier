mystem = Mystem(entire_input=False)
lemmas = [unicode(w.strip(), 'utf-8') for w in
    self.mystem.lemmatize(' '.join(self.words)) if
    not(w in ['\n', ' ', '\t', '\r'])]
