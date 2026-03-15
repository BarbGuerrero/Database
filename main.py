# interface (commandline handling)
from database import Database

def main():

    db = Database()

    # input loop
    while True:
        # prepare for input
        try:
            command = input().strip()
        except EOFError:
            break

        if not command:
            continue

        # parse
        parts = command.split(" ", 2)
        action = parts[0]

        # if SET
        if action == "SET" and len(parts) == 3:
            key = parts[1]
            val = parts[2]

            db.set(key, val)
            print("OK")

        # if GET
        elif action == "GET" and len(parts) == 2:
            key = parts[1]

            result = db.get(key)

            if result is None:
                print("")
            else:
                print(result)

        elif action == "EXIT":
            print("bye bye")
            break

        else:
            print("ERROR")

if __name__ == "__main__":
    main()