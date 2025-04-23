# coding: utf-8

import decimal

class BigDecimal(decimal.Decimal):
    """ Compatibility class for decimal.Decimal """

    ROUND_DOWN = decimal.ROUND_DOWN
    ROUND_UP = decimal.ROUND_UP

    @classmethod
    def _mk_exp(cls, prec):
        return cls('0.' + '0' * prec)

    def divide(self, other, scale=None, rounding=None):
        if not scale and not rounding:
            return BigDecimal(self / other)
        if type(scale) is not int:
            raise ValueError("Expected integer value for scale")
        exp = BigDecimal._mk_exp(scale)
        return BigDecimal((self / other).quantize(exp, rounding=rounding))

    @classmethod
    def valueOf(cls, value):
        return cls(value)

    def multiply(self, other):
        return BigDecimal(self * other)

    def setScale(self, scale, rounding):
        exp = BigDecimal._mk_exp(scale)
        return BigDecimal(self.quantize(exp, rounding=rounding))

    def add(self, other):
        return BigDecimal(self + other)

    def subtract(self, other):
        return BigDecimal(self - other)

    def longValue(self):
        return int(self)

    def compareTo(self, other):
        return BigDecimal(self.compare(other))

BigDecimal.ZERO = BigDecimal(0)
BigDecimal.ONE = BigDecimal(1)
BigDecimal.TEN = BigDecimal(10)


class Lohnsteuer2025:
    TAB1 = [BigDecimal.valueOf(0), BigDecimal.valueOf(0.4), BigDecimal.valueOf(0.384), BigDecimal.valueOf(0.368), BigDecimal.valueOf(0.352), BigDecimal.valueOf(0.336), BigDecimal.valueOf(0.32), BigDecimal.valueOf(0.304), BigDecimal.valueOf(0.288), BigDecimal.valueOf(0.272), BigDecimal.valueOf(0.256), BigDecimal.valueOf(0.24), BigDecimal.valueOf(0.224), BigDecimal.valueOf(0.208), BigDecimal.valueOf(0.192), BigDecimal.valueOf(0.176), BigDecimal.valueOf(0.16), BigDecimal.valueOf(0.152), BigDecimal.valueOf(0.144), BigDecimal.valueOf(0.14), BigDecimal.valueOf(0.136), BigDecimal.valueOf(0.132), BigDecimal.valueOf(0.128), BigDecimal.valueOf(0.124), BigDecimal.valueOf(0.12), BigDecimal.valueOf(0.116), BigDecimal.valueOf(0.112), BigDecimal.valueOf(0.108), BigDecimal.valueOf(0.104), BigDecimal.valueOf(0.1), BigDecimal.valueOf(0.096), BigDecimal.valueOf(0.092), BigDecimal.valueOf(0.088), BigDecimal.valueOf(0.084), BigDecimal.valueOf(0.08), BigDecimal.valueOf(0.076), BigDecimal.valueOf(0.072), BigDecimal.valueOf(0.068), BigDecimal.valueOf(0.064), BigDecimal.valueOf(0.06), BigDecimal.valueOf(0.056), BigDecimal.valueOf(0.052), BigDecimal.valueOf(0.048), BigDecimal.valueOf(0.044), BigDecimal.valueOf(0.04), BigDecimal.valueOf(0.036), BigDecimal.valueOf(0.032), BigDecimal.valueOf(0.028), BigDecimal.valueOf(0.024), BigDecimal.valueOf(0.02), BigDecimal.valueOf(0.016), BigDecimal.valueOf(0.012), BigDecimal.valueOf(0.008), BigDecimal.valueOf(0.004), BigDecimal.valueOf(0)]
    """
    geändert für 2025
    """

    TAB2 = [BigDecimal.valueOf(0), BigDecimal.valueOf(3000), BigDecimal.valueOf(2880), BigDecimal.valueOf(2760), BigDecimal.valueOf(2640), BigDecimal.valueOf(2520), BigDecimal.valueOf(2400), BigDecimal.valueOf(2280), BigDecimal.valueOf(2160), BigDecimal.valueOf(2040), BigDecimal.valueOf(1920), BigDecimal.valueOf(1800), BigDecimal.valueOf(1680), BigDecimal.valueOf(1560), BigDecimal.valueOf(1440), BigDecimal.valueOf(1320), BigDecimal.valueOf(1200), BigDecimal.valueOf(1140), BigDecimal.valueOf(1080), BigDecimal.valueOf(1050), BigDecimal.valueOf(1020), BigDecimal.valueOf(990), BigDecimal.valueOf(960), BigDecimal.valueOf(930), BigDecimal.valueOf(900), BigDecimal.valueOf(870), BigDecimal.valueOf(840), BigDecimal.valueOf(810), BigDecimal.valueOf(780), BigDecimal.valueOf(750), BigDecimal.valueOf(720), BigDecimal.valueOf(690), BigDecimal.valueOf(660), BigDecimal.valueOf(630), BigDecimal.valueOf(600), BigDecimal.valueOf(570), BigDecimal.valueOf(540), BigDecimal.valueOf(510), BigDecimal.valueOf(480), BigDecimal.valueOf(450), BigDecimal.valueOf(420), BigDecimal.valueOf(390), BigDecimal.valueOf(360), BigDecimal.valueOf(330), BigDecimal.valueOf(300), BigDecimal.valueOf(270), BigDecimal.valueOf(240), BigDecimal.valueOf(210), BigDecimal.valueOf(180), BigDecimal.valueOf(150), BigDecimal.valueOf(120), BigDecimal.valueOf(90), BigDecimal.valueOf(60), BigDecimal.valueOf(30), BigDecimal.valueOf(0)]
    """
    geändert für 2025
    """

    TAB3 = [BigDecimal.valueOf(0), BigDecimal.valueOf(900), BigDecimal.valueOf(864), BigDecimal.valueOf(828), BigDecimal.valueOf(792), BigDecimal.valueOf(756), BigDecimal.valueOf(720), BigDecimal.valueOf(684), BigDecimal.valueOf(648), BigDecimal.valueOf(612), BigDecimal.valueOf(576), BigDecimal.valueOf(540), BigDecimal.valueOf(504), BigDecimal.valueOf(468), BigDecimal.valueOf(432), BigDecimal.valueOf(396), BigDecimal.valueOf(360), BigDecimal.valueOf(342), BigDecimal.valueOf(324), BigDecimal.valueOf(315), BigDecimal.valueOf(306), BigDecimal.valueOf(297), BigDecimal.valueOf(288), BigDecimal.valueOf(279), BigDecimal.valueOf(270), BigDecimal.valueOf(261), BigDecimal.valueOf(252), BigDecimal.valueOf(243), BigDecimal.valueOf(234), BigDecimal.valueOf(225), BigDecimal.valueOf(216), BigDecimal.valueOf(207), BigDecimal.valueOf(198), BigDecimal.valueOf(189), BigDecimal.valueOf(180), BigDecimal.valueOf(171), BigDecimal.valueOf(162), BigDecimal.valueOf(153), BigDecimal.valueOf(144), BigDecimal.valueOf(135), BigDecimal.valueOf(126), BigDecimal.valueOf(117), BigDecimal.valueOf(108), BigDecimal.valueOf(99), BigDecimal.valueOf(90), BigDecimal.valueOf(81), BigDecimal.valueOf(72), BigDecimal.valueOf(63), BigDecimal.valueOf(54), BigDecimal.valueOf(45), BigDecimal.valueOf(36), BigDecimal.valueOf(27), BigDecimal.valueOf(18), BigDecimal.valueOf(9), BigDecimal.valueOf(0)]
    """
    geändert für 2025
    """

    TAB4 = [BigDecimal.valueOf(0), BigDecimal.valueOf(0.4), BigDecimal.valueOf(0.384), BigDecimal.valueOf(0.368), BigDecimal.valueOf(0.352), BigDecimal.valueOf(0.336), BigDecimal.valueOf(0.32), BigDecimal.valueOf(0.304), BigDecimal.valueOf(0.288), BigDecimal.valueOf(0.272), BigDecimal.valueOf(0.256), BigDecimal.valueOf(0.24), BigDecimal.valueOf(0.224), BigDecimal.valueOf(0.208), BigDecimal.valueOf(0.192), BigDecimal.valueOf(0.176), BigDecimal.valueOf(0.16), BigDecimal.valueOf(0.152), BigDecimal.valueOf(0.144), BigDecimal.valueOf(0.14), BigDecimal.valueOf(0.136), BigDecimal.valueOf(0.132), BigDecimal.valueOf(0.128), BigDecimal.valueOf(0.124), BigDecimal.valueOf(0.12), BigDecimal.valueOf(0.116), BigDecimal.valueOf(0.112), BigDecimal.valueOf(0.108), BigDecimal.valueOf(0.104), BigDecimal.valueOf(0.1), BigDecimal.valueOf(0.096), BigDecimal.valueOf(0.092), BigDecimal.valueOf(0.088), BigDecimal.valueOf(0.084), BigDecimal.valueOf(0.08), BigDecimal.valueOf(0.076), BigDecimal.valueOf(0.072), BigDecimal.valueOf(0.068), BigDecimal.valueOf(0.064), BigDecimal.valueOf(0.06), BigDecimal.valueOf(0.056), BigDecimal.valueOf(0.052), BigDecimal.valueOf(0.048), BigDecimal.valueOf(0.044), BigDecimal.valueOf(0.04), BigDecimal.valueOf(0.036), BigDecimal.valueOf(0.032), BigDecimal.valueOf(0.028), BigDecimal.valueOf(0.024), BigDecimal.valueOf(0.02), BigDecimal.valueOf(0.016), BigDecimal.valueOf(0.012), BigDecimal.valueOf(0.008), BigDecimal.valueOf(0.004), BigDecimal.valueOf(0)]
    """
    geändert für 2025
    """

    TAB5 = [BigDecimal.valueOf(0), BigDecimal.valueOf(1900), BigDecimal.valueOf(1824), BigDecimal.valueOf(1748), BigDecimal.valueOf(1672), BigDecimal.valueOf(1596), BigDecimal.valueOf(1520), BigDecimal.valueOf(1444), BigDecimal.valueOf(1368), BigDecimal.valueOf(1292), BigDecimal.valueOf(1216), BigDecimal.valueOf(1140), BigDecimal.valueOf(1064), BigDecimal.valueOf(988), BigDecimal.valueOf(912), BigDecimal.valueOf(836), BigDecimal.valueOf(760), BigDecimal.valueOf(722), BigDecimal.valueOf(684), BigDecimal.valueOf(665), BigDecimal.valueOf(646), BigDecimal.valueOf(627), BigDecimal.valueOf(608), BigDecimal.valueOf(589), BigDecimal.valueOf(570), BigDecimal.valueOf(551), BigDecimal.valueOf(532), BigDecimal.valueOf(513), BigDecimal.valueOf(494), BigDecimal.valueOf(475), BigDecimal.valueOf(456), BigDecimal.valueOf(437), BigDecimal.valueOf(418), BigDecimal.valueOf(399), BigDecimal.valueOf(380), BigDecimal.valueOf(361), BigDecimal.valueOf(342), BigDecimal.valueOf(323), BigDecimal.valueOf(304), BigDecimal.valueOf(285), BigDecimal.valueOf(266), BigDecimal.valueOf(247), BigDecimal.valueOf(228), BigDecimal.valueOf(209), BigDecimal.valueOf(190), BigDecimal.valueOf(171), BigDecimal.valueOf(152), BigDecimal.valueOf(133), BigDecimal.valueOf(114), BigDecimal.valueOf(95), BigDecimal.valueOf(76), BigDecimal.valueOf(57), BigDecimal.valueOf(38), BigDecimal.valueOf(19), BigDecimal.valueOf(0)]
    """
    geändert für 2025
    """

    ZAHL1 = BigDecimal.ONE
    """
    Zahlenkonstanten fuer im Plan oft genutzte BigDecimal Werte
    """

    ZAHL2 = BigDecimal(2)
    ZAHL5 = BigDecimal(5)
    ZAHL7 = BigDecimal(7)
    ZAHL12 = BigDecimal(12)
    ZAHL100 = BigDecimal(100)
    ZAHL360 = BigDecimal(360)
    ZAHL500 = BigDecimal(500)
    ZAHL700 = BigDecimal(700)
    ZAHL1000 = BigDecimal(1000)
    ZAHL10000 = BigDecimal(10000)

    def __init__(self, **kwargs):
        # input variables

        # 1, wenn die Anwendung des Faktorverfahrens gewählt wurden (nur in Steuerklasse IV)
        self.af = 1
        if "af" in kwargs:
            self.setAf(kwargs["af"])

        # Auf die Vollendung des 64. Lebensjahres folgende
        # Kalenderjahr (erforderlich, wenn ALTER1=1)
        self.AJAHR = 0
        if "AJAHR" in kwargs:
            self.setAjahr(kwargs["AJAHR"])

        # 1, wenn das 64. Lebensjahr zu Beginn des Kalenderjahres vollendet wurde, in dem
        # der Lohnzahlungszeitraum endet (§ 24 a EStG), sonst = 0
        self.ALTER1 = 0
        if "ALTER1" in kwargs:
            self.setAlter1(kwargs["ALTER1"])

        # eingetragener Faktor mit drei Nachkommastellen
        self.f = 1.0
        if "f" in kwargs:
            self.setF(kwargs["f"])

        # Jahresfreibetrag für die Ermittlung der Lohnsteuer für die sonstigen Bezüge
        # sowie für Vermögensbeteiligungen nach § 19a Absatz 1 und 4 EStG nach Maßgabe der
        # elektronischen Lohnsteuerabzugsmerkmale nach § 39e EStG oder der Eintragung
        # auf der Bescheinigung für den Lohnsteuerabzug 2025 in Cent (ggf. 0)
        self.JFREIB = BigDecimal(0)
        if "JFREIB" in kwargs:
            self.setJfreib(kwargs["JFREIB"])

        # Jahreshinzurechnungsbetrag für die Ermittlung der Lohnsteuer für die sonstigen Bezüge
        # sowie für Vermögensbeteiligungen nach § 19a Absatz 1 und 4 EStG nach Maßgabe der
        # elektronischen Lohnsteuerabzugsmerkmale nach § 39e EStG oder der Eintragung auf der
        # Bescheinigung für den Lohnsteuerabzug 2025 in Cent (ggf. 0)
        self.JHINZU = BigDecimal(0)
        if "JHINZU" in kwargs:
            self.setJhinzu(kwargs["JHINZU"])

        # Voraussichtlicher Jahresarbeitslohn ohne sonstige Bezüge (d.h. auch ohne
        # die zu besteuernden Vorteile bei Vermögensbeteiligungen,
        # § 19a Absatz 4 EStG) in Cent.
        # Anmerkung: Die Eingabe dieses Feldes (ggf. 0) ist erforderlich bei Eingaben zu sonstigen
        # Bezügen (Feld SONSTB).
        # Sind in einem vorangegangenen Abrechnungszeitraum bereits sonstige Bezüge gezahlt worden,
        # so sind sie dem voraussichtlichen Jahresarbeitslohn hinzuzurechnen. Gleiches gilt für zu
        # besteuernde Vorteile bei Vermögensbeteiligungen (§ 19a Absatz 4 EStG).
        self.JRE4 = BigDecimal(0)
        if "JRE4" in kwargs:
            self.setJre4(kwargs["JRE4"])

        # In JRE4 enthaltene Entschädigungen nach § 24 Nummer 1 EStG und zu besteuernde
        # Vorteile bei Vermögensbeteiligungen (§ 19a Absatz 4 EStG in Cent
        self.JRE4ENT = BigDecimal.ZERO
        if "JRE4ENT" in kwargs:
            self.setJre4ent(kwargs["JRE4ENT"])

        # In JRE4 enthaltene Versorgungsbezuege in Cents (ggf. 0)
        self.JVBEZ = BigDecimal(0)
        if "JVBEZ" in kwargs:
            self.setJvbez(kwargs["JVBEZ"])

        # Merker für die Vorsorgepauschale
        # 0 = der Arbeitnehmer ist in der gesetzlichen Rentenversicherung oder einer
        # berufsständischen Versorgungseinrichtung pflichtversichert oder bei Befreiung von der
        # Versicherungspflicht freiwillig versichert; es gilt die allgemeine Beitragsbemessungsgrenze
        # 
        # 1 = wenn nicht 0
        # 
        self.KRV = 0
        if "KRV" in kwargs:
            self.setKrv(kwargs["KRV"])

        # Kassenindividueller Zusatzbeitragssatz bei einem gesetzlich krankenversicherten Arbeitnehmer
        # in Prozent (bspw. 2,50 für 2,50 %) mit 2 Dezimalstellen.
        # Es ist der volle Zusatzbeitragssatz anzugeben. Die Aufteilung in Arbeitnehmer- und Arbeitgeber-
        # anteil erfolgt im Programmablauf.
        self.KVZ = BigDecimal(0)
        if "KVZ" in kwargs:
            self.setKvz(kwargs["KVZ"])

        # Lohnzahlungszeitraum:
        # 1 = Jahr
        # 2 = Monat
        # 3 = Woche
        # 4 = Tag
        self.LZZ = 0
        if "LZZ" in kwargs:
            self.setLzz(kwargs["LZZ"])

        # Der als elektronisches Lohnsteuerabzugsmerkmal für den Arbeitgeber nach § 39e EStG festgestellte
        # oder in der Bescheinigung für den Lohnsteuerabzug 2025 eingetragene Freibetrag für den
        # Lohnzahlungszeitraum in Cent
        self.LZZFREIB = BigDecimal(0)
        if "LZZFREIB" in kwargs:
            self.setLzzfreib(kwargs["LZZFREIB"])

        # Der als elektronisches Lohnsteuerabzugsmerkmal für den Arbeitgeber nach § 39e EStG festgestellte
        # oder in der Bescheinigung für den Lohnsteuerabzug 2025 eingetragene Hinzurechnungsbetrag für den
        # Lohnzahlungszeitraum in Cent
        self.LZZHINZU = BigDecimal(0)
        if "LZZHINZU" in kwargs:
            self.setLzzhinzu(kwargs["LZZHINZU"])

        # Nicht zu besteuernde Vorteile bei Vermögensbeteiligungen
        # (§ 19a Absatz 1 Satz 4 EStG) in Cent
        self.MBV = BigDecimal(0)
        if "MBV" in kwargs:
            self.setMbv(kwargs["MBV"])

        # Dem Arbeitgeber mitgeteilte Zahlungen des Arbeitnehmers zur privaten
        # Kranken- bzw. Pflegeversicherung im Sinne des §10 Abs. 1 Nr. 3 EStG 2010
        # als Monatsbetrag in Cent (der Wert ist inabhängig vom Lohnzahlungszeitraum immer
        # als Monatsbetrag anzugeben).
        self.PKPV = BigDecimal(0)
        if "PKPV" in kwargs:
            self.setPkpv(kwargs["PKPV"])

        # Krankenversicherung:
        # 0 = gesetzlich krankenversicherte Arbeitnehmer
        # 1 = ausschließlich privat krankenversicherte Arbeitnehmer OHNE Arbeitgeberzuschuss
        # 2 = ausschließlich privat krankenversicherte Arbeitnehmer MIT Arbeitgeberzuschuss
        self.PKV = 0
        if "PKV" in kwargs:
            self.setPkv(kwargs["PKV"])

        # Zahl der beim Arbeitnehmer zu berücksichtigenden Beitragsabschläge in der sozialen Pflegeversicherung
        # bei mehr als einem Kind
        # 0 = kein Abschlag
        # 1 = Beitragsabschlag für das 2. Kind
        # 2 = Beitragsabschläge für das 2. und 3. Kind
        # 3 = Beitragsabschläge für 2. bis 4. Kinder
        # 4 = Beitragsabschläge für 2. bis 5. oder mehr Kinder
        self.PVA = BigDecimal(0)
        if "PVA" in kwargs:
            self.setPva(kwargs["PVA"])

        # 1, wenn bei der sozialen Pflegeversicherung die Besonderheiten in Sachsen zu berücksichtigen sind bzw.
        # zu berücksichtigen wären, sonst 0.
        self.PVS = 0
        if "PVS" in kwargs:
            self.setPvs(kwargs["PVS"])

        # 1, wenn er der Arbeitnehmer den Zuschlag zur sozialen Pflegeversicherung
        # zu zahlen hat, sonst 0.
        self.PVZ = 0
        if "PVZ" in kwargs:
            self.setPvz(kwargs["PVZ"])

        # Religionsgemeinschaft des Arbeitnehmers lt. elektronischer Lohnsteuerabzugsmerkmale oder der
        # Bescheinigung für den Lohnsteuerabzug 2025 (bei keiner Religionszugehörigkeit = 0)
        self.R = 0
        if "R" in kwargs:
            self.setR(kwargs["R"])

        # Steuerpflichtiger Arbeitslohn für den Lohnzahlungszeitraum vor Berücksichtigung des
        # Versorgungsfreibetrags und des Zuschlags zum Versorgungsfreibetrag, des Altersentlastungsbetrags
        # und des als elektronisches Lohnsteuerabzugsmerkmal festgestellten oder in der Bescheinigung für
        # den Lohnsteuerabzug 2025 für den Lohnzahlungszeitraum eingetragenen Freibetrags bzw.
        # Hinzurechnungsbetrags in Cent
        self.RE4 = BigDecimal(0)
        if "RE4" in kwargs:
            self.setRe4(kwargs["RE4"])

        # Sonstige Bezüge einschließlich zu besteuernde Vorteile bei Vermögensbeteiligungen und Sterbegeld bei Versorgungsbezügen sowie
        # Kapitalauszahlungen/Abfindungen, in Cent (ggf. 0)
        self.SONSTB = BigDecimal(0)
        if "SONSTB" in kwargs:
            self.setSonstb(kwargs["SONSTB"])

        # In SONSTB enthaltene Entschädigungen nach § 24 Nummer 1 EStG
        self.SONSTENT = BigDecimal.ZERO
        if "SONSTENT" in kwargs:
            self.setSonstent(kwargs["SONSTENT"])

        # Sterbegeld bei Versorgungsbezuegen sowie Kapitalauszahlungen/Abfindungen,
        # (in SONSTB enthalten) in Cent
        self.STERBE = BigDecimal(0)
        if "STERBE" in kwargs:
            self.setSterbe(kwargs["STERBE"])

        # Steuerklasse:
        # 1 = I
        # 2 = II
        # 3 = III
        # 4 = IV
        # 5 = V
        # 6 = VI
        self.STKL = 0
        if "STKL" in kwargs:
            self.setStkl(kwargs["STKL"])

        # In RE4 enthaltene Versorgungsbezuege in Cents (ggf. 0)
        self.VBEZ = BigDecimal(0)
        if "VBEZ" in kwargs:
            self.setVbez(kwargs["VBEZ"])

        # Vorsorgungsbezug im Januar 2005 bzw. fuer den ersten vollen Monat
        # in Cents
        self.VBEZM = BigDecimal(0)
        if "VBEZM" in kwargs:
            self.setVbezm(kwargs["VBEZM"])

        # Voraussichtliche Sonderzahlungen im Kalenderjahr des Versorgungsbeginns
        # bei Versorgungsempfaengern ohne Sterbegeld, Kapitalauszahlungen/Abfindungen
        # bei Versorgungsbezuegen in Cents
        self.VBEZS = BigDecimal(0)
        if "VBEZS" in kwargs:
            self.setVbezs(kwargs["VBEZS"])

        # In SONSTB enthaltene Versorgungsbezuege einschliesslich Sterbegeld
        # in Cents (ggf. 0)
        self.VBS = BigDecimal(0)
        if "VBS" in kwargs:
            self.setVbs(kwargs["VBS"])

        # Jahr, in dem der Versorgungsbezug erstmalig gewaehrt wurde; werden
        # mehrere Versorgungsbezuege gezahlt, so gilt der aelteste erstmalige Bezug
        self.VJAHR = 0
        if "VJAHR" in kwargs:
            self.setVjahr(kwargs["VJAHR"])

        # Zahl der Freibetraege fuer Kinder (eine Dezimalstelle, nur bei Steuerklassen
        # I, II, III und IV)
        self.ZKF = BigDecimal(0)
        if "ZKF" in kwargs:
            self.setZkf(kwargs["ZKF"])

        # Zahl der Monate, fuer die Versorgungsbezuege gezahlt werden (nur
        # erforderlich bei Jahresberechnung (LZZ = 1)
        self.ZMVB = 0
        if "ZMVB" in kwargs:
            self.setZmvb(kwargs["ZMVB"])

        # output variables

        # Bemessungsgrundlage fuer die Kirchenlohnsteuer in Cents
        self.BK = BigDecimal(0)

        # Bemessungsgrundlage der sonstigen Bezüge  für die Kirchenlohnsteuer in Cent.
        # Hinweis: Negativbeträge, die aus nicht zu besteuernden Vorteilen bei
        # Vermögensbeteiligungen (§ 19a Absatz 1 Satz 4 EStG) resultieren, mindern BK
        # (maximal bis 0). Der Sonderausgabenabzug für tatsächlich erbrachte Vorsorgeaufwendungen
        # im Rahmen der Veranlagung zur Einkommensteuer bleibt unberührt.
        self.BKS = BigDecimal(0)

        # Fuer den Lohnzahlungszeitraum einzubehaltende Lohnsteuer in Cents
        self.LSTLZZ = BigDecimal(0)

        # Fuer den Lohnzahlungszeitraum einzubehaltender Solidaritaetszuschlag
        # in Cents
        self.SOLZLZZ = BigDecimal(0)

        # Solidaritätszuschlag für sonstige Bezüge (ohne Vergütung für mehrjährige Tätigkeit in Cent.
        # Hinweis: Negativbeträge, die aus nicht zu besteuernden Vorteilen bei Vermögensbeteiligungen
        # (§ 19a Absatz 1 Satz 4 EStG) resultieren, mindern SOLZLZZ (maximal bis 0). Der
        # Sonderausgabenabzug für tatsächlich erbrachte Vorsorgeaufwendungen im Rahmen der
        # Veranlagung zur Einkommensteuer bleibt unberührt.
        self.SOLZS = BigDecimal(0)

        # Lohnsteuer für sonstige Bezüge in Cent
        # Hinweis: Negativbeträge, die aus nicht zu besteuernden Vorteilen bei Vermögensbeteiligungen
        # (§ 19a Absatz 1 Satz 4 EStG) resultieren, mindern LSTLZZ (maximal bis 0). Der
        # Sonderausgabenabzug für tatsächlich erbrachte Vorsorgeaufwendungen im Rahmen der
        # Veranlagung zur Einkommensteuer bleibt unberührt.
        self.STS = BigDecimal(0)

        # Für den Lohnzahlungszeitraum berücksichtigte Beiträge des Arbeitnehmers zur
        # privaten Basis-Krankenversicherung und privaten Pflege-Pflichtversicherung (ggf. auch
        # die Mindestvorsorgepauschale) in Cent beim laufenden Arbeitslohn. Für Zwecke der Lohn-
        # steuerbescheinigung sind die einzelnen Ausgabewerte außerhalb des eigentlichen Lohn-
        # steuerbescheinigungsprogramms zu addieren; hinzuzurechnen sind auch die Ausgabewerte
        # VKVSONST
        self.VKVLZZ = BigDecimal(0)

        # Für den Lohnzahlungszeitraum berücksichtigte Beiträge des Arbeitnehmers
        # zur privaten Basis-Krankenversicherung und privaten Pflege-Pflichtversicherung (ggf.
        # auch die Mindestvorsorgepauschale) in Cent bei sonstigen Bezügen. Der Ausgabewert kann
        # auch negativ sein.
        self.VKVSONST = BigDecimal(0)

        # Verbrauchter Freibetrag bei Berechnung des laufenden Arbeitslohns, in Cent
        self.VFRB = BigDecimal(0)

        # Verbrauchter Freibetrag bei Berechnung des voraussichtlichen Jahresarbeitslohns, in Cent
        self.VFRBS1 = BigDecimal(0)

        # Verbrauchter Freibetrag bei Berechnung der sonstigen Bezüge, in Cent
        self.VFRBS2 = BigDecimal(0)

        # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach dem DBA Türkei verfügbares ZVE über
        # dem Grundfreibetrag bei der Berechnung des laufenden Arbeitslohns, in Cent
        self.WVFRB = BigDecimal(0)

        # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach dem DBA Türkei verfügbares ZVE über dem Grundfreibetrag
        # bei der Berechnung des voraussichtlichen Jahresarbeitslohns, in Cent
        self.WVFRBO = BigDecimal(0)

        # Für die weitergehende Berücksichtigung des Steuerfreibetrags nach dem DBA Türkei verfügbares ZVE
        # über dem Grundfreibetrag bei der Berechnung der sonstigen Bezüge, in Cent
        self.WVFRBM = BigDecimal(0)

        # internal variables

        # Altersentlastungsbetrag nach Alterseinkünftegesetz in €,
        # Cent (2 Dezimalstellen)
        self.ALTE = BigDecimal(0)

        # Arbeitnehmer-Pauschbetrag in EURO
        self.ANP = BigDecimal(0)

        # Auf den Lohnzahlungszeitraum entfallender Anteil von Jahreswerten
        # auf ganze Cents abgerundet
        self.ANTEIL1 = BigDecimal(0)

        # Bemessungsgrundlage für Altersentlastungsbetrag in €, Cent
        # (2 Dezimalstellen)
        self.BMG = BigDecimal(0)

        # Beitragsbemessungsgrenze in der gesetzlichen Krankenversicherung
        # und der sozialen Pflegeversicherung in Euro
        self.BBGKVPV = BigDecimal(0)

        # allgemeine Beitragsbemessungsgrenze in der allgemeinen Renten-versicherung in Euro
        self.BBGRV = BigDecimal(0)

        # Differenz zwischen ST1 und ST2 in EURO
        self.DIFF = BigDecimal(0)

        # Entlastungsbetrag für Alleinerziehende in Euro
        self.EFA = BigDecimal(0)

        # Versorgungsfreibetrag in €, Cent (2 Dezimalstellen)
        self.FVB = BigDecimal(0)

        # Versorgungsfreibetrag in €, Cent (2 Dezimalstellen) für die Berechnung
        # der Lohnsteuer für den sonstigen Bezug
        self.FVBSO = BigDecimal(0)

        # Zuschlag zum Versorgungsfreibetrag in EURO
        self.FVBZ = BigDecimal(0)

        # Zuschlag zum Versorgungsfreibetrag in EURO fuer die Berechnung
        # der Lohnsteuer beim sonstigen Bezug
        self.FVBZSO = BigDecimal(0)

        # Grundfreibetrag in Euro
        self.GFB = BigDecimal(0)

        # Maximaler Altersentlastungsbetrag in €
        self.HBALTE = BigDecimal(0)

        # Maßgeblicher maximaler Versorgungsfreibetrag in Euro, Cent (2 Dezimalstellen)
        self.HFVB = BigDecimal(0)

        # Massgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in €,Cent
        # (2 Dezimalstellen)
        self.HFVBZ = BigDecimal(0)

        # Massgeblicher maximaler Zuschlag zum Versorgungsfreibetrag in €, Cent
        # (2 Dezimalstellen) für die Berechnung der Lohnsteuer für den
        # sonstigen Bezug
        self.HFVBZSO = BigDecimal(0)

        # Zwischenfeld zu X fuer die Berechnung der Steuer nach § 39b
        # Abs. 2 Satz 7 EStG in €
        self.HOCH = BigDecimal(0)

        # Nummer der Tabellenwerte fuer Versorgungsparameter
        self.J = 0

        # Jahressteuer nach § 51a EStG, aus der Solidaritaetszuschlag und
        # Bemessungsgrundlage fuer die Kirchenlohnsteuer ermittelt werden in EURO
        self.JBMG = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechneter LZZFREIB in €, Cent
        # (2 Dezimalstellen)
        self.JLFREIB = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnete LZZHINZU in €, Cent
        # (2 Dezimalstellen)
        self.JLHINZU = BigDecimal(0)

        # Jahreswert, dessen Anteil fuer einen Lohnzahlungszeitraum in
        # UPANTEIL errechnet werden soll in Cents
        self.JW = BigDecimal(0)

        # Nummer der Tabellenwerte fuer Parameter bei Altersentlastungsbetrag
        self.K = 0

        # Summe der Freibetraege fuer Kinder in EURO
        self.KFB = BigDecimal(0)

        # Beitragssatz des Arbeitgebers zur Krankenversicherung
        self.KVSATZAG = BigDecimal(0)

        # Beitragssatz des Arbeitnehmers zur Krankenversicherung
        self.KVSATZAN = BigDecimal(0)

        # Kennzahl fuer die Einkommensteuer-Tabellenart:
        # 1 = Grundtabelle
        # 2 = Splittingtabelle
        self.KZTAB = 0

        # Jahreslohnsteuer in EURO
        self.LSTJAHR = BigDecimal(0)

        # Zwischenfelder der Jahreslohnsteuer in Cent
        self.LSTOSO = BigDecimal(0)
        self.LSTSO = BigDecimal(0)

        # Mindeststeuer fuer die Steuerklassen V und VI in EURO
        self.MIST = BigDecimal(0)

        # Beitragssatz des Arbeitgebers zur Pflegeversicherung (6 Dezimalstellen)
        self.PVSATZAG = BigDecimal(0)

        # Beitragssatz des Arbeitnehmers zur Pflegeversicherung (6 Dezimalstellen)
        self.PVSATZAN = BigDecimal(0)

        # Beitragssatz des Arbeitnehmers in der allgemeinen gesetzlichen Rentenversicherung (4 Dezimalstellen)
        self.RVSATZAN = BigDecimal(0)

        # Rechenwert in Gleitkommadarstellung
        self.RW = BigDecimal(0)

        # Sonderausgaben-Pauschbetrag in EURO
        self.SAP = BigDecimal(0)

        # Freigrenze fuer den Solidaritaetszuschlag in EURO
        self.SOLZFREI = BigDecimal(0)

        # Solidaritaetszuschlag auf die Jahreslohnsteuer in EURO, C (2 Dezimalstellen)
        self.SOLZJ = BigDecimal(0)

        # Zwischenwert fuer den Solidaritaetszuschlag auf die Jahreslohnsteuer
        # in EURO, C (2 Dezimalstellen)
        self.SOLZMIN = BigDecimal(0)

        # Bemessungsgrundlage des Solidaritätszuschlags zur Prüfung der Freigrenze beim Solidaritätszuschlag für sonstige Bezüge in Euro
        self.SOLZSBMG = BigDecimal(0)

        # Zu versteuerndes Einkommen für die Ermittlung der Bemessungsgrundlage des Solidaritätszuschlags zur Prüfung der Freigrenze beim Solidaritätszuschlag für sonstige Bezüge in Euro, Cent (2 Dezimalstellen)
        self.SOLZSZVE = BigDecimal(0)

        # Bemessungsgrundlage des Solidaritätszuschlags für die Prüfung der Freigrenze beim Solidaritätszuschlag für die Vergütung für mehrjährige Tätigkeit in Euro
        self.SOLZVBMG = BigDecimal(0)

        # Tarifliche Einkommensteuer in EURO
        self.ST = BigDecimal(0)

        # Tarifliche Einkommensteuer auf das 1,25-fache ZX in EURO
        self.ST1 = BigDecimal(0)

        # Tarifliche Einkommensteuer auf das 0,75-fache ZX in EURO
        self.ST2 = BigDecimal(0)

        # Bemessungsgrundlage fuer den Versorgungsfreibetrag in Cents
        self.VBEZB = BigDecimal(0)

        # Bemessungsgrundlage für den Versorgungsfreibetrag in Cent für
        # den sonstigen Bezug
        self.VBEZBSO = BigDecimal(0)

        # Zwischenfeld zu X fuer die Berechnung der Steuer nach § 39b
        # Abs. 2 Satz 7 EStG in €
        self.VERGL = BigDecimal(0)

        # Hoechstbetrag der Vorsorgepauschale nach Alterseinkuenftegesetz in EURO, C
        self.VHB = BigDecimal(0)

        # Jahreswert der berücksichtigten Beiträge zur privaten Basis-Krankenversicherung und
        # privaten Pflege-Pflichtversicherung (ggf. auch die Mindestvorsorgepauschale) in Cent.
        self.VKV = BigDecimal(0)

        # Vorsorgepauschale in EURO, C (2 Dezimalstellen)
        self.VSP = BigDecimal(0)

        # Vorsorgepauschale nach Alterseinkuenftegesetz in EURO, C
        self.VSPN = BigDecimal(0)

        # Zwischenwert 1 bei der Berechnung der Vorsorgepauschale nach
        # dem Alterseinkuenftegesetz in EURO, C (2 Dezimalstellen)
        self.VSP1 = BigDecimal(0)

        # Zwischenwert 2 bei der Berechnung der Vorsorgepauschale nach
        # dem Alterseinkuenftegesetz in EURO, C (2 Dezimalstellen)
        self.VSP2 = BigDecimal(0)

        # Vorsorgepauschale mit Teilbeträgen für die gesetzliche Kranken- und
        # soziale Pflegeversicherung nach fiktiven Beträgen oder ggf. für die
        # private Basiskrankenversicherung und private Pflege-Pflichtversicherung
        # in Euro, Cent (2 Dezimalstellen)
        self.VSP3 = BigDecimal(0)

        # Erster Grenzwert in Steuerklasse V/VI in Euro
        self.W1STKL5 = BigDecimal(0)

        # Zweiter Grenzwert in Steuerklasse V/VI in Euro
        self.W2STKL5 = BigDecimal(0)

        # Dritter Grenzwert in Steuerklasse V/VI in Euro
        self.W3STKL5 = BigDecimal(0)

        # Zu versteuerndes Einkommen gem. § 32a Abs. 1 und 2 EStG €, C
        # (2 Dezimalstellen)
        self.X = BigDecimal(0)

        # Gem. § 32a Abs. 1 EStG (6 Dezimalstellen)
        self.Y = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4 in €, C (2 Dezimalstellen)
        # nach Abzug der Freibeträge nach § 39 b Abs. 2 Satz 3 und 4.
        self.ZRE4 = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4 in €, C (2 Dezimalstellen)
        self.ZRE4J = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes RE4 in €, C (2 Dezimalstellen)
        # nach Abzug des Versorgungsfreibetrags und des Alterentlastungsbetrags
        # zur Berechnung der Vorsorgepauschale in €, Cent (2 Dezimalstellen)
        self.ZRE4VP = BigDecimal(0)

        # Feste Tabellenfreibeträge (ohne Vorsorgepauschale) in €, Cent
        # (2 Dezimalstellen)
        self.ZTABFB = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes (VBEZ abzueglich FVB) in
        # EURO, C (2 Dezimalstellen)
        self.ZVBEZ = BigDecimal(0)

        # Auf einen Jahreslohn hochgerechnetes VBEZ in €, C (2 Dezimalstellen)
        self.ZVBEZJ = BigDecimal(0)

        # Zu versteuerndes Einkommen in €, C (2 Dezimalstellen)
        self.ZVE = BigDecimal(0)

        # Zwischenfeld zu X fuer die Berechnung der Steuer nach § 39b
        # Abs. 2 Satz 7 EStG in €
        self.ZX = BigDecimal(0)

        # Zwischenfeld zu X fuer die Berechnung der Steuer nach § 39b
        # Abs. 2 Satz 7 EStG in €
        self.ZZX = BigDecimal(0)


    def setAf(self, value):
        self.af = value

    def setAjahr(self, value):
        self.AJAHR = value

    def setAlter1(self, value):
        self.ALTER1 = value

    def setF(self, value):
        self.f = value

    def setJfreib(self, value):
        self.JFREIB = BigDecimal(value)

    def setJhinzu(self, value):
        self.JHINZU = BigDecimal(value)

    def setJre4(self, value):
        self.JRE4 = BigDecimal(value)

    def setJre4ent(self, value):
        self.JRE4ENT = BigDecimal(value)

    def setJvbez(self, value):
        self.JVBEZ = BigDecimal(value)

    def setKrv(self, value):
        self.KRV = value

    def setKvz(self, value):
        self.KVZ = BigDecimal(value)

    def setLzz(self, value):
        self.LZZ = value

    def setLzzfreib(self, value):
        self.LZZFREIB = BigDecimal(value)

    def setLzzhinzu(self, value):
        self.LZZHINZU = BigDecimal(value)

    def setMbv(self, value):
        self.MBV = BigDecimal(value)

    def setPkpv(self, value):
        self.PKPV = BigDecimal(value)

    def setPkv(self, value):
        self.PKV = value

    def setPva(self, value):
        self.PVA = BigDecimal(value)

    def setPvs(self, value):
        self.PVS = value

    def setPvz(self, value):
        self.PVZ = value

    def setR(self, value):
        self.R = value

    def setRe4(self, value):
        self.RE4 = BigDecimal(value)

    def setSonstb(self, value):
        self.SONSTB = BigDecimal(value)

    def setSonstent(self, value):
        self.SONSTENT = BigDecimal(value)

    def setSterbe(self, value):
        self.STERBE = BigDecimal(value)

    def setStkl(self, value):
        self.STKL = value

    def setVbez(self, value):
        self.VBEZ = BigDecimal(value)

    def setVbezm(self, value):
        self.VBEZM = BigDecimal(value)

    def setVbezs(self, value):
        self.VBEZS = BigDecimal(value)

    def setVbs(self, value):
        self.VBS = BigDecimal(value)

    def setVjahr(self, value):
        self.VJAHR = value

    def setZkf(self, value):
        self.ZKF = BigDecimal(value)

    def setZmvb(self, value):
        self.ZMVB = value

    def getBk(self):
        return self.BK

    def getBks(self):
        return self.BKS

    def getLstlzz(self):
        return self.LSTLZZ

    def getSolzlzz(self):
        return self.SOLZLZZ

    def getSolzs(self):
        return self.SOLZS

    def getSts(self):
        return self.STS

    def getVkvlzz(self):
        return self.VKVLZZ

    def getVkvsonst(self):
        return self.VKVSONST

    def getVfrb(self):
        return self.VFRB

    def getVfrbs1(self):
        return self.VFRBS1

    def getVfrbs2(self):
        return self.VFRBS2

    def getWvfrb(self):
        return self.WVFRB

    def getWvfrbo(self):
        return self.WVFRBO

    def getWvfrbm(self):
        return self.WVFRBM

    def MAIN(self):
        """
        PROGRAMMABLAUFPLAN, PAP Seite 13
        """
        self.MPARA()
        self.MRE4JL()
        self.VBEZBSO = BigDecimal.ZERO
        self.MRE4()
        self.MRE4ABZ()
        self.MBERECH()
        self.MSONST()

    def MPARA(self):
        """
        Zuweisung von Werten für bestimmte Sozialversicherungsparameter  PAP Seite 14
        """
        if self.KRV < 1:
            self.BBGRV = BigDecimal(96600)
            self.RVSATZAN = BigDecimal.valueOf(0.093)
        self.BBGKVPV = BigDecimal(66150)
        self.KVSATZAN = self.KVZ.divide(Lohnsteuer2025.ZAHL2).divide(Lohnsteuer2025.ZAHL100).add(BigDecimal.valueOf(0.07))
        self.KVSATZAG = BigDecimal.valueOf(0.0125).add(BigDecimal.valueOf(0.07))
        if self.PVS == 1:
            self.PVSATZAN = BigDecimal.valueOf(0.023)
            self.PVSATZAG = BigDecimal.valueOf(0.013)
        else:
            self.PVSATZAN = BigDecimal.valueOf(0.018)
            self.PVSATZAG = BigDecimal.valueOf(0.018)
        if self.PVZ == 1:
            self.PVSATZAN = self.PVSATZAN.add(BigDecimal.valueOf(0.006))
        else:
            self.PVSATZAN = self.PVSATZAN.subtract(self.PVA.multiply(BigDecimal.valueOf(0.0025)))
        self.W1STKL5 = BigDecimal(13785)
        self.W2STKL5 = BigDecimal(34240)
        self.W3STKL5 = BigDecimal(222260)
        self.GFB = BigDecimal(12096)
        self.SOLZFREI = BigDecimal(19950)

    def MRE4JL(self):
        """
        Ermittlung des Jahresarbeitslohns nach § 39 b Abs. 2 Satz 2 EStG, PAP Seite 15
        """
        if self.LZZ == 1:
            self.ZRE4J = self.RE4.divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.ZVBEZJ = self.VBEZ.divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.JLFREIB = self.LZZFREIB.divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            self.JLHINZU = self.LZZHINZU.divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        else:
            if self.LZZ == 2:
                self.ZRE4J = self.RE4.multiply(Lohnsteuer2025.ZAHL12).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                self.ZVBEZJ = self.VBEZ.multiply(Lohnsteuer2025.ZAHL12).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                self.JLFREIB = self.LZZFREIB.multiply(Lohnsteuer2025.ZAHL12).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                self.JLHINZU = self.LZZHINZU.multiply(Lohnsteuer2025.ZAHL12).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
            else:
                if self.LZZ == 3:
                    self.ZRE4J = self.RE4.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                    self.ZVBEZJ = self.VBEZ.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                    self.JLFREIB = self.LZZFREIB.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                    self.JLHINZU = self.LZZHINZU.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL700, 2, BigDecimal.ROUND_DOWN)
                else:
                    self.ZRE4J = self.RE4.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                    self.ZVBEZJ = self.VBEZ.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                    self.JLFREIB = self.LZZFREIB.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
                    self.JLHINZU = self.LZZHINZU.multiply(Lohnsteuer2025.ZAHL360).divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        if self.af == 0:
            self.f = 1

    def MRE4(self):
        """
        Freibeträge für Versorgungsbezüge, Altersentlastungsbetrag (§ 39b Abs. 2 Satz 3 EStG), PAP Seite 16
        """
        if self.ZVBEZJ.compareTo(BigDecimal.ZERO) == 0:
            self.FVBZ = BigDecimal.ZERO
            self.FVB = BigDecimal.ZERO
            self.FVBZSO = BigDecimal.ZERO
            self.FVBSO = BigDecimal.ZERO
        else:
            if self.VJAHR < 2006:
                self.J = 1
            else:
                if self.VJAHR < 2058:
                    self.J = self.VJAHR - 2004
                else:
                    self.J = 54
            if self.LZZ == 1:
                self.VBEZB = self.VBEZM.multiply(BigDecimal.valueOf(self.ZMVB)).add(self.VBEZS)
                self.HFVB = Lohnsteuer2025.TAB2[self.J].divide(Lohnsteuer2025.ZAHL12).multiply(BigDecimal.valueOf(self.ZMVB)).setScale(0, BigDecimal.ROUND_UP)
                self.FVBZ = Lohnsteuer2025.TAB3[self.J].divide(Lohnsteuer2025.ZAHL12).multiply(BigDecimal.valueOf(self.ZMVB)).setScale(0, BigDecimal.ROUND_UP)
            else:
                self.VBEZB = self.VBEZM.multiply(Lohnsteuer2025.ZAHL12).add(self.VBEZS).setScale(2, BigDecimal.ROUND_DOWN)
                self.HFVB = Lohnsteuer2025.TAB2[self.J]
                self.FVBZ = Lohnsteuer2025.TAB3[self.J]
            self.FVB = self.VBEZB.multiply(Lohnsteuer2025.TAB1[self.J]).divide(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_UP)
            if self.FVB.compareTo(self.HFVB) == 1:
                self.FVB = self.HFVB
            if self.FVB.compareTo(self.ZVBEZJ) == 1:
                self.FVB = self.ZVBEZJ
            self.FVBSO = self.FVB.add(self.VBEZBSO.multiply(Lohnsteuer2025.TAB1[self.J]).divide(Lohnsteuer2025.ZAHL100)).setScale(2, BigDecimal.ROUND_UP)
            if self.FVBSO.compareTo(Lohnsteuer2025.TAB2[self.J]) == 1:
                self.FVBSO = Lohnsteuer2025.TAB2[self.J]
            self.HFVBZSO = self.VBEZB.add(self.VBEZBSO).divide(Lohnsteuer2025.ZAHL100).subtract(self.FVBSO).setScale(2, BigDecimal.ROUND_DOWN)
            self.FVBZSO = self.FVBZ.add(self.VBEZBSO.divide(Lohnsteuer2025.ZAHL100)).setScale(0, BigDecimal.ROUND_UP)
            if self.FVBZSO.compareTo(self.HFVBZSO) == 1:
                self.FVBZSO = self.HFVBZSO.setScale(0, BigDecimal.ROUND_UP)
            if self.FVBZSO.compareTo(Lohnsteuer2025.TAB3[self.J]) == 1:
                self.FVBZSO = Lohnsteuer2025.TAB3[self.J]
            self.HFVBZ = self.VBEZB.divide(Lohnsteuer2025.ZAHL100).subtract(self.FVB).setScale(2, BigDecimal.ROUND_DOWN)
            if self.FVBZ.compareTo(self.HFVBZ) == 1:
                self.FVBZ = self.HFVBZ.setScale(0, BigDecimal.ROUND_UP)
        self.MRE4ALTE()

    def MRE4ALTE(self):
        """
        Altersentlastungsbetrag (§ 39b Abs. 2 Satz 3 EStG), PAP Seite 17
        """
        if self.ALTER1 == 0:
            self.ALTE = BigDecimal.ZERO
        else:
            if self.AJAHR < 2006:
                self.K = 1
            else:
                if self.AJAHR < 2058:
                    self.K = self.AJAHR - 2004
                else:
                    self.K = 54
            self.BMG = self.ZRE4J.subtract(self.ZVBEZJ)
            self.ALTE = self.BMG.multiply(Lohnsteuer2025.TAB4[self.K]).setScale(0, BigDecimal.ROUND_UP)
            self.HBALTE = Lohnsteuer2025.TAB5[self.K]
            if self.ALTE.compareTo(self.HBALTE) == 1:
                self.ALTE = self.HBALTE

    def MRE4ABZ(self):
        """
        Ermittlung des Jahresarbeitslohns nach Abzug der Freibeträge nach § 39 b Abs. 2 Satz 3 und 4 EStG, PAP Seite 20
        """
        self.ZRE4 = self.ZRE4J.subtract(self.FVB).subtract(self.ALTE).subtract(self.JLFREIB).add(self.JLHINZU).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZRE4.compareTo(BigDecimal.ZERO) == -1:
            self.ZRE4 = BigDecimal.ZERO
        self.ZRE4VP = self.ZRE4J
        self.ZVBEZ = self.ZVBEZJ.subtract(self.FVB).setScale(2, BigDecimal.ROUND_DOWN)
        if self.ZVBEZ.compareTo(BigDecimal.ZERO) == -1:
            self.ZVBEZ = BigDecimal.ZERO

    def MBERECH(self):
        """
        Berechnung fuer laufende Lohnzahlungszeitraueme Seite 21
        """
        self.MZTABFB()
        self.VFRB = self.ANP.add(self.FVB.add(self.FVBZ)).multiply(Lohnsteuer2025.ZAHL100).setScale(0, BigDecimal.ROUND_DOWN)
        self.MLSTJAHR()
        self.WVFRB = self.ZVE.subtract(self.GFB).multiply(Lohnsteuer2025.ZAHL100).setScale(0, BigDecimal.ROUND_DOWN)
        if self.WVFRB.compareTo(BigDecimal.ZERO) == -1:
            self.WVFRB = BigDecimal.valueOf(0)
        self.LSTJAHR = self.ST.multiply(BigDecimal.valueOf(self.f)).setScale(0, BigDecimal.ROUND_DOWN)
        self.UPLSTLZZ()
        self.UPVKVLZZ()
        if self.ZKF.compareTo(BigDecimal.ZERO) == 1:
            self.ZTABFB = self.ZTABFB.add(self.KFB)
            self.MRE4ABZ()
            self.MLSTJAHR()
            self.JBMG = self.ST.multiply(BigDecimal.valueOf(self.f)).setScale(0, BigDecimal.ROUND_DOWN)
        else:
            self.JBMG = self.LSTJAHR
        self.MSOLZ()

    def MZTABFB(self):
        """
        Ermittlung der festen Tabellenfreibeträge (ohne Vorsorgepauschale), PAP Seite 22
        """
        self.ANP = BigDecimal.ZERO
        if self.ZVBEZ.compareTo(BigDecimal.ZERO) >= 0 and self.ZVBEZ.compareTo(self.FVBZ) == -1:
            self.FVBZ = BigDecimal.valueOf(self.ZVBEZ.longValue())
        if self.STKL < 6:
            if self.ZVBEZ.compareTo(BigDecimal.ZERO) == 1:
                if self.ZVBEZ.subtract(self.FVBZ).compareTo(BigDecimal.valueOf(102)) == -1:
                    self.ANP = self.ZVBEZ.subtract(self.FVBZ).setScale(0, BigDecimal.ROUND_UP)
                else:
                    self.ANP = BigDecimal.valueOf(102)
        else:
            self.FVBZ = BigDecimal.valueOf(0)
            self.FVBZSO = BigDecimal.valueOf(0)
        if self.STKL < 6:
            if self.ZRE4.compareTo(self.ZVBEZ) == 1:
                if self.ZRE4.subtract(self.ZVBEZ).compareTo(BigDecimal.valueOf(1230)) == -1:
                    self.ANP = self.ANP.add(self.ZRE4).subtract(self.ZVBEZ).setScale(0, BigDecimal.ROUND_UP)
                else:
                    self.ANP = self.ANP.add(BigDecimal.valueOf(1230))
        self.KZTAB = 1
        if self.STKL == 1:
            self.SAP = BigDecimal.valueOf(36)
            self.KFB = self.ZKF.multiply(BigDecimal.valueOf(9600)).setScale(0, BigDecimal.ROUND_DOWN)
        else:
            if self.STKL == 2:
                self.EFA = BigDecimal.valueOf(4260)
                self.SAP = BigDecimal.valueOf(36)
                self.KFB = self.ZKF.multiply(BigDecimal.valueOf(9600)).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                if self.STKL == 3:
                    self.KZTAB = 2
                    self.SAP = BigDecimal.valueOf(36)
                    self.KFB = self.ZKF.multiply(BigDecimal.valueOf(9600)).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    if self.STKL == 4:
                        self.SAP = BigDecimal.valueOf(36)
                        self.KFB = self.ZKF.multiply(BigDecimal.valueOf(4800)).setScale(0, BigDecimal.ROUND_DOWN)
                    else:
                        if self.STKL == 5:
                            self.SAP = BigDecimal.valueOf(36)
                            self.KFB = BigDecimal.ZERO
                        else:
                            self.KFB = BigDecimal.ZERO
        self.ZTABFB = self.EFA.add(self.ANP).add(self.SAP).add(self.FVBZ).setScale(2, BigDecimal.ROUND_DOWN)

    def MLSTJAHR(self):
        """
        Ermittlung Jahreslohnsteuer, PAP Seite 23
        """
        self.UPEVP()
        self.ZVE = self.ZRE4.subtract(self.ZTABFB).subtract(self.VSP)
        self.UPMLST()

    def UPVKVLZZ(self):
        """
        PAP Seite 24
        """
        self.UPVKV()
        self.JW = self.VKV
        self.UPANTEIL()
        self.VKVLZZ = self.ANTEIL1

    def UPVKV(self):
        """
        PAP Seite 24
        """
        if self.PKV > 0:
            if self.VSP2.compareTo(self.VSP3) == 1:
                self.VKV = self.VSP2.multiply(Lohnsteuer2025.ZAHL100)
            else:
                self.VKV = self.VSP3.multiply(Lohnsteuer2025.ZAHL100)
        else:
            self.VKV = BigDecimal.ZERO

    def UPLSTLZZ(self):
        """
        PAP Seite 25
        """
        self.JW = self.LSTJAHR.multiply(Lohnsteuer2025.ZAHL100)
        self.UPANTEIL()
        self.LSTLZZ = self.ANTEIL1

    def UPMLST(self):
        """
        Ermittlung der Jahreslohnsteuer aus dem Einkommensteuertarif. PAP Seite 26
        """
        if self.ZVE.compareTo(Lohnsteuer2025.ZAHL1) == -1:
            self.ZVE = BigDecimal.ZERO
            self.X = BigDecimal.ZERO
        else:
            self.X = self.ZVE.divide(BigDecimal.valueOf(self.KZTAB)).setScale(0, BigDecimal.ROUND_DOWN)
        if self.STKL < 5:
            self.UPTAB25()
        else:
            self.MST5_6()

    def UPEVP(self):
        """
        Vorsorgepauschale (§ 39b Absatz 2 Satz 5 Nummer 3 und Absatz 4 EStG) PAP Seite 27
        """
        if self.KRV == 1:
            self.VSP1 = BigDecimal.ZERO
        else:
            if self.ZRE4VP.compareTo(self.BBGRV) == 1:
                self.ZRE4VP = self.BBGRV
            self.VSP1 = self.ZRE4VP.multiply(self.RVSATZAN).setScale(2, BigDecimal.ROUND_DOWN)
        self.VSP2 = self.ZRE4VP.multiply(BigDecimal.valueOf(0.12)).setScale(2, BigDecimal.ROUND_DOWN)
        if self.STKL == 3:
            self.VHB = BigDecimal.valueOf(3000)
        else:
            self.VHB = BigDecimal.valueOf(1900)
        if self.VSP2.compareTo(self.VHB) == 1:
            self.VSP2 = self.VHB
        self.VSPN = self.VSP1.add(self.VSP2).setScale(0, BigDecimal.ROUND_UP)
        self.MVSP()
        if self.VSPN.compareTo(self.VSP) == 1:
            self.VSP = self.VSPN.setScale(2, BigDecimal.ROUND_DOWN)

    def MVSP(self):
        """
        Vorsorgepauschale (§39b Abs. 2 Satz 5 Nr 3 EStG) Vergleichsberechnung fuer Guenstigerpruefung, PAP Seite 28
        """
        if self.ZRE4VP.compareTo(self.BBGKVPV) == 1:
            self.ZRE4VP = self.BBGKVPV
        if self.PKV > 0:
            if self.STKL == 6:
                self.VSP3 = BigDecimal.ZERO
            else:
                self.VSP3 = self.PKPV.multiply(Lohnsteuer2025.ZAHL12).divide(Lohnsteuer2025.ZAHL100)
                if self.PKV == 2:
                    self.VSP3 = self.VSP3.subtract(self.ZRE4VP.multiply(self.KVSATZAG.add(self.PVSATZAG))).setScale(2, BigDecimal.ROUND_DOWN)
        else:
            self.VSP3 = self.ZRE4VP.multiply(self.KVSATZAN.add(self.PVSATZAN)).setScale(2, BigDecimal.ROUND_DOWN)
        self.VSP = self.VSP3.add(self.VSP1).setScale(0, BigDecimal.ROUND_UP)

    def MST5_6(self):
        """
        Lohnsteuer fuer die Steuerklassen V und VI (§ 39b Abs. 2 Satz 7 EStG), PAP Seite 29
        """
        self.ZZX = self.X
        if self.ZZX.compareTo(self.W2STKL5) == 1:
            self.ZX = self.W2STKL5
            self.UP5_6()
            if self.ZZX.compareTo(self.W3STKL5) == 1:
                self.ST = self.ST.add(self.W3STKL5.subtract(self.W2STKL5).multiply(BigDecimal.valueOf(0.42))).setScale(0, BigDecimal.ROUND_DOWN)
                self.ST = self.ST.add(self.ZZX.subtract(self.W3STKL5).multiply(BigDecimal.valueOf(0.45))).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                self.ST = self.ST.add(self.ZZX.subtract(self.W2STKL5).multiply(BigDecimal.valueOf(0.42))).setScale(0, BigDecimal.ROUND_DOWN)
        else:
            self.ZX = self.ZZX
            self.UP5_6()
            if self.ZZX.compareTo(self.W1STKL5) == 1:
                self.VERGL = self.ST
                self.ZX = self.W1STKL5
                self.UP5_6()
                self.HOCH = self.ST.add(self.ZZX.subtract(self.W1STKL5).multiply(BigDecimal.valueOf(0.42))).setScale(0, BigDecimal.ROUND_DOWN)
                if self.HOCH.compareTo(self.VERGL) == -1:
                    self.ST = self.HOCH
                else:
                    self.ST = self.VERGL

    def UP5_6(self):
        """
        Unterprogramm zur Lohnsteuer fuer die Steuerklassen V und VI (§ 39b Abs. 2 Satz 7 EStG), PAP Seite 30
        """
        self.X = self.ZX.multiply(BigDecimal.valueOf(1.25)).setScale(2, BigDecimal.ROUND_DOWN)
        self.UPTAB25()
        self.ST1 = self.ST
        self.X = self.ZX.multiply(BigDecimal.valueOf(0.75)).setScale(2, BigDecimal.ROUND_DOWN)
        self.UPTAB25()
        self.ST2 = self.ST
        self.DIFF = self.ST1.subtract(self.ST2).multiply(Lohnsteuer2025.ZAHL2)
        self.MIST = self.ZX.multiply(BigDecimal.valueOf(0.14)).setScale(0, BigDecimal.ROUND_DOWN)
        if self.MIST.compareTo(self.DIFF) == 1:
            self.ST = self.MIST
        else:
            self.ST = self.DIFF

    def MSOLZ(self):
        """
        Solidaritaetszuschlag, PAP Seite 31
        """
        self.SOLZFREI = self.SOLZFREI.multiply(BigDecimal.valueOf(self.KZTAB))
        if self.JBMG.compareTo(self.SOLZFREI) == 1:
            self.SOLZJ = self.JBMG.multiply(BigDecimal.valueOf(5.5)).divide(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.SOLZMIN = self.JBMG.subtract(self.SOLZFREI).multiply(BigDecimal.valueOf(11.9)).divide(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            if self.SOLZMIN.compareTo(self.SOLZJ) == -1:
                self.SOLZJ = self.SOLZMIN
            self.JW = self.SOLZJ.multiply(Lohnsteuer2025.ZAHL100).setScale(0, BigDecimal.ROUND_DOWN)
            self.UPANTEIL()
            self.SOLZLZZ = self.ANTEIL1
        else:
            self.SOLZLZZ = BigDecimal.ZERO
        if self.R > 0:
            self.JW = self.JBMG.multiply(Lohnsteuer2025.ZAHL100)
            self.UPANTEIL()
            self.BK = self.ANTEIL1
        else:
            self.BK = BigDecimal.ZERO

    def UPANTEIL(self):
        """
        Anteil von Jahresbetraegen fuer einen LZZ (§ 39b Abs. 2 Satz 9 EStG), PAP Seite 32
        """
        if self.LZZ == 1:
            self.ANTEIL1 = self.JW
        else:
            if self.LZZ == 2:
                self.ANTEIL1 = self.JW.divide(Lohnsteuer2025.ZAHL12, 0, BigDecimal.ROUND_DOWN)
            else:
                if self.LZZ == 3:
                    self.ANTEIL1 = self.JW.multiply(Lohnsteuer2025.ZAHL7).divide(Lohnsteuer2025.ZAHL360, 0, BigDecimal.ROUND_DOWN)
                else:
                    self.ANTEIL1 = self.JW.divide(Lohnsteuer2025.ZAHL360, 0, BigDecimal.ROUND_DOWN)

    def MSONST(self):
        """
        Berechnung sonstiger Bezuege nach § 39b Abs. 3 Saetze 1 bis 8 EStG), PAP Seite 33
        """
        self.LZZ = 1
        if self.ZMVB == 0:
            self.ZMVB = 12
        if self.SONSTB.compareTo(BigDecimal.ZERO) == 0 and self.MBV.compareTo(BigDecimal.ZERO) == 0:
            self.VKVSONST = BigDecimal.ZERO
            self.LSTSO = BigDecimal.ZERO
            self.STS = BigDecimal.ZERO
            self.SOLZS = BigDecimal.ZERO
            self.BKS = BigDecimal.ZERO
        else:
            self.MOSONST()
            self.UPVKV()
            self.VKVSONST = self.VKV
            self.ZRE4J = self.JRE4.add(self.SONSTB).divide(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.ZVBEZJ = self.JVBEZ.add(self.VBS).divide(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            self.VBEZBSO = self.STERBE
            self.MRE4SONST()
            self.MLSTJAHR()
            self.WVFRBM = self.ZVE.subtract(self.GFB).multiply(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
            if self.WVFRBM.compareTo(BigDecimal.ZERO) == -1:
                self.WVFRBM = BigDecimal.ZERO
            self.UPVKV()
            self.VKVSONST = self.VKV.subtract(self.VKVSONST)
            self.LSTSO = self.ST.multiply(Lohnsteuer2025.ZAHL100)
            self.STS = self.LSTSO.subtract(self.LSTOSO).multiply(BigDecimal.valueOf(self.f)).divide(Lohnsteuer2025.ZAHL100, 0, BigDecimal.ROUND_DOWN).multiply(Lohnsteuer2025.ZAHL100)
            self.STSMIN()

    def STSMIN(self):
        """
        PAP Seite 34
        """
        if self.STS.compareTo(BigDecimal.ZERO) == -1:
            if self.MBV.compareTo(BigDecimal.ZERO) == 0:
                pass
            else:
                self.LSTLZZ = self.LSTLZZ.add(self.STS)
                if self.LSTLZZ.compareTo(BigDecimal.ZERO) == -1:
                    self.LSTLZZ = BigDecimal.ZERO
                self.SOLZLZZ = self.SOLZLZZ.add(self.STS.multiply(BigDecimal.valueOf(5.5).divide(Lohnsteuer2025.ZAHL100))).setScale(0, BigDecimal.ROUND_DOWN)
                if self.SOLZLZZ.compareTo(BigDecimal.ZERO) == -1:
                    self.SOLZLZZ = BigDecimal.ZERO
                self.BK = self.BK.add(self.STS)
                if self.BK.compareTo(BigDecimal.ZERO) == -1:
                    self.BK = BigDecimal.ZERO
            self.STS = BigDecimal.ZERO
            self.SOLZS = BigDecimal.ZERO
        else:
            self.MSOLZSTS()
        if self.R > 0:
            self.BKS = self.STS
        else:
            self.BKS = BigDecimal.ZERO

    def MSOLZSTS(self):
        """
        Berechnung des SolZ auf sonstige Bezüge, PAP Seite 35
        """
        if self.ZKF.compareTo(BigDecimal.ZERO) == 1:
            self.SOLZSZVE = self.ZVE.subtract(self.KFB)
        else:
            self.SOLZSZVE = self.ZVE
        if self.SOLZSZVE.compareTo(BigDecimal.ONE) == -1:
            self.SOLZSZVE = BigDecimal.ZERO
            self.X = BigDecimal.ZERO
        else:
            self.X = self.SOLZSZVE.divide(BigDecimal.valueOf(self.KZTAB), 0, BigDecimal.ROUND_DOWN)
        if self.STKL < 5:
            self.UPTAB25()
        else:
            self.MST5_6()
        self.SOLZSBMG = self.ST.multiply(BigDecimal.valueOf(self.f)).setScale(0, BigDecimal.ROUND_DOWN)
        if self.SOLZSBMG.compareTo(self.SOLZFREI) == 1:
            self.SOLZS = self.STS.multiply(BigDecimal.valueOf(5.5)).divide(Lohnsteuer2025.ZAHL100, 0, BigDecimal.ROUND_DOWN)
        else:
            self.SOLZS = BigDecimal.ZERO

    def MOSONST(self):
        """
        Sonderberechnung ohne sonstige Bezüge für Berechnung bei sonstigen Bezügen oder Vergütung für mehrjährige Tätigkeit, PAP Seite 36
        """
        self.ZRE4J = self.JRE4.divide(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
        self.ZVBEZJ = self.JVBEZ.divide(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
        self.JLFREIB = self.JFREIB.divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        self.JLHINZU = self.JHINZU.divide(Lohnsteuer2025.ZAHL100, 2, BigDecimal.ROUND_DOWN)
        self.MRE4()
        self.MRE4ABZ()
        self.ZRE4VP = self.ZRE4VP.subtract(self.JRE4ENT.divide(Lohnsteuer2025.ZAHL100))
        self.MZTABFB()
        self.VFRBS1 = self.ANP.add(self.FVB.add(self.FVBZ)).multiply(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
        self.MLSTJAHR()
        self.WVFRBO = self.ZVE.subtract(self.GFB).multiply(Lohnsteuer2025.ZAHL100).setScale(2, BigDecimal.ROUND_DOWN)
        if self.WVFRBO.compareTo(BigDecimal.ZERO) == -1:
            self.WVFRBO = BigDecimal.ZERO
        self.LSTOSO = self.ST.multiply(Lohnsteuer2025.ZAHL100)

    def MRE4SONST(self):
        """
        Sonderberechnung mit sonstige Bezüge für Berechnung bei sonstigen Bezügen oder Vergütung für mehrjährige Tätigkeit, PAP Seite 37
        """
        self.MRE4()
        self.FVB = self.FVBSO
        self.MRE4ABZ()
        self.ZRE4VP = self.ZRE4VP.add(self.MBV.divide(Lohnsteuer2025.ZAHL100)).subtract(self.JRE4ENT.divide(Lohnsteuer2025.ZAHL100)).subtract(self.SONSTENT.divide(Lohnsteuer2025.ZAHL100))
        self.FVBZ = self.FVBZSO
        self.MZTABFB()
        self.VFRBS2 = self.ANP.add(self.FVB).add(self.FVBZ).multiply(Lohnsteuer2025.ZAHL100).subtract(self.VFRBS1)

    def UPTAB25(self):
        """
        Tarifliche Einkommensteuer §32a EStG, PAP Seite 38
        """
        if self.X.compareTo(self.GFB.add(Lohnsteuer2025.ZAHL1)) == -1:
            self.ST = BigDecimal.ZERO
        else:
            if self.X.compareTo(BigDecimal.valueOf(17444)) == -1:
                self.Y = self.X.subtract(self.GFB).divide(Lohnsteuer2025.ZAHL10000, 6, BigDecimal.ROUND_DOWN)
                self.RW = self.Y.multiply(BigDecimal.valueOf(932.3))
                self.RW = self.RW.add(BigDecimal.valueOf(1400))
                self.ST = self.RW.multiply(self.Y).setScale(0, BigDecimal.ROUND_DOWN)
            else:
                if self.X.compareTo(BigDecimal.valueOf(68481)) == -1:
                    self.Y = self.X.subtract(BigDecimal.valueOf(17443)).divide(Lohnsteuer2025.ZAHL10000, 6, BigDecimal.ROUND_DOWN)
                    self.RW = self.Y.multiply(BigDecimal.valueOf(176.64))
                    self.RW = self.RW.add(BigDecimal.valueOf(2397))
                    self.RW = self.RW.multiply(self.Y)
                    self.ST = self.RW.add(BigDecimal.valueOf(1015.13)).setScale(0, BigDecimal.ROUND_DOWN)
                else:
                    if self.X.compareTo(BigDecimal.valueOf(277826)) == -1:
                        self.ST = self.X.multiply(BigDecimal.valueOf(0.42)).subtract(BigDecimal.valueOf(10911.92)).setScale(0, BigDecimal.ROUND_DOWN)
                    else:
                        self.ST = self.X.multiply(BigDecimal.valueOf(0.45)).subtract(BigDecimal.valueOf(19246.67)).setScale(0, BigDecimal.ROUND_DOWN)
        self.ST = self.ST.multiply(BigDecimal.valueOf(self.KZTAB))
