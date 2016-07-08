def PMI(term, dv1, dv2):
    t1 = dv1.get_term_in_docs_count_safe(term) + 1
    t2 = dv2.get_term_in_docs_count_safe(term) + 1
    N1 = dv1.get_docs_count()
    N2 = dv2.get_docs_count()
    return log(p(t1, N1 + N2) * float(N1 + N2) /
        (p(t1 + t2, N1 + N2) * p(N1, N1 + N2)), 2)

def p(docs_with_term, total_docs):
    return float(docs_with_term) / total_docs
