class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None               


class StudentList:
    def __init__(self):
        self.head = None       
    def add_student(self, student_id, student_name, gpa):
        new_node = StudentNode(student_id, student_name, gpa)
        if self.head is None:          
            self.head = new_node
            return
        current = self.head
        while current.next is not None: 
            current = current.next
        current.next = new_node
    def delete_student(self, student_id):
        current = self.head
        if current is not None and current.student_id == student_id:
            self.head = current.next   
            return True
        previous = None
        while current is not None and current.student_id != student_id:
            previous = current         
            current = current.next
        if current is None:
            return False               
        previous.next = current.next    
        return True
    def display_all(self):
        if self.head is None:
            print("Siyahıda tələbə yoxdur.")
            return
        current = self.head
        while current is not None:
            print(current.student_id, current.student_name, current.gpa)
            current = current.next

    # 4. GPA > 80 olanları göstər
    def show_high_gpa(self):
        current = self.head
        while current is not None:
            if current.gpa > 80:
                print(current.student_id, current.student_name, current.gpa)
            current = current.next

    # 5. Ada görə axtarış
    def search_by_name(self, name):
        current = self.head
        while current is not None:
            if current.student_name == name:
                print("Tapıldı:", current.student_id,
                      current.student_name, current.gpa)
                return
            current = current.next
        print("Tapılmadı.")
    def count_students(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
students = StudentList()
while True:
    print("\n TƏLƏBƏ QEYDİYYAT SİSTEMİ ")
    print("1. Tələbə əlavə et")
    print("2. Tələbə sil")
    print("3. Bütün tələbələri göstər")
    print("4. GPA > 80 olanları göstər")
    print("5. Ada görə axtarış")
    print("6. Sayı göstər")
    print("0. Çıxış")

    secim = input("Seçim: ")

    if secim == "1":
        sid = int(input("ID: "))
        ad = input("Ad: ")
        gpa = float(input("GPA: "))
        students.add_student(sid, ad, gpa)
        print("Əlavə olundu.")

    elif secim == "2":
        sid = int(input("Silinecək ID: "))
        if students.delete_student(sid):
            print("Silindi.")
        else:
            print("Bu ID yoxdur.")

    elif secim == "3":
        students.display_all()

    elif secim == "4":
        students.show_high_gpa()

    elif secim == "5":
        ad = input("Ad axtar: ")
        students.search_by_name(ad)

    elif secim == "6":
        print("Say:", students.count_students())

    elif secim == "0":
        print("Bağlanır...")
        break

    else:
        print("Yanlış seçim!")
