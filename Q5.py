import PC as P
import MMC as MarkovCls
import SMM as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTICOAGULATION)

# simulate the cohort
simOutputs = cohort.simulate()

# print the outcomes of this simulated cohort
SupportMarkov.print_outcomes(simOutputs, 'Anticoagulation:')
