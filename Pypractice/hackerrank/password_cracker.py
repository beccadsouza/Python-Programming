test_cases = int(input())

for test_case in range(test_cases):

    users = int(input())
    passwords = list(input().split())
    login_attempt = input()
    login_attempt_copy = login_attempt
    sorted_passwords = sorted(passwords, key=len, reverse=True)
    for password in sorted_passwords:
        login_attempt = login_attempt.replace(password,"")
    if len(login_attempt) != 0:
        print("WRONG PASSWORD")
    else:
        for password in sorted_passwords:
            try:
                pos = login_attempt_copy.index(password)
                print(password,pos)
                login_attempt_copy = login_attempt_copy.replace(password,"",1)
                print("now",login_attempt_copy)
            except ValueError:
                print(password,"not present")
