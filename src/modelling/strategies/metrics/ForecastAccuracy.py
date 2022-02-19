import numpy as np

def predict_per_flight(passengers_forecasted, passengers_true):
    '''
    The forecast accuracy is calculated based on the relative difference between the forecasted number of 
    passengers and the actual number of passengers per flight , we will call this the deviation per flight.
 
    :param passengers_forecasted:       A vector of size N where N is the number of flights. 
                                        each entry is the forecasted number of flight passengers.
                                        Such that passengers_forecasted[i] = forecasted number of 
                                        flight passengers for flight i.
    :param passengers_true:             A vector of size N where N is the number of fligts. 
                                        each entry is the true number of flight passengers.
                                        Such that passengers_true[i] = true number of flight passengers 
                                        for flight i.

    :returns:                           A vector of size N with the accuracy per flight: 100% - | Deviation per flight |
    '''

    deviation_per_flight = (passengers_true-passengers_forecasted) / passengers_true
    return 100 - np.abs(deviation_per_flight)

def predict_total(passengers_forecasted, passengers_true):
    '''
    The forecast accuracy is calculated based on the relative difference between the forecasted number of 
    passengers and the actual number of passengers per flight , we will call this the deviation per flight.
 
    :param passengers_forecasted:       A vector of size N where N is the number of flights. 
                                        each entry is the forecasted number of flight passengers.
                                        Such that passengers_forecasted[i] = forecasted number of 
                                        flight passengers for flight i.
    :param passengers_true:             A vector of size N where N is the number of fligts. 
                                        each entry is the true number of flight passengers.
                                        Such that passengers_true[i] = true number of flight passengers 
                                        for flight i.

    :returns:                           The total accuracy: mean(100% - | Deviation per flight |)
    '''

    deviation_per_flight = (passengers_true-passengers_forecasted) / passengers_true
    return np.mean(100 - np.abs(deviation_per_flight))