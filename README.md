# Wordle Backend Project3 : Reading Replications and Adding New API Endpoints

Group 4 team members:
Florentino Becerra,
Kevin Delgado,
Ly Nguyen,
Steven Rico

Steps to run the project:

1. Ensure that your nginx service is configured to our tutorial.txt file

2. Start the API by running

   foreman start
   
3. Then initialize the database and after starting the API:

   ./bin/init.sh

4. Check if the replications is working use these commands:
   
   - Initialize a user, use this command:
     http POST http://tuffix-vm/new-user/ first_name="firstname" last_name="lastname" user_name="username" password="password"

   - To start a new game with the specified user, use this command:
     http --auth username:password POST http://tuffix-vm/new-game/
     
   - To guess a word in the game you are playing, use this command:
     http --auth username:password POST http://tuffix-vm/make-guess/ gameid="uuid_number" word="guess"
   
   - To get a game by the specified game id, use this command:
     http --auth username:password http://tuffix-vm/grab-game-by-game-id/?id="Gameid"

   - To get all games for the specified user, use this command:
     http --auth username:password http://tuffix-vm/grab-games/
     
5. To post the results of a game and guesses the user made, use command:

   http POST http://127.0.0.1:5100/results/ username="username" score="score"
 
6. To Retrieve the 10 users by average score, use command:

   http GET http://127.0.0.1:5100/top-scores/
