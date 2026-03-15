# interface (commandline handling)
from database import Database

def main():

    db = Database()

    # welcome message
    print("The Very Hungry Database")
    print("Command it using:\n* SET <key> <value>\n* GET <key>\n* EXIT")
    print("\n\nOoOoOoOoO(:>)")
    print("^ ^ ^ ^ ^\n")

    # input loop
    while True:
        # prepare for input
        try:
            command = input().strip()
        except EOFError:
            break

        if not command:
            print("BLEH not a command")
            continue

        # parse
        parts = command.split(" ", 2)
        action = parts[0]

        # if SET
        if action == "SET" and len(parts) == 3:
            key = parts[1]
            val = parts[2]

            db.set(key, val)
            print("nom nom nom")

        # if GET
        elif action == "GET" and len(parts) == 2:
            key = parts[1]

            result = db.get(key)

            if result is None:
                print("mmmmmrrrr not in here...")
            else:
                print(f"*throws up* here you go: {result}")

        elif action == "EXIT":
            print("bye bye")
            break

        else:
            print("UMMM not a command!")

if __name__ == "__main__":
    main()