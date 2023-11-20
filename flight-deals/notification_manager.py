import smtplib
import html
class NotificationManager:
    def __init__(self):
        self.my_email = "portopapii@gmail.com"
        self.my_password = "scpg eymd zzqm hybc"

    def send_mail(self, flight_data_dict, client_address):

        with smtplib.SMTP("smtp.gmail.com") as connection:
            message = f"Subject: New Flight Deal!\n\n"
            f"Only ${flight_data_dict['Flight Price']} to fly from {flight_data_dict['Departure City']}"
            f"-{flight_data_dict['Departure IATA CODE']} to {flight_data_dict['Arrival City']}"
            f"-{flight_data_dict['Arrival IATA Code']} from {flight_data_dict['Outbound']} to "
            f"{flight_data_dict['Inbound']}"
            if flight_data_dict['stop-over'] == 1:
                message += f"\nFlight has one stop over via {flight_data_dict['via-city']}"
        connection.starttls()
        connection.login(user=self.my_email, password=self.my_password)
        connection.sendmail(
            from_addr=self.my_email,
            to_addrs=client_address,
            msg=html.escape(message)
        )

    def get_mail(self):
        pass
