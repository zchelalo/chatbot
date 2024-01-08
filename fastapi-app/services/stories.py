from models.stories import Story as StoryModel
from schemas.stories import Story as StorySchema, StoryUpdate as StoryUpdateSchema

class StoryService():
  def __init__(self, db) -> None:
    self.db = db

  def get_stories(self):
    with self.db as session:
      result = session.query(StoryModel).all()
      return result
  
  def get_story(self, id):
    with self.db as session:
      result = session.query(StoryModel).where(StoryModel.id == id).one_or_none()
      return result
  
  def create_story(self, story: StorySchema):
    with self.db as session:
      new_story = StoryModel(**story.model_dump())
      session.add(new_story)
      session.commit()
      session.refresh(new_story)
      return new_story
  
  def update_story(self, story: StorySchema, story_update: StoryUpdateSchema):
    with self.db as session:
      for field, value in story_update.model_dump(exclude_unset=True).items():
        setattr(story, field, value)

      session.commit()
      session.refresh(story)
      return story
  
  def delete_story(self, story):
    with self.db as session:
      session.delete(story)
      session.commit()
      return