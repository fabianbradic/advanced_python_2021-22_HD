#
# The first version of our function!
# Write doc strings 
#
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities or tuples
    Intensities are defined as local maxima if the
    intensities of the elements in the list before and after
    are smaller than the peak we want to determine.

    For example given a list:
        [1 5 6 4 1 2 3 2]

    We expect 6 and 3 to be returned.
    

    Args:
        list_of_intensities (list of floats, ints or tuple of ints): a list of
            numeric values

    Returns:
        list of floats or tuples: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)

    """
    maxima_list = []
    
    for step in range(len(list_of_intensities)):

        for value in list_of_intensities:
            if value == None:
                return False


        if (step != 0) & (step != len(list_of_intensities)):
            if list_of_intensities[step-1] < list_of_intensities[step] > list_of_intensities[step+1]:
                maxima_list.append(list_of_intensities[step])

    return maxima_list