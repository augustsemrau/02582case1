import numpy as np

def forecast_accuracy(loadfactor_forecasted, loadfactor_true, seatcapacity_original):
    '''
    The forecast accuracy is calculated based on the relative difference between the forecasted number of 
    passengers and the actual number of passengers per flight , we will call this the deviation per flight.
 
    :param loadfactor_forecasted:       A vector of size N where N is the number of flights. 
                                        Each entry is the forecasted flight loadfactor.
                                        Such that loadfactor_forecasted[i] = forecasted loadfactor
                                        for flight i.
    :param loadfactor_true:             A vector of size N where N is the number of flights. 
                                        Each entry is the true flight loadfactor.
                                        Such that loadfactor_true[i] = true loadfactor
                                        for flight i.
    :param seatcapacity_original:       A vector of size N where N is the number of flights. 
                                        Each entry is the seat capacity of a given flight.
                                        Such that seatcapacity_original[i] = seat capacity
                                        for flight i.

    :returns:                           A vector of size N with the accuracy per flight: 100% - | Deviation per flight |
    '''
    passengers_true = loadfactor_true * seatcapacity_original
    passengers_forecasted = loadfactor_forecasted * seatcapacity_original
    deviation_per_flight = (passengers_true-passengers_forecasted) / passengers_true
    return 100 - np.abs(deviation_per_flight)

def mean_forecast_accuracy(loadfactor_forecasted, loadfactor_true, seatcapacity_original):
    '''
    The forecast accuracy is calculated based on the relative difference between the forecasted number of 
    passengers and the actual number of passengers per flight , we will call this the deviation per flight.
 
    :param loadfactor_forecasted:       A vector of size N where N is the number of flights. 
                                        Each entry is the forecasted flight loadfactor.
                                        Such that loadfactor_forecasted[i] = forecasted loadfactor
                                        for flight i.
    :param loadfactor_true:             A vector of size N where N is the number of flights. 
                                        Each entry is the true flight loadfactor.
                                        Such that loadfactor_true[i] = true loadfactor
                                        for flight i.
    :param seatcapacity_original:       A vector of size N where N is the number of flights. 
                                        Each entry is the seat capacity of a given flight.
                                        Such that seatcapacity_original[i] = seat capacity
                                        for flight i.

    :returns:                           The total (mean) forecast accuracy: mean(100% - | Deviation per flight |)
    '''
    passengers_true = loadfactor_true * seatcapacity_original
    passengers_forecasted = loadfactor_forecasted * seatcapacity_original
    deviation_per_flight = (passengers_true-passengers_forecasted) / passengers_true
    return np.mean(100 - np.abs(deviation_per_flight))