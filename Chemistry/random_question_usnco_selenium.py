from selenium import webdriver
import random

subjects = ['Stoichiometry', 'Unit Conversions', 'Solutions', 'Descriptive Chemistry', 'Laboratory Practice', 'States of Matter', 'Intermolecular Forces', 'Unit Cells', 'Kinetic Theory of Gases', 'Thermodynamics', 'Thermodynamic Concepts', 'Thermodynamic Calculations', 'Kinetics', 'Rate Laws', 'Arrhenius Equation', 'Equilibrium', 'Titrations', 'Oxidation-Reduction', 'Oxidation States', 'Atomic Structure', 'Nuclear Chemistry', 'Electrons', 'Periodicity', 'Bonding', 'Lewis Structures', 'Molecular Structure', 'VSEPR', 'Isomerization', 'Organic Chemistry', 'Biochemistry']

def launchRandomPage():
    url = "https://usnco-quizzes.web.app/quiz/{}".format(subjects[random.randint(0, len(subjects) - 1)])
    driver.get(url)

driver = webdriver.Chrome()

while True:
    driver.maximize_window()
    launchRandomPage()

    # when there is only one window, the program does nothing
    while len(driver.window_handles) == 1:
        pass

    driver.quit()
    driver = webdriver.Chrome() # previous window is closed and new one is opened
