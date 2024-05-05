import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QListWidget, QListWidgetItem,
    QHBoxLayout, QSpinBox
)

class Concert:
    def __init__(self, name, venue, date, time, capacity):
        self.name = name
        self.venue = venue
        self.date = date
        self.time = time
        self.capacity = capacity
        self.available_tickets = capacity

class TicketBookingSystemGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Konser Bilet Sistemi")
        self.setGeometry(100, 100, 800, 600)

        self.ticket_system = TicketBookingSystem()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.init_ui()

    def init_ui(self):
        self.label_title = QLabel("Konserler", self)
        self.layout.addWidget(self.label_title)

        self.list_widget_concerts = QListWidget(self)
        self.list_widget_concerts.itemClicked.connect(self.display_concert_info)
        self.layout.addWidget(self.list_widget_concerts)

        self.label_quantity = QLabel("Bilet Adedi:", self)
        self.layout.addWidget(self.label_quantity)

        self.spin_box_quantity = QSpinBox(self)
        self.spin_box_quantity.setMinimum(1)
        self.layout.addWidget(self.spin_box_quantity)

        self.button_book = QPushButton("Bilet Al", self)
        self.button_book.clicked.connect(self.book_tickets)
        self.layout.addWidget(self.button_book)

        self.text_edit_info = QLabel(self)
        self.layout.addWidget(self.text_edit_info)

        self.label_concert_info = QLabel(self)
        self.layout.addWidget(self.label_concert_info)

        self.display_concerts()

    def display_concerts(self):
        self.list_widget_concerts.clear()
        for concert in self.ticket_system.concerts:
            item = QListWidgetItem(f"{concert.name} - {concert.date} {concert.time}")
            self.list_widget_concerts.addItem(item)

    def display_concert_info(self, item):
        selected_concert_name = item.text().split(" - ")[0]
        selected_concert = self.ticket_system.get_concert(selected_concert_name)
        if selected_concert:
            self.label_concert_info.setText(
                f"Konser: {selected_concert.name}\n"
                f"Mekan: {selected_concert.venue}\n"
                f"Tarih: {selected_concert.date}\n"
                f"Saat: {selected_concert.time}\n"
                f"Kapasite: {selected_concert.capacity}\n"
                f"Kalan Biletler: {selected_concert.available_tickets}"
            )

    def book_tickets(self):
        selected_item = self.list_widget_concerts.currentItem()
        if selected_item:
            selected_concert_name = selected_item.text().split(" - ")[0]
            quantity = self.spin_box_quantity.value()
            success = self.ticket_system.book_tickets(selected_concert_name, quantity)
            if success:
                self.display_concerts()
                self.text_edit_info.setText("Bilet başarıyla alındı!")
            else:
                self.text_edit_info.setText("Üzgünüz, bilet alınamadı. Kontenjan dolu.")
        else:
            self.text_edit_info.setText("Lütfen bir konser seçin.")

class TicketBookingSystem:
    def __init__(self):
        self.concerts = []
        self.generate_concerts()

    def generate_concerts(self):
        names = ["Rock Fest", "Pop Night", "Jazz Fusion", "Classical Soirée", "Indie Showcase"]
        venues = ["Stadium", "Arena", "Club", "Theater", "Outdoor Amphitheater"]
        dates = ["2024-05-20", "2024-06-15", "2024-07-10", "2024-08-05", "2024-09-20"]
        times = ["18:00", "19:30", "20:00", "21:00", "22:00"]
        capacities = [500, 400, 300, 200, 100]

        for name, venue, date, time, capacity in zip(names, venues, dates, times, capacities):
            self.add_concert(name, venue, date, time, capacity)

    def add_concert(self, name, venue, date, time, capacity):
        concert = Concert(name, venue, date, time, capacity)
        self.concerts.append(concert)

    def get_concert(self, name):
        for concert in self.concerts:
            if concert.name == name:
                return concert
        return None

    def book_tickets(self, concert_name, quantity):
        concert = self.get_concert(concert_name)
        if concert and concert.available_tickets >= quantity:
            concert.available_tickets -= quantity
            return True
        return False

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ticket_booking_system_gui = TicketBookingSystemGUI()
    ticket_booking_system_gui.show()

    sys.exit(app.exec())
