#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    errors = []
    error_list = []

    for i in range(len(predictions)):
        errors.append(predictions[i] - net_worths[i])
        error_list.append(predictions[i] - net_worths[i])

    count = 0
    error_list.sort()
    while count < (len(predictions)):
        clean = ()
        if errors[count] < error_list[-9]:
            clean = (ages[count], net_worths[count], errors[count])
            cleaned_data.append(clean)
        count += 1
    
    return cleaned_data

