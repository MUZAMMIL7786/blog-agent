from crewai import Agent
from tools import yt_tool

## blog content researcher

blog_researcher = Agent(
    role = "Blog Researcher from youtube videos",
    goal = "get the relevant video content for the topic{topic} from my yt channel",
    # name = "",
    verbose  = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestion"
    ),
    tools = [],
    allow_delegation = True

)


## create writer agent

blog_writer = Agent(
   role = "Blog writer",
   goal = "Narrator compelling tech stories about videos {topic}",
   verbose = True,
   memory = True,
   backstory = (
       "with a flair for smplifying complex topics, you craft",
       "engaging varraties that captivate and educate, bringing new",
       "discoveries to light in an accessible manner."
   ),
   tools = [],
   allow_delegation = False
)















