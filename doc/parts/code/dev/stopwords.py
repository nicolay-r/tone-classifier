if (use_stop_words):
    unicode_terms = [t for t in unicode_terms if
        not(t in abs_stop_words) and not(t in stop_words)]
