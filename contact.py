#Contact 클래스 생성
class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

#사용자 정보 입력 함수 - input 함수 사용
def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr) #Contact클래스의 인스턴스 생성
    return contact

#메뉴 출력 함수
def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)

#연락처 출력 함수
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

#연락처 삭제 함수
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list): #enumerate: 리스트가 있는 경우 순서와 리스트의 값을 전달
        if contact.name == name: #contact에 담긴 name이 입력받은 name과 같다면
            del contact_list[i] #contact_list의 해당 리스트 삭제

#연락처 파일 저장 함수
def store_contact(contact_list):
    f = open("contact_db.txt", "wt") #contact_db.txt라는 이름의 텍스트 파일 wt모드로 열기
    for contact in contact_list: #contact_list를 순회하면서 각 인스턴스의 정보 출력
        f.write(contact.name + '\n') #contact_db.txt 파일에 정보 저장
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()

#연락처 파일 로드 함수
def load_contact(contact_list):
    f = open("contact_db.txt", "rt")
    lines = f.readlines() #readlines 함수를 이용해 파일에 있는 모든 데이터 읽어서 lines에 저장
    num = len(lines) / 4  #연락처 하나당 4줄의 데이터가 존재하므로 4로 나누어 데이터 개수 확인
    num = int(num)  #나눗셈 후 실수가 된 num을 정수형으로 변환

    for i in range(num): #num의 개수만큼 루프를 돌리면서 lines 리스트에 저장된 데이터를 읽어 들여 Contact 클래스의 인스턴스를 생성하고 생성한 인스턴스를 contact_list에 추가
        name = lines[4*i].rstrip('\n')
        phone = lines[4*i+1].rstrip('\n')
        email = lines[4*i+2].rstrip('\n')
        addr = lines[4*i+3].rstrip('\n')
        contact = Contact(name, phone, email, addr)
        contact_list.append(contact)
    f.close()

#실행 함수
def run():
    contact_list = [] #리스트 생성
    load_contact(contact_list) #저장된 파일 로드
    while 1: #프로그램이 계속 실행되도록 무한루프 사용
        menu = print_menu() #메뉴 출력
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact) #contact_list에 append 함수 사용해서 데이터 붙여넣기
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list) #리스트를 파일 형태로 저장
            break #무한루프 종료

if __name__ == "__main__": #인터프리터에서 직접 실행했을 경우에만 run 함수 실행

    run()
