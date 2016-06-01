def SO(tv1, dv1, tv2, dv2):
    N = dv1.get_docs_count() + dv2.get_docs_count()
    r1 = {}
    all_terms = merge_two_lists(tv1.get_terms(), tv2.get_terms())
    for term in all_terms:
        r1[to_unicode(term)] = PMI(term, dv1, dv2) - PMI(term, dv2, dv1)
    r1 = sorted(r1.items(), key=operator.itemgetter(1), reverse=True)
    return r1
