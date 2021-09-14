""" default setting configurations

each constant is set to its equivalent in environment variables or hardcoded default below

"""

import os


# --------------- Map -------------- #

MAP_PATH = os.environ.get("MAP_PATH", None) or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "maps", "map9.json")


# --------------- Logging -------------- #

GAME_LOG_DESTINATION = os.environ.get("GAME_LOG_DESTINATION", None) or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '../gameLog')
GAME_LOG_STATIC_FILENAME = os.environ.get("GAME_LOG_STATIC_FILENAME", None)

AGENT_LOG_DESTINATION = os.environ.get("AGENT_LOG_DESTINATION", None) or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '../agentLog')

GAME_LOG_LOGGER_LEVEL = os.environ.get("GAME_LOG_LOGGER_LEVEL", None) or 10
GAME_LOG_TO_STDERR = os.environ.get("GAME_LOG_TO_STDERR", None) or True
GAME_LOG_TO_FILE = os.environ.get("GAME_LOG_TO_FILE", None) or True

AGENT_LOG = os.environ.get("AGENT_LOG", None) or True
AGENT_LOG_TO_FILE = os.environ.get("AGENT_LOG_TO_FILE", None) or True


# --------------- Players -------------- #

PLAYER_1_NAME = os.environ.get("PLAYER_1_NAME", None) or 'First player'
PLAYER_2_NAME = os.environ.get("PLAYER_2_NAME", None) or 'Second player'


# --------------- Turn -------------- #

TURN_INIT = os.environ.get("TURN_INIT", None) or 0


# --------------- Timeout -------------- #

TIME_OUT = os.environ.get("TIME_OUT", None) or 0.4
TIME_OUT_BEHAVIOUR = os.environ.get("TIME_OUT_BEHAVIOUR", None) or 'kill'
