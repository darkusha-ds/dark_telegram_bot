from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN_def")
# TOKEN = env.str("TOKEN_test")