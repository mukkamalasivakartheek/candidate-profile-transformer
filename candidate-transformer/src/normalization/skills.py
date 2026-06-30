CANONICAL = {

    "node": "nodejs",
    "node.js": "nodejs",
    "py": "python",
    "k8s": "kubernetes"
}


def normalize_skill(skill):

    skill = skill.lower().strip()

    return CANONICAL.get(skill, skill)