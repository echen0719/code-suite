import webbrowser
import random

subjects = ['Stoichiometry', 'Unit Conversions', 'Solutions', 'Descriptive Chemistry', 'Laboratory Practice', 'States of Matter', 'Intermolecular Forces', 'Unit Cells', 'Kinetic Theory of Gases', 'Thermodynamics', 'Concepts', 'Calculations', 'Kinetics', 'Rate', 'Laws', 'Arrhenius Equation', 'Equilibrium', 'Titrations', 'Oxidation-Reduction', 'Oxidation States', 'Atomic Structure', 'Nuclear Chemistry', 'Electrons', 'Periodicity', 'Bonding', 'Lewis Structures', 'Molecular', 'Structure', 'VSEPR', 'Isomerization', 'Organic Chemistry', 'Biochemistry']

while True:
	url = "https://usnco-quizzes.web.app/quiz/{}".format(subjects[random.randint(0, len(subjects) - 1)])
	webbrowser.open(url)
	input("Press Enter to move to the next question.")
