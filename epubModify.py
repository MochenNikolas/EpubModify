import ebooklib
from ebooklib import epub

def modify_epub(epubFilePath, newTitle, newAuthor, bookCoverImg, newFileName):

    # load the epub file
    book = epub.read_epub(epubFilePath)

    book.set_title(newTitle)
    book.add_author(newAuthor)

    with open(bookCoverImg, 'rb') as img:
        book.set_cover("cover.jpg", img.read(), create_page=True)

    # store the modified file
    epub.write_epub("newFileName" + ".epub", book, {})


if __name__ == '__main__':
    modify_epub('yourEpubFilePath', 'newTitle', 'newAuthor', 'yourEpubCoverImgPath', "newFileName")
