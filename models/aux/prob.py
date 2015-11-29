#!/usr/bin/python

def save(problem, filepath):
    #save problem
    with open(filepath, "w") as out:
        print "problem vectors: %s"%(len(problem))
        for pv in problem:
            out.write("%s "%(pv[0]))
            for index, value in sorted(pv[1].iteritems()):
                out.write("%s:%s "%(index, value))
            out.write("\n");
