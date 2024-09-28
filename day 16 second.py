counter = 0
while True:
    lyric = input("""
Finish the following lyric:

I'm not ______ to take a stand!

your answer: """)
    
    if lyric != "afraid":
        print("""
Close! Why don't you try one more time!""")
        
        lyric
        counter += 1
    else:
        print("""
Congrat! You got it! 
""")
        lyric
        counter += 1
        break
print("""Good job! The number of tries it took you to get it right is: """, counter)