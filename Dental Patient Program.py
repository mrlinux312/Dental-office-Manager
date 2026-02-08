import datetime

patients = {}
appointments = []

def add_patient():
    pid = input("Enter patient ID: ").strip()
    if pid in patients:
        print("Patient ID already exists.")
        return
    name = input("Enter patient name: ").strip()
    phone = input("Enter phone number: ").strip()
    notes = input("Enter notes (optional): ").strip()
    patients[pid] = {
        "name": name,
        "phone": phone,
        "notes": notes
    }
    print("Patient added.\n")

def list_patients():
    if not patients:
        print("No patients found.\n")
        return
    for pid, info in patients.items():
        print(f"ID: {pid} | Name: {info['name']} | Phone: {info['phone']} | Notes: {info['notes']}")
    print()

def schedule_appointment():
    pid = input("Enter patient ID: ").strip()
    if pid not in patients:
        print("Patient not found.\n")
        return
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    time_str = input("Enter time (HH:MM, 24h): ").strip()
    reason = input("Reason for visit: ").strip()

    try:
        dt = datetime.datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date/time format.\n")
        return

    appointments.append({
        "patient_id": pid,
        "datetime": dt,
        "reason": reason
    })
    print("Appointment scheduled.\n")

def list_appointments():
    if not appointments:
        print("No appointments scheduled.\n")
        return
    sorted_appts = sorted(appointments, key=lambda a: a["datetime"])
    for appt in sorted_appts:
        p = patients.get(appt["patient_id"], {"name": "Unknown"})
        print(f"{appt['datetime']} | {p['name']} (ID: {appt['patient_id']}) | Reason: {appt['reason']}")
    print()

def main():
    while True:
        print("=== Dental Office Manager ===")
        print("1. Add patient")
        print("2. List patients")
        print("3. Schedule appointment")
        print("4. List appointments")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_patient()
        elif choice == "2":
            list_patients()
        elif choice == "3":
            schedule_appointment()
        elif choice == "4":
            list_appointments()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()

