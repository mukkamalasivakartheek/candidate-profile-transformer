from models.canonical import CandidateProfile


def validate(profile):

    return CandidateProfile(**profile)