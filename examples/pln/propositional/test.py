import os
from unittest import TestCase
from opencog.scheme_wrapper import scheme_eval
from opencog.atomspace import TruthValue
from opencog.backwardchainer import BackwardChainer
from opencog.type_constructors import *
from opencog.utilities import initialize_opencog
from opencog.scheme_wrapper import load_scm
import opencog.logger



def init(atomspace):
   initialize_opencog(atomspace)
   scheme_eval(atomspace, '(use-modules (opencog))')
   scheme_eval(atomspace, '(use-modules (opencog exec))')
   scheme_eval(atomspace, '(use-modules (opencog query))')
   scheme_eval(atomspace, '(use-modules (opencog logger))')
   scheme_eval(atomspace, '(use-modules (opencog rule-engine))')
   scheme_eval(atomspace, '(add-to-load-path "{0}")'.format('/home/noskill/projects/opencog/examples/pln/propositional'))


def test():
    atomspace = AtomSpace()

    init(atomspace)
    scheme_eval(atomspace, '(load-from-path "propositional-rule-base-config.scm")')
    # facts:
    P  = PredicateNode("P")
    Q = PredicateNode("Q")
    A = ConceptNode("A")
    B = ConceptNode("B")
    C = ConceptNode("C")
    PA = EvaluationLink(P, A)
    PA.tv = TruthValue(0.5, 0.8)
    PB = EvaluationLink(P, B)
    PB.tv = TruthValue(0.3, 0.9)
    QC = EvaluationLink(Q, C)
    QC.tv = TruthValue(0.9, 0.7)
    proposition = OrLink(AndLink(PA, PB), NotLink(QC))

    rbs = ConceptNode("propositional-rule-base")
    trace_as = AtomSpace()
    chainer = BackwardChainer(atomspace, rbs, proposition, trace_as=trace_as)
    chainer.do_chain()
    results = chainer.get_results()
    traces = chainer.get_inference_trace()
    import pdb;pdb.set_trace()
test()
