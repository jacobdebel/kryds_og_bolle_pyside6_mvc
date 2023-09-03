import sys

from PySide6.QtWidgets import QApplication, QMainWindow

import view_kryds_og_bolle

import model_kryds_og_bolle


class KrydsOgBolleSpil(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = view_kryds_og_bolle.Ui_MainWindow()
        self.ui.setupUi(self)
        self.spillerscorere = {"X": 0, "O": 0}
        self.spillerscorere_labels = {
            "X": self.ui.spiller_x_score,
            "O": self.ui.spiller_o_score,
        }

        self.spil = model_kryds_og_bolle.KrydsOgBolle()
        self.felter = [
            self.ui.knap_0,
            self.ui.knap_1,
            self.ui.knap_2,
            self.ui.knap_3,
            self.ui.knap_4,
            self.ui.knap_5,
            self.ui.knap_6,
            self.ui.knap_7,
            self.ui.knap_8,
        ]
        for felt in self.felter:
            felt.clicked.connect(self.tryk_paa_felt)

        self.ui.actionNyt_spil.triggered.connect(self.nyt_spil)

        self.nyt_spil()

    def tryk_paa_felt(self):
        sender = self.sender()
        indeks = self.felter.index(sender)
        sender.setText(self.spil.spiller)
        sender.setEnabled(False)
        self.spil.saet_plads(indeks, self.spil.spiller)
        vinder = self.spil.tjek_vinder()
        if vinder:
            self.spillerscorere[vinder] += 1
            self.spillerscorere_labels[vinder].setText(
                f"Spiller {vinder}: {self.spillerscorere[vinder]}"
            )
            for felt in self.felter:
                felt.setEnabled(False)
            self.ui.info_label.setText(f"Spiller {self.spil.spiller} vandt!")
        else:
            self.spil.skift_spiller()
            self.ui.info_label.setText(f"Det er spiller {self.spil.spiller}s tur")
            uafgjort = self.spil.er_braettet_fyldt()
            if uafgjort:
                self.ui.info_label.setText("Spillet endte uafgjort.")

    def nyt_spil(self):
        self.spil.nulstil_braet()
        for felt in self.felter:
            felt.setEnabled(True)
            felt.setText("")
        self.ui.info_label.setText(f"Det er spiller {self.spil.spiller}s tur")


program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
kryds_og_bolle_spil = KrydsOgBolleSpil()
kryds_og_bolle_spil.show()
program.exec()
