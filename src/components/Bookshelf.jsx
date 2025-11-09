import './Bookshelf.css'

function Bookshelf() {
  return (
    <div className="bookshelf-container">
      <div className="bookshelf-background">
        {/* Bookshelf shelves */}
        <div className="shelf shelf-1"></div>
        <div className="shelf shelf-2"></div>
        <div className="shelf shelf-3"></div>
        <div className="shelf shelf-4"></div>
        <div className="shelf shelf-5"></div>
        
        {/* Books on shelf */}
        <div className="books-row books-row-1">
          <div className="book-spine book-1"></div>
          <div className="book-spine book-2"></div>
          <div className="book-spine book-3"></div>
          <div className="book-spine book-4"></div>
          <div className="book-spine book-5"></div>
          <div className="book-spine book-6"></div>
          <div className="book-spine book-7"></div>
        </div>
        
        <div className="books-row books-row-2">
          <div className="book-spine book-8"></div>
          <div className="book-spine book-9"></div>
          <div className="book-spine book-10"></div>
          <div className="book-spine book-11"></div>
          <div className="book-spine book-12"></div>
          <div className="book-spine book-13"></div>
        </div>
        
        <div className="books-row books-row-3">
          <div className="book-spine book-14"></div>
          <div className="book-spine book-15"></div>
          <div className="book-spine book-16"></div>
          <div className="book-spine book-17"></div>
          <div className="book-spine book-18"></div>
          <div className="book-spine book-19"></div>
          <div className="book-spine book-20"></div>
        </div>

        <div className="books-row books-row-4">
          <div className="book-spine book-1"></div>
          <div className="book-spine book-2"></div>
          <div className="book-spine book-3"></div>
          <div className="book-spine book-4"></div>
          <div className="book-spine book-5"></div>
        </div>
      </div>
    </div>
  )
}

export default Bookshelf
