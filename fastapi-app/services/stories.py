from models.stories import Story as StoryModel
from schemas.stories import Story as StorySchema, StoryUpdate as StoryUpdateSchema

class StoryService():
  def __init__(self, db) -> None:
    self.db = db

  def get_stories(self):
    result = self.db.query(StoryModel).all()
    return result
  
  def get_story(self, id):
    result = self.db.query(StoryModel).where(StoryModel.id == id).one_or_none()
    return result
  
  def create_story(self, story: StorySchema):
    new_story = StoryModel(**story.model_dump())
    self.db.add(new_story)
    self.db.commit()
    self.db.refresh(new_story)
    return new_story
  
  def update_story(self, story: StorySchema, story_update: StoryUpdateSchema):
    for field, value in story_update.model_dump(exclude_unset=True).items():
      setattr(story, field, value)

    self.db.commit()
    self.db.refresh(story)
    return story
  
  def delete_story(self, story):
    self.db.delete(story)
    self.db.commit()
    return