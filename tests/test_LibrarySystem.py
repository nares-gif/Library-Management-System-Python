import pytest  
from LibrarySystem import BookRepository, LibraryService

@pytest.fixture
def service():
    repository = BookRepository(r"tests\test data\test_books.json", "tests_library")
    repository.books_dict = {}
    return LibraryService(repository)

@pytest.fixture
def service_with_data(service):
    service.add_book("Sapiens")
    return service


# TEST ADD BOOK    
def test_add_book_success(service):
    success, message = service.add_book("Supernova")
    assert success is False
    assert "Supernova" in message

def test_add_book_blank(service):
    success, message = service.add_book("")
    assert success is False

def test_add_book_blankspace(service):
    success, message = service.add_book("  ")
    assert success is False
    
# TEST ISSUE BOOKS
def test_issue_book_success(service_with_data):
    success, message = service_with_data.issue_books("101", "Karina")
    assert success is True
 
def test_issue_book_not_found(service):
    success, message = service.issue_books("1000", "Karina")
    assert success is False
    assert "Not found" in message.lower()
 
def test_issue_book_already_issued(service_with_data):
    service_with_data.issue_books("101", "Karina")  
    success, message = service_with_data.issue_books("101", "Someone Else")  # coba pinjam lagi
    assert success is False


# TEST RETURN BOOKS
def test_return_book_success(service_with_data):
    success, message = service_with_data.return_books("101")
    assert success is True

def test_return_books_available(service_with_data):
    success, message = service_with_data.return_books("101")
    assert success is False 

def test_return_books_not_found(service_with_data):
    success, message = service_with_data.return_books("1000")
    assert success is False
    assert "Not found" in message.lower()
    
## TEST SEARCH BOOKS
def test_search_books_sucess(service_with_data):
    result = service_with_data.search_books("sapiens")
    assert len(result) == 1

def test_search_books_not_found(service_with_data):
    result = service_with_data.service_with_data("Non exist book")
    assert len(result) == 0


# TEST DELETE BOOK
def test_delete_book_success(service_with_data):
    success, message = service_with_data.delete_book("101")
    assert success is True
    assert "101" not in service_with_data.get_all_books()

def test_delete_book_not_found(service):
    success, message = service.delete_book("1000")
    assert success is False
    
