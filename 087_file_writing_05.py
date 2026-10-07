"""
Complete the write_movie_info() function that takes 2 parameters:

filename - a string representing the name of the output text file.
movies - a list of strings, where each string contains information on a movie in the format: Name,Run_Time,Rating
The function should go through the movie information provided in the movies list and use it to write to the specified text file, a table containing this information.


The format of the table is as follows:

The table header has 3 columns: A column entitled 'Movie Name' that is 15 characters in width, a column entitled 'Run Time' that is 10 characters in width, and a column entitled 'Rating'
that is 8 characters in width. The titles of these columns are centred within each column.
The table header is followed by several rows, one row per movie. Each row has 3 columns corresponding to the movie's name, run time and rating. The movies should be arranged in
alphabetical order. These columns are formatted as follows:
The column for 'Movie Name' is 15 characters wide. If the name of the movie is more than 15 characters long, only the first 15 characters are displayed. If the name of the movie is 15
characters or less, it is right aligned in the column.
The column for 'Run Time' is 10 characters wide. The run time should be centred in the column. For example, if the run time is '96', then there will be 4 spaces on either side of the run
time. If, however, the run time is '110', then there will be 3 spaces on the left and 4 spaces on the right of the run time. In other words, if the number of spaces around the run time is
odd, there should be one more space on the right than there is on the left.
The column for 'Rating' is 8 characters wide. The rating should be centred in the column in the same way the run time is.
The table has borders made up of the '|' and '-' characters.


Note:

Remember to close any file you open.
"""

def write_movie_info(filename, movies):
    movies.sort()
    
    with open(filename, "w") as output_stream:
        output_stream.write(" --------------- ---------- --------\n")
        output_stream.write("|  Movie Name   | Run Time | Rating |\n")
        output_stream.write(" --------------- ---------- --------\n")
        
        for movie in movies:
            movie_list = movie.split(",")
            
            output_stream.write("|")
            if len(movie_list[0]) >= 15:
                movie_name = movie_list[0][:15]
                
            else:
                movie_name = (
                    f"{" " * (15 - len(movie_list[0]))}"
                    f"{movie_list[0]}"
                )
                
            output_stream.write(f"{movie_name}|")
            
            if len(movie_list[1]) == 2:
                run_time = f"    {movie_list[1]}    |"
                
            else:
                run_time = f"   {movie_list[1]}    |"
                
            output_stream.write(run_time)
            
            space_counter = int((8 - len(movie_list[2])) // 2) 
            if len(movie_list[2]) % 2 == 1:
                rating = (
                    f"{" " * space_counter}{movie_list[2]}"
                    f"{" " * (space_counter + 1)}|\n"
                )
                
            else:
                rating = (
                    f"{" " * space_counter}{movie_list[2]}"
                    f"{" " * (space_counter)}|\n"
                )
                
            output_stream.write(rating)
            
            output_stream.write(" --------------- ---------- --------\n")

def print_contents(filename):
    with open(filename, 'r') as input_file:
        content = input_file.read()
    print(content)

filename = '087_file_writing_05_file.txt'
movies = ["Marty Supreme,150,R13", "Primate,88,R16", "Mercy,100,M",
          "Iron Lung,127,R16", "The SpongeBob Movie: Search for Squarepants,96,PG",
          "Send Help,113,R16", "Mortal Kombat 2,116,R16"]
write_movie_info(filename, movies)
print_contents(filename)
