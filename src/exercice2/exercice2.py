import pandas as pd
#in the data folder we have two csv file, one with all the codes and the other with only the available ones

def calculate_percentage():
    """
    This function calculate the percentage of available codes
    out of all codes.

    We suppose that each code in codes_disponibles are in tous_les_codes.

    :return: percentage of available codes
    """
    #open both csv files 
    Available_Codes=pd.read_csv("data/codes_disponibles.csv",usecols=["codes"])
    All_Codes=pd.read_csv("data/tous_les_codes.csv",usecols=["codes"])

    # the file of available codes contains a lot of duplicate
    # so we need to remove all the duplicate codes
    # then check if each available code is in all codes to calculate the percentage
    
    Available_codes_no_duplicates=Available_Codes["codes"].drop_duplicates()
    AV_size=len(Available_codes_no_duplicates) #Available codes size
    AL_size=len(All_Codes)# All codes size

    #calculate the percentage
    return (AV_size*100)/AL_size

def frequency(code):
    """
    Calculate the frequency of a given available code

    :param code: an available code 
    :return: frequency of code
    """
    # open the available codes csv file

    # count all the occurrences of code in the file

    # divide the number of occurrences of code on all available codes



def main():
    print("The percentage of available codes out of all codes is :",calculate_percentage())

main()