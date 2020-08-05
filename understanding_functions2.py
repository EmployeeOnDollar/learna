""" First quote out lower line starting with import... .
        Then, run this code and observe the outputs
            Runs the imported function. __name__ is imported script.
            meseeks() is not known
    Then, quote out first line starting with from...
        Run the code twice and observe the outputs
            runs the imported function, changes the built-in variable to understanding_functions script
            imports meseeks() and runs it
        https://www.youtube.com/watch?v=sugvnHA7ElY
    """
# import understanding_functions

from understanding_functions import meseeks


meseeks()
