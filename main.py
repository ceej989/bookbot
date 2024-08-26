def count_words(book):
  words = book.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    data = f.read()
    return data
  
def count_characters(book):
  '''
    Take text from book as string
    Return number of times each character appears
    { 'char': int, ... }
  '''
  char_count_dict = {}
  lowered_string = book.lower()
  
  for i in lowered_string:
    if i in char_count_dict and i.isalpha():
      char_count_dict[i] += 1
    elif i.isalpha():
      
      char_count_dict[i] = 1
  return char_count_dict

def print_book_report(book):
  words = count_words(book)
  print(f"{words} words found in the document")
  char_count = count_characters(book)
  char_count = dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
  for ch in char_count:
    print(f"The '{ch}' character was found times {char_count[ch]}")
  print(f"--- End report ---")



def main():
  file_path = './books/frankenstein.txt'
  text = get_book_text(file_path)
  print(f"--- Begin report of {file_path} ---")
  print_book_report(text)


main()