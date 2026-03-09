from typing import Optional

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class ExerciseSchema(BaseModel):
    """
    Описание структуры урока.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    min_score: int = Field(alias="minScore")
    max_score: int = Field(alias="maxScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения уроков.
    """
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения урока.
    """
    exercise: ExerciseSchema


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания урока.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str]
    max_score: Optional[int] = Field(alias="maxScore")
    min_score: Optional[int] = Field(alias="minScore")
    order_index: Optional[int] = Field(alias="orderIndex")
    description: Optional[str]
    estimated_time: Optional[str] = Field(alias="estimatedTime")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа обновления урока.
    """
    exercise: ExerciseSchema
