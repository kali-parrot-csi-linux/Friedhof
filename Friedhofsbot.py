def friedhof_beratung():
    print("Willkommen beim Friedhof Eberstadt!")

    # Frage 1: Sterbefall
    sterbefall = input("Haben Sie einen Sterbefall? (ja/nein): ").strip().lower()
    if sterbefall == "ja":
        while True:
            bestattung = input(
                "Möchten Sie eine Erdbestattung oder eine Feuerbestattung? (erdbestattung/feuerbestattung): ").strip().lower()
            if bestattung == "erdbestattung":
                waehlen_erdbestattung()
                break  # Beende die Schleife nach der Verarbeitung
            elif bestattung == "feuerbestattung":
                feuerbestattung()
                break  # Beende die Schleife nach der Verarbeitung
            else:
                print("Ungültige Eingabe. Bitte wählen Sie entweder 'erdbestattung' oder 'feuerbestattung'.")

    # Frage 2: Allgemeine Information
    info = input("Möchten Sie eine allgemeine Information über Gräber? (ja/nein): ").strip().lower()
    if info == "ja":
        grab_arten_preise()

    # Frage 3: Vorkauf
    vorkauf = input("Möchten Sie ein Grab im Vorkauf erwerben? (ja/nein): ").strip().lower()
    if vorkauf == "ja":
        while True:
            bestattung = input(
                "Möchten Sie eine Erdbestattung oder eine Feuerbestattung? (erdbestattung/feuerbestattung): ").strip().lower()
            if bestattung == "erdbestattung":
                waehlen_erdbestattung()
                break
            elif bestattung == "feuerbestattung":
                feuerbestattung()
                break
            else:
                print("Ungültige Eingabe. Bitte wählen Sie entweder 'erdbestattung' oder 'feuerbestattung'.")

    # Frage 4: Verlängerung
    verlaengerung = input("Möchten Sie ein bestehendes Grab verlängern? (ja/nein): ").strip().lower()
    if verlaengerung == "ja":
        grab_verlaengerung()

    print(
        "Vielen Dank für Ihre Anfrage! Bitte setzen Sie sich mit der Friedhofsverwaltung in Verbindung, um die Realisierung zu besprechen.")


def waehlen_erdbestattung():
    while True:
        grabart = input(
            "Möchten Sie eine Wahlgrabstelle oder eine Reihengrabstelle? (wahlgrab/reihengrab): ").strip().lower()
        if grabart == "wahlgrab":
            while True:
                try:
                    stellen = int(input("Wie viele Stellen soll die Wahlgrabstelle haben? (1/2/3/4): "))
                    if stellen == 1:
                        print(
                            "Die Grabstätte kostet 1700 Euro. Es sind 1 Erdbestattung und 2 Urnenbestattungen möglich.")
                        break
                    elif stellen == 2:
                        print(
                            "Die Grabstätte kostet 3400 Euro. Es sind 2 Erdbestattungen und 4 Urnenbeisetzungen möglich.")
                        break
                    elif stellen == 3:
                        print(
                            "Die Grabstätte kostet 5100 Euro. Es sind 3 Erdbestattungen und 6 Urnenbeisetzungen möglich.")
                        break
                    elif stellen == 4:
                        print(
                            "Die Grabstätte kostet 6800 Euro. Es sind 4 Erdbestattungen und 8 Urnenbeisetzungen möglich.")
                        break

                    else:
                        print("Ungültige Anzahl. Bitte wählen Sie eine Zahl zwischen 1 und 4.")
                except ValueError:
                    print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            break
        elif grabart == "reihengrab":
            print("Ein Reihengrab kostet 830 Euro und läuft 20 Jahre, es ist nicht verlängerbar. Die Lage wird vorgegeben.")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie entweder 'wahlgrab' oder 'reihengrab'.")


def feuerbestattung():
    while True:
        pflege = input(
            "Soll die Pflege des Grabes von Ihnen erfolgen oder vom Friedhof übernommen werden? (selbst/friedhof): ").strip().lower()
        if pflege == "selbst":
            print("Wir können Ihnen ein Urnenwahlgrab für 2 Urnen für 1400 Euro anbieten.")
            break
        elif pflege == "friedhof":
            print("Wir können Ihnen ein Urnengemeinschaftsgrab für 1 Urne mit Pflege für 1411 Euro anbieten.")
            grab = input("Möchten Sie dieses Angebot annehmen? (ja/nein): ").strip().lower()
            if grab == "nein":
                print("Alternativ können wir Ihnen eine Urnennische für 2 Urnen für 1300 Euro anbieten.")
            break
        else:
            print("Ungültige Eingabe. Bitte wählen Sie entweder 'selbst' oder 'friedhof'.")


def grab_arten_preise():
    print("Hier sind alle Grabarten und die jeweiligen Gebühren:")
    print("- Wahlgrab für Erdbestattung: 1700 Euro pro Stelle")
    print("- Reihengrab für Erdbestattung: 830 Euro, keine Verlängerung möglich, Laufzeit 20 Jahre")
    print("- Urnengemeinschaftsgrab: 1411 Euro inklusive Pflege")
    print("- Urnenwahlgrab: 1400 Euro für 2 Urnen")
    print("- Urnennische: 1300 Euro für 2 Urnen")


def grab_verlaengerung():
    print("Die Verlängerung eines Wahlgrabes für eine Erdbestattung pro Stelle kostet 53 Euro pro Jahr.")
    print("Die Verlängerung eines zweistelliges Urnenwahlgrab kostet 43 Euro pro Jahr.")
    print("Die Verlängerung einer Urnennische kostet 51 Euro pro Jahr.")
    print("Die Verlängerung eines Urnengemeinschaftsgrabes mit Pflege kostet 48 Euro pro Jahr.")


# Start des Programms
friedhof_beratung()