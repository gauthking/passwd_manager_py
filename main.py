import argparse
from master_pwd import verify_master_pwd
from storage import add_pwd, get_pwd, update_pwd, delete_pwd
from config import MASTER_PWD, load_key

def parse_arguments():
    parser = argparse.ArgumentParser(description="!GAUTHKINGG CLI PWD MANAGER!")
    subparsers = parser.add_subparsers(dest="command", help="available commands")

    # to add pwd
    add_parser = subparsers.add_parser("add", help="Add a new password")
    add_parser.add_argument("service", help="Service Name")
    add_parser.add_argument("password", help="Password for the service")

    # to retrieve the pwd
    get_parser = subparsers.add_parser("get", help="Retrieve a password")
    get_parser.add_argument("service", help="Service name")

    # update the pwd
    update_parser = subparsers.add_parser("update", help="Update a password")
    update_parser.add_argument("service", help="Service name")
    update_parser.add_argument("new_pwd", help="New password for the service")

    #delete pwd
    delete_parser = subparsers.add_parser("delete", help="delete a password")
    delete_parser.add_argument("service", help="service name")

    return parser.parse_args()

def main():
    master_key = load_key()

    if verify_master_pwd(MASTER_PWD):
        args = parse_arguments()

        if args.command == "add":
            add_pwd(args.service, args.password, master_key)
        elif args.command == "get":
            get_pwd(args.service, master_key)
        elif args.command == "update":
            update_pwd(args.service, args.new_pwd, master_key)
        elif args.command == "delete":
            delete_pwd(args.service, master_key)
        else:
            print("Invalid Commandd!!!! Use -h for help")

if __name__ == "__main__":
    main()