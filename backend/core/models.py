# Defining Pydentic models for loading in our LLM data
from typing import List,Dict , Any , Optional
from pydantic import BaseModel, Field

# We are creating this detailed class because we want LLM to give the
# data in so we are going to specify all the fields we want to be included
# in the data that comes back from the LLM by writing all these descriptions
# and LLM will know how to populate this so that we can get the correct data

# We are mapping exactly story to look like within this python class structure
# So we can pass to LLN
class StoryOptionLLM(BaseModel):
    text: str = Field(description="the test of the option shown to the user")
    nextNode: Dict[str, Any] = Field(description="the next node content and its options")

class StoryNodeLLM(BaseModel):
    content:str = Field(description="the main content of the story node")
    isEnding: bool = Field(description="Whether this node is an ending node")
    isWinningEnding: bool = Field(description="Whether this node is a winning ending node")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="The options for this node")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="the title of the story")
    rootNode: StoryNodeLLM = Field(description="the root node of the story")


