import datetime
import json


class BookRepository:
    def __init__(self, file_path, library_name: str) -> None:
        self.file_path:str = file_path        
        self.library_name:str = library_name
        self.books_dict:dict = {}
       
    def save_data(self) -> None:
        with open(self.file_path, "w") as bk:
            json.dump(self.books_dict, bk, indent = 4)
    
    def load_data(self) -> None:
        try:
            with open(self.file_path, "r") as bk:
                self.books_dict = json.load(bk)

        except FileNotFoundError:
            self.books_dict = {}
            self.save_data() 
        
        except json.JSONDecodeError:
            print("DATA FILE CORRUPT")
            self.books_dict = {}
    
    def get_all(self) -> dict:
        return self.books_dict
    
    def get_by_id(self, books_id: str) -> dict|None:
        return self.books_dict.get(books_id)
    
    def exists(self, books_id: str) -> bool:
        return books_id in self.books_dict
    
    def add(self, books_id: str, data: dict) -> None:
        self.books_dict[books_id] = data
        self.save_data()
    
    def update(self, books_id: str, data: dict) -> None:
        self.books_dict[books_id].update(data)
        self.save_data()
    
    def delete(self, books_id: str) -> None:
        del self.books_dict[books_id]
        self.save_data()
    
    def next_id(self) -> str:
        if self.books_dict:
            return str(max(map(int, self.books_dict.keys()))+1)
        return "101"
    
class LibraryService():
    def __init__(self, repository: BookRepository):
        self.repository = repository
    
    def get_all_books(self) -> dict:
        return self.repository.get_all()
        
    def issue_books(self, books_id: str, borrower_name: str) -> tuple[bool, str]:
        book = self.repository.get_by_id(books_id)
        
        if book is None:
            return False, "Book ID not found"
        if book["status"] != "available":
            return False, (f"This book is already issued to {book['lender_name']} " f"on {book['issue_date']}")
            
        current_date: str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")    
        
        self.repository.update(books_id, {
            "lender_name": borrower_name,
            "status": "already issued",
            "issue_date": current_date
        })
        
        return True, "The book was issued succesfully"
        
    
    def add_book(self, title: str) -> tuple[bool, str]:        
        if title.strip() == "":
            return False, "title cannot be empty. input the title!"
            
        new_id = self.repository.next_id()
        self.repository.add(new_id,{
            "books_title": title,
            "lender_name": "",
            "status": "available",
            "issue_date": ""
        })
        return True, f"{title} added successfully"
    
    def return_books(self, books_id:str) -> tuple[bool,str]: 
        book = self.repository.get_by_id(books_id)
               
        if book is None:
            return False, "Book ID not found"
        
        if book["status"] == "available":
            return False, "This book is already available"
        
        self.repository.update(books_id, {
        "lender_name": "",
        "status": "available",
        "issue_date": ""    
        })
        return True, "Books succesfully returned"
        
    def search_books(self, search: str) -> dict:
        search = search.lower()
        return {
            books_id: data
            for books_id, data in self.repository.get_all().items()
                if search in data.get("books_title", "").lower()
        }
        
    def delete_book(self, books_id: str) -> None:        
        book = self.repository.get_by_id(books_id)
        if book is None:
            return False, "Book ID not found"
        
        title = book["books_title"]
        self.repository.delete(books_id)
        return True, f"{title} successfully deleted"
        
        
    