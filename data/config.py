from environs import Env


env = Env()
env.read_env()
POSTGRES_URI = env.str('POSTGRES_URI') 
