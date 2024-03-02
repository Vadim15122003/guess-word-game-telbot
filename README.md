# GuessWordGame TelegramBot
## [Click here to open bot](https://t.me/guessword_gamebot)

### Is a telegram bot that implements a game
> Rules of the game:  
> Everyone receives a word in private. Some people did not receive the word  
> those people will have to guess it  
> The rest of the people will have to guess the people who do not know the word  
>  
> \- To guess the word write in private /report_word then you will be able to send the word  
> \- If you guess you will receive 3 points if not you will lose 1 point and the game will end for you  
> \- If you think you guessed the word but said a synonym you can write /verify_my_word and the other players will vote if you said the word correctly or not  
>  
> \- To guess the person who does not know the word write in private /report_player and then you will be able to select from a list the person you suspect  
> \- If you do not guess both you and that person will leave the game and the one who did not guess will lose 4 points  
> \- If you guess the game will end and you will receive 2 points, and if there are no more people who do not know the word the game will end  
>  
> Next, each in turn will ask the next player a question and that will have to answer  
> Player number 1 will ask player number 2 a question, and number 2 will answer after which number 2 will ask a question to number 3 and so on  
> In this way the players who know the word will have to figure out who does not know it, and those who do not know the word must figure out what that word is  
>

### Libraryes that you need:
> - pip install pyTelegramBotAPI
> - pip install python-dotenv

> **./infinite_runner.sh** will run program and if they end with an error they will restart them and save error in error.log file (use chmod +x
> to have permission to run this script in bash)
