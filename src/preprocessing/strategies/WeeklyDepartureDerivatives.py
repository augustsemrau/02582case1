import pandas as pd
from preprocessing.strategies import register, Strategy

@register
class WeeklyDepartureDerivatives(Strategy.Strategy):

    def __get_departures_per_week(self, data):
        return data.groupby(['scheduletime year', 'scheduletime week number']).count()

    def __get_first_order_departures(self, weekly_departures):
        return weekly_departures.diff()['airline'].fillna(0).rename('d_departure')

    def __get_second_order_departures(self, weekly_departures):
        return weekly_departures.diff().diff()['airline'].fillna(0).rename('dd_departure')

    def process(self, data):
        data['flightnumber'] = data['flightnumber'].astype(object)

        data = self._split_date_cols(data)

        # Compute new features first and second derivates of departures per week
        departures_per_week = self.__get_departures_per_week(data)
        data = data.join(self.__get_first_order_departures(departures_per_week), 
                            on=['scheduletime year', 'scheduletime week number'], how='left')
        data = data.join(self.__get_second_order_departures(departures_per_week), 
                            on=['scheduletime year', 'scheduletime week number'], how='left')

        data = pd.get_dummies(data)
        data = self._set_response_last(data)

        return data