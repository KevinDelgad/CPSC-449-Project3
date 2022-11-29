from pydoc import doc
import collections
import dataclasses
import textwrap
import redis

# Necessary quart imports
from quart import Quart, g, request, abort
from quart_schema import QuartSchema, RequestSchemaValidationError, validate_request

app = Quart(__name__)
QuartSchema(app)

# Initialize redis client
redisClient = redis.Redis(host='localhost', port=6379, db=0)

# Create a data class to assist with API data
@dataclasses.dataclass
class LeaderboardInfo:
    """ Contains details for a leaderboard. """
    username: str
    score: int


# Results posting endpoint
# Note: validate_request takes a param that is the data class just created
@app.route("/results/", methods=["POST"])
@validate_request(LeaderboardInfo)
async def postResults(data: LeaderboardInfo):
    """
    This function is responsible for posting the results of a game
    As it is not yet tied to the actual game, it currently takes in any values

    @return: 200 if successful
    Potential: May return 401 if data does not match the LeaderboardInfo dataclass template
    """

    # Create sorted set
    leaderboardSet = "Leaderboard"
    leaderboardData = dataclasses.asdict(data)

    # Were we able to post?
    if redisClient.zadd(leaderboardSet, leaderboardData[score], leaderboardData[username]) == 1:
        return leaderboardData, 200
    else:
        return {"Error:" "Something went wrong."}, 404


@app.route("/top-scores/", methods=["GET"])
async def topScores():
    """
    this function is responsible for displaying the top 10 scores found in the database
    """

