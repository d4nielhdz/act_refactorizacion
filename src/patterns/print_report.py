from patterns.csv_utils import Ride

class PrintReport():
    padding = 20

    def create_report(self, data):
        content = self._create_content(data)
        self._create_file(content)


    def _create_content(self, rides):
        builder = [self._create_title("Taxi Report"), self._create_headers()]
        for ride in rides:
            builder.append(self._add_ride(ride))

        return "".join(builder)


    def _create_file(self, content: str):
        with open("financial-report.txt", "w") as file:
            file.write(content)


    def _create_title(self, title: str):
        return f"{title}\n\n"


    def _create_headers(self):
        return f"{self._add_padding('TaxiID')}\t{self._add_padding('Pickup time')}\t{self._add_padding('Dropoff time')}\t{self._add_padding('Passenger count')}\t{self._add_padding('Trip Distance')}\t{self._add_padding('Total amount')}\n"


    def _add_padding(self, txt):
        return f"{txt}".ljust(self.padding)


    def _add_ride(self, ride: Ride):
        return "".join([
            f"{self._add_padding(ride.taxi_id)}\t",
            f"{self._add_padding(ride.pick_up_time.isoformat())}\t",
            f"{self._add_padding(ride.drop_of_time.isoformat())}\t",
            f"{self._add_padding(ride.passenger_count)}\t",
            f"{self._add_padding(ride.trip_distance)}\t",
            f"{self._add_padding(self._format_amount(ride.tolls_amount))}\n",
        ])


    def _format_amount(self, amount):
        if amount < 0:
            return f"({amount})"
        return str(amount)
