def save(problem, filepath):
    """
    Save vectors
    """
    with open(filepath, "w") as out:
        print "Vectors count: %s" % (len(problem))
        for vector in problem:
            out.write("%s " % (vector[0]))
            for index, value in sorted(vector[1].iteritems()):
                out.write("%s:%s " % (index, value))
            out.write("\n")
