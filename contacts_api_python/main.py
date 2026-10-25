from contacts_api_python.cli import parse_arguments
from contacts_api_python.read import read_contacts
from contacts_api_python.representation import show_contacts
from contacts_api_python.search import search_contacts


def main() -> None:
    args = parse_arguments()
    contacts = read_contacts(args.json_path)
    if args.search_term:
        contacts = search_contacts(contacts, args.search_term)
    show_contacts(contacts)


if __name__ == "__main__":
    main()
