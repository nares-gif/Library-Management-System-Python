from LibrarySystem import BookRepository, LibraryService
   
def display_book(books: dict) -> None:
    if not books:
        print("No book found")
        return   
    print("----------------------------List of books----------------------------")
    print("Books ID", "\t\t", "Title")
    print("---------------------------------------------------------------------")

    for books_id, data in books.items():
        print(books_id, "\t\t", data.get("books_title"), "-[", data.get("status"), "]")
   
                
def main() -> None:
    repo = BookRepository("data/books.json", "LMS")
    lms = LibraryService(repo)
    
    key_list = {"1": "Display Books", "2": "Issue Books", "3": "Add Books", "4": "Return Books", "5": "Search Books", "6": "Delete Books", "q": "quit"}
    
    repo.load_data()
    
    while True:
                
        print(f"============ Welcome To Library ============= \n")
        for key, value in key_list.items():
            print(f"({key}) {value}")
        
        choice = input("enter your choice: ")
        
        if choice == "1":
            display_book(lms.get_all_books())
            
        elif choice == "2": 
            books_id:str = input("enter book id: ")
            borrower_name: str = input("enter your name: ")
            validation, message = lms.issue_books(books_id, borrower_name)
            print(message)
            
        elif choice == "3":
            title:str = input("Enter title: ")
            validation, message = lms.add_book(title)
            print(message)
            
        elif choice == "4":
            books_id:str = input("enter books id: ")
            validation, message = lms.return_books(books_id)
            print(message)
            
        elif choice == "5":
            search: str = input("Enter books title: ").strip().lower()
            books = lms.search_books(search)
            print(books)
            
        elif choice == "6":
            books_id: str = input("Enter books ID: ")
            validation, message = lms.delete_book(books_id)
            print(message)
            
        elif choice == "q":
            break
        else:
            print("error! please check your input")
        
            
            
if __name__ == "__main__":
   main()   


