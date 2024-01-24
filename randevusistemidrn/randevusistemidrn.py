admins = []  
doctors = []  
patients = []  
appointments = []  
clinics = []  

def add_admin():
    Admin_ID = input("Enter Admin Username: ")
    Admin_Password = input("Enter Admin Password: ")
    admin_info = {"Admin_ID": Admin_ID, "Admin_Password": Admin_Password}
    admins.append(admin_info)
    print("New admin successfully added.")

def delete_admin():
    print("Admin List:")
    for i, admin in enumerate(admins, 1):
        print(f"{i}. Admin ID: {admin['Admin_ID']}")
    
    selected_admin = int(input("Select the number of the admin to delete: "))
    
    if 1 <= selected_admin <= len(admins):
        deleted_admin = admins.pop(selected_admin - 1)
        print(f"{deleted_admin['Admin_ID']} ID admin successfully deleted.")
    else:
        print("Invalid selection. Please try again.")

def view_admin():
    print("Admin List:")
    for admin in admins:
        print(f"Admin ID: {admin['Admin_ID']}")

def add_doctor():
    Dr_Name = input("Enter Doctor Name: ")
    Dr_Surname = input("Enter Doctor Surname: ")
    doctor_info = {"Dr_Name": Dr_Name, "Dr_Surname": Dr_Surname}
    doctors.append(doctor_info)
    print("New doctor successfully added.")

def delete_doctor():
    print("Doctor List:")
    for i, doctor in enumerate(doctors, 1):
        print(f"{i}. Doctor Name: {doctor['Dr_Name']} {doctor['Dr_Surname']}")
    
    selected_doctor = int(input("Select the number of the doctor to delete: "))
    
    if 1 <= selected_doctor <= len(doctors):
        deleted_doctor = doctors.pop(selected_doctor - 1)
        print(f"{deleted_doctor['Dr_Name']} {deleted_doctor['Dr_Surname']} successfully deleted.")
    else:
        print("Invalid selection. Please try again.")

def view_doctor():
    print("Doctor List:")
    for doctor in doctors:
        print(f"Doctor Name: {doctor['Dr_Name']} {doctor['Dr_Surname']}")

def add_patient():
    Tc = input("Enter Patient T.C. ID: ")
    Name = input("Enter Patient Name: ")
    Surname = input("Enter Patient Surname: ")
    Birth_date = input("Enter Patient Birth Date (YYYY-MM-DD): ")
    Birth_place = input("Enter Patient Birth Place: ")
    Address = input("Enter Patient Address: ")

    patient_info = {"Tc": Tc, "Name": Name, "Surname": Surname, "Birth_date": Birth_date, "Birth_place": Birth_place, "Address": Address}
    patients.append(patient_info)
    print("New patient successfully added.")

def delete_patient():
    print("Patient List:")
    for i, patient in enumerate(patients, 1):
        print(f"{i}. T.C. ID: {patient['Tc']}, Name: {patient['Name']} {patient['Surname']}")
    
    selected_patient = int(input("Select the number of the patient to delete: "))
    
    if 1 <= selected_patient <= len(patients):
        deleted_patient = patients.pop(selected_patient - 1)
        print(f"{deleted_patient['Name']} {deleted_patient['Surname']} successfully deleted.")
    else:
        print("Invalid selection. Please try again.")

def view_patient():
    print("Patient List:")
    for patient in patients:
        print(f"T.C. ID: {patient['Tc']}, Name: {patient['Name']} {patient['Surname']}, Birth Date: {patient['Birth_date']}, Birth Place: {patient['Birth_place']}, Address: {patient['Address']}")

def add_appointment():
    print("Doctor List:")
    for i, doctor in enumerate(doctors, 1):
        print(f"{i}. Doctor Name: {doctor['Dr_Name']} {doctor['Dr_Surname']}")
    
    selected_doctor = int(input("Select the number of the doctor for the appointment: "))
    
    if 1 <= selected_doctor <= len(doctors):
        selected_patient = input("Enter the T.C. ID of the patient for the appointment: ")
        appointment_date = input("Enter the appointment date (YYYY-MM-DD): ")
        appointment_time = input("Enter the appointment time: ")
        
        appointment_info = {"Doctor": doctors[selected_doctor - 1], "Patient_Tc": selected_patient, "Date": appointment_date, "Time": appointment_time}
        appointments.append(appointment_info)
        print("New appointment successfully added.")
    else:
        print("Invalid selection. Please try again.")

def clinic_info():
    clinic_name = input("Enter the name of the clinic: ")
    clinics.append(clinic_name)
    print("Clinic information successfully added.")

def cikis():
    print("Exiting the program...")
    exit()

def admin_panel():
    while True:
        print("\nAdmin Panel:")
        print("1. Add Admin")
        print("2. Delete Admin")
        print("3. View Admin")
        print("4. Add Doctor")
        print("5. Delete Doctor")
        print("6. View Doctor")
        print("7. Add Patient")
        print("8. Delete Patient")
        print("9. View Patient")
        print("10. Add Appointment")
        print("11. Clinic Info")
        print("12. Exit")
        
        choice = int(input("Select the operation you want to perform: "))
        
        if choice == 1:
            add_admin()
        elif choice == 2:
            delete_admin()
        elif choice == 3:
            view_admin()
        elif choice == 4:
            add_doctor()
        elif choice == 5:
            delete_doctor()
        elif choice == 6:
            view_doctor()
        elif choice == 7:
            add_patient()
        elif choice == 8:
            delete_patient()
        elif choice == 9:
            view_patient()
        elif choice == 10:
            add_appointment()
        elif choice == 11:
            clinic_info()
        elif choice == 12:
            cikis()
        else:
            print("Invalid selection. Please try again.")


admin_panel()

