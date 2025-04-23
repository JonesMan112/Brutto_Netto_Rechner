# main.py – Brutto-Netto-Rechner mit PyQt6 (finale Version, exe-kompatibel)

import sys
import os
import argparse
import sqlite3
import csv
from fpdf import FPDF
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QLineEdit, QCheckBox,
    QPushButton, QGridLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
)
from PyQt6.QtGui import QFont
from lst2025 import Lohnsteuer2025


def resource_path(relpath: str) -> str:
    """
    Liefert im EXE-Bundle (PyInstaller --onefile) den temporären Pfad,
    ansonsten das Skript-Verzeichnis.
    """
    if hasattr(sys, "_MEIPASS"):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, relpath)


class NettoRechner(QWidget):
    def __init__(self, args):
        super().__init__()
        self.args = args
        self.lang = args.lang
        title = "Brutto-Netto-Rechner" if self.lang == "de" else "Gross-to-Net Calculator"
        self.setWindowTitle(title)
        self.setFixedSize(800, 400)
        self.verlauf = []
        self.setup_ui()
        self.combo_bundesland.currentIndexChanged.connect(self.update_kassen)
        self.update_kassen()

    def setup_ui(self):
        layout = QGridLayout(self)
        self.setStyleSheet("""
            QWidget { font-family: Segoe UI; font-size: 10.5pt; }
            QLineEdit, QComboBox, QCheckBox, QPushButton, QTableWidget {
                background-color: #ffffff; color: #000000; border: 1px solid #ccc;
            }
            QPushButton:hover { background-color: #e0e0e0; }
            QLabel#error { color: red; }
        """)

        # Brutto-Eingabe
        self.input_brutto = QLineEdit()
        self.input_brutto.setPlaceholderText("z. B. 3000")
        self.input_brutto.textChanged.connect(self.berechne_netto)

        # Bundesland
        self.combo_bundesland = QComboBox()
        self.combo_bundesland.addItems([
            "Baden-Württemberg", "Bayern", "Berlin", "Brandenburg", "Bremen",
            "Hamburg", "Hessen", "Mecklenburg-Vorpommern", "Niedersachsen",
            "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland", "Sachsen",
            "Sachsen-Anhalt", "Schleswig-Holstein", "Thüringen"
        ])
        self.combo_bundesland.currentTextChanged.connect(self.berechne_netto)

        # Steuerklasse
        self.combo_steuerklasse = QComboBox()
        self.combo_steuerklasse.addItems(["1", "2", "3", "4", "5", "6"])
        self.combo_steuerklasse.currentTextChanged.connect(self.berechne_netto)

        # Kirchensteuer
        self.check_kirchensteuer = QCheckBox("Kirchensteuer")
        self.check_kirchensteuer.stateChanged.connect(self.berechne_netto)

        # Krankenkasse
        self.combo_kasse = QComboBox()
        self.combo_kasse.currentTextChanged.connect(self.berechne_netto)

        # Ergebnis & Fehler
        self.label_result = QLabel("Netto: ")
        self.label_result.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))
        self.label_error = QLabel("", objectName="error")

        # Buttons Berechnen & Speichern
        self.btn_berechnen = QPushButton("Berechnen")
        self.btn_berechnen.clicked.connect(self.berechne_netto)
        self.btn_speichern = QPushButton("Speichern")
        self.btn_speichern.clicked.connect(self.berechne_und_speichern)
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_berechnen)
        btn_layout.addWidget(self.btn_speichern)

        # Verlaufstabelle
        self.verlaufstabelle = QTableWidget()
        self.verlaufstabelle.setColumnCount(6)
        self.verlaufstabelle.setHorizontalHeaderLabels(
            ["Brutto", "Bundesland", "SK", "Kirche", "Kasse", "Netto"]
        )
        self.verlaufstabelle.horizontalHeader().setStretchLastSection(True)

        # Export-Buttons
        self.btn_export_pdf = QPushButton("Export als PDF")
        self.btn_export_pdf.clicked.connect(self.export_pdf)
        self.btn_export_csv = QPushButton("Export als CSV")
        self.btn_export_csv.clicked.connect(self.export_csv)
        export_layout = QHBoxLayout()
        export_layout.addWidget(self.btn_export_pdf)
        export_layout.addWidget(self.btn_export_csv)

        # Layout zusammenbauen
        layout.addWidget(QLabel("Bruttogehalt (€):"),    0, 0)
        layout.addWidget(self.input_brutto,              0, 1)
        layout.addWidget(QLabel("Bundesland:"),         1, 0)
        layout.addWidget(self.combo_bundesland,         1, 1)
        layout.addWidget(QLabel("Steuerklasse:"),       2, 0)
        layout.addWidget(self.combo_steuerklasse,       2, 1)
        layout.addWidget(self.check_kirchensteuer,      3, 1)
        layout.addWidget(QLabel("Krankenkasse:"),       4, 0)
        layout.addWidget(self.combo_kasse,              4, 1)
        layout.addLayout(btn_layout,                    5, 0, 1, 2)
        layout.addWidget(self.label_result,             6, 0, 1, 2)
        layout.addWidget(self.label_error,              7, 0, 1, 2)
        layout.addWidget(self.verlaufstabelle,          8, 0, 1, 2)
        layout.addLayout(export_layout,                 9, 0, 1, 2)

    def update_kassen(self):
        bl = self.combo_bundesland.currentText()
        dbfile = resource_path("krankenkassen.db")
        conn = sqlite3.connect(dbfile)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name, beitragssatz FROM krankenkassen "
            "WHERE bundeslaender LIKE ? OR bundeslaender = 'Alle'",
            (f"%{bl}%",)
        )
        self.kassen = {name: satz for name, satz in cursor.fetchall()}
        conn.close()
        self.combo_kasse.clear()
        self.combo_kasse.addItems(self.kassen.keys())

    def berechne_und_speichern(self):
        netto = self.berechne_netto()
        if netto is not None:
            eintrag = (
                self.input_brutto.text(),
                self.combo_bundesland.currentText(),
                self.combo_steuerklasse.currentText(),
                "Ja" if self.check_kirchensteuer.isChecked() else "Nein",
                self.combo_kasse.currentText(),
                f"{netto:.2f} €"
            )
            self.verlauf.append(eintrag)
            self.update_verlaufstabelle()

    def update_verlaufstabelle(self):
        self.verlaufstabelle.setRowCount(len(self.verlauf))
        for i, eintrag in enumerate(self.verlauf):
            for j, wert in enumerate(eintrag):
                self.verlaufstabelle.setItem(i, j, QTableWidgetItem(str(wert)))

    def export_csv(self):
        try:
            with open("netto_verlauf.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Brutto", "Bundesland", "SK", "Kirche", "Kasse", "Netto"])
                writer.writerows(self.verlauf)
            QMessageBox.information(self, "Erfolg", "CSV-Datei wurde gespeichert.")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim CSV-Export: {e}")

    def export_pdf(self):
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, txt="Brutto-Netto-Verlauf", ln=True, align="C")
            pdf.ln(5)
            headers = ["Brutto", "Bundesland", "SK", "Kirche", "Kasse", "Netto"]
            for row in [headers] + self.verlauf:
                pdf.cell(0, 8, txt=" | ".join(row), ln=True)
            pdf.output("netto_verlauf.pdf")
            QMessageBox.information(self, "Erfolg", "PDF wurde gespeichert.")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim PDF-Export: {e}")

    def berechne_netto(self):
        try:
            self.label_error.setText("")
            text = self.input_brutto.text().strip()
            if not text:
                self.label_result.setText("Netto: ")
                return None
            brutto = float(text)
            if brutto <= 0:
                raise ValueError("Bruttogehalt muss > 0 sein")

            # Eingaben
            bundesland   = self.combo_bundesland.currentText()
            steuerklasse = int(self.combo_steuerklasse.currentText())
            kk_satz       = self.kassen[self.combo_kasse.currentText()]
            kirche        = self.check_kirchensteuer.isChecked()

            # Lohnsteuer via PAP
            lst = Lohnsteuer2025()
            lst.setRe4(int(brutto * 100))
            lst.setStkl(steuerklasse)
            lst.setLzz(2)
            lst.setPkv(0)
            lst.setKrv(1)
            lst.setPvs(0)
            lst.setPvz(0)
            lst.setAf(0)
            lst.setF(1)
            lst.setR(0)
            lst.setAlter1(0)
            lst.setLzzhinzu(0)
            lst.MAIN()
            lohnsteuer = float(lst.getLstlzz()) / 100
            soli        = float(lst.getSolzlzz()) / 100

            # Kirchensteuer
            if kirche:
                kst_satz = 0.08 if bundesland in ["Bayern", "Baden-Württemberg"] else 0.09
                kirchensteuer = lohnsteuer * kst_satz
            else:
                kirchensteuer = 0.0

            # Sozialabgaben (AN-Anteile)
            kv_anteil = ((kk_satz - 14.6) / 2) + 7.3
            kv        = brutto * kv_anteil / 100
            pv        = brutto * 0.01525
            rv        = brutto * 0.093
            av        = brutto * 0.012

            # Debug-Ausgabe
            print(f"DEBUG: Brutto        = {brutto:.2f}")
            print(f"DEBUG: Lohnsteuer    = {lohnsteuer:.2f}")
            print(f"DEBUG: Solidaritätsz. = {soli:.2f}")
            print(f"DEBUG: Kirchensteuer = {kirchensteuer:.2f}")
            print(f"DEBUG: KV-Anteil     = {kv_anteil:.3f}% -> {kv:.2f} €")
            print(f"DEBUG: PV            = {pv:.2f}")
            print(f"DEBUG: RV            = {rv:.2f}")
            print(f"DEBUG: AV            = {av:.2f}")

            netto = brutto - (lohnsteuer + soli + kirchensteuer + kv + pv + rv + av)
            self.label_result.setText(f"Netto: {netto:.2f} €")
            return netto

        except Exception as e:
            self.label_error.setText(f"Fehler: {e}")
            return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--theme", choices=["light", "dark"], default="light")
    parser.add_argument("--lang",   choices=["de", "en"],    default="de")
    args = parser.parse_args()

    app = QApplication(sys.argv)
    win = NettoRechner(args)

    if args.theme == "dark":
        app.setStyleSheet("""
            QWidget {
                background-color: #2b2b2b; color: #e0e0e0;
                font-family: Segoe UI; font-size: 10.5pt;
            }
            QLineEdit, QComboBox, QCheckBox, QPushButton, QTableWidget {
                background-color: #3c3f41; color: white; border: 1px solid #555;
            }
            QPushButton:hover { background-color: #505357; }
        """)

    win.show()
    sys.exit(app.exec())
