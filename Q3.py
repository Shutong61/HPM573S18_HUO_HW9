import PC as P
import MMC as MarkovCls
import SMM as SMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(id=0, therapy=P.Therapies.NO_DRUG)

# simulate the cohort
simOutputs = cohort.simulate()

# print the outcomes of this simulated cohort
SMarkov.print_outcomes(simOutputs, 'No drug:')
