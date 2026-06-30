from pydantic import BaseModel
from typing import List, Optional


class Skill(BaseModel):
    name: str
    confidence: float
    sources: List[str]


class Experience(BaseModel):
    company: Optional[str]
    title: Optional[str]
    start: Optional[str]
    end: Optional[str]
    summary: Optional[str]


class Education(BaseModel):
    institution: Optional[str]
    degree: Optional[str]
    field: Optional[str]
    end_year: Optional[int]


class Location(BaseModel):
    city: Optional[str]
    region: Optional[str]
    country: Optional[str]


class Links(BaseModel):
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None
    other: List[str] = []


class Provenance(BaseModel):
    field: str
    source: str
    method: str


class CandidateProfile(BaseModel):

    candidate_id: str

    full_name: Optional[str]

    emails: List[str]

    phones: List[str]

    location: Optional[Location]

    links: Optional[Links]

    headline: Optional[str]

    years_experience: Optional[float]

    skills: List[Skill]

    experience: List[Experience]

    education: List[Education]

    provenance: List[Provenance]

    overall_confidence: float