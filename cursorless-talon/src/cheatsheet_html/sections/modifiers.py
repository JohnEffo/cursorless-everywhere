from ..get_list import get_raw_list, make_dict_readable

MODIFIER_LIST_NAMES = [
    "simple_modifier",
    "interior_modifier",
    "head_tail_modifier",
    "simple_scope_modifier",
    "first_modifier",
    "last_modifier",
    "previous_next_modifier",
    "backward_modifier",
]


def get_modifiers():
    all_modifiers = {}
    for name in MODIFIER_LIST_NAMES:
        all_modifiers.update(get_raw_list(name))

    complex_modifier_ids = [
        "extendThroughStartOf",
        "extendThroughEndOf",
        "every",
        "first",
        "last",
        "previous",
        "next",
        "backward",
    ]
    simple_modifiers = {
        key: value
        for key, value in all_modifiers.items()
        if value not in complex_modifier_ids
    }
    complex_modifiers = {
        value: key
        for key, value in all_modifiers.items()
        if value in complex_modifier_ids
    }

    return [
        *make_dict_readable(
            "modifier",
            simple_modifiers,
            {
                "excludeInterior": "Bounding paired delimiters",
                "toRawSelection": "No inference",
                "leading": "Leading delimiter range",
                "trailing": "Trailing delimiter range",
            },
        ),
        {
            "id": "extendThroughStartOf",
            "type": "modifier",
            "variations": [
                {
                    "spokenForm": complex_modifiers["extendThroughStartOf"],
                    "description": "Extend through start of line",
                },
                {
                    "spokenForm": f"{complex_modifiers['extendThroughStartOf']} <modifier>",
                    "description": "Extend through start of <modifier>",
                },
            ],
        },
        {
            "id": "extendThroughEndOf",
            "type": "modifier",
            "variations": [
                {
                    "spokenForm": complex_modifiers["extendThroughEndOf"],
                    "description": "Extend through end of line",
                },
                {
                    "spokenForm": f"{complex_modifiers['extendThroughEndOf']} <modifier>",
                    "description": "Extend through end of <modifier>",
                },
            ],
        },
        {
            "id": "containingScope",
            "type": "modifier",
            "variations": [
                {
                    "spokenForm": f"<scope>",
                    "description": "Containing instance of <scope>",
                },
            ],
        },
        {
            "id": "every",
            "type": "modifier",
            "variations": [
                {
                    "spokenForm": f"{complex_modifiers['every']} <scope>",
                    "description": "Every instance of <scope>",
                },
            ],
        },
        {
            "id": "relativeScope",
            "type": "modifier",
            "variations": [
                {
                    "spokenForm": f"{complex_modifiers['previous']} <scope>",
                    "description": "Previous instance of <scope>",
                },
                {
                    "spokenForm": f"{complex_modifiers['next']} <scope>",
                    "description": "Next instance of <scope>",
                },
                {
                    "spokenForm": f"<ordinal> {complex_modifiers['previous']} <scope>",
                    "description": "<ordinal> instance of <scope> before target",
                },
                {
                    "spokenForm": f"<ordinal> {complex_modifiers['next']} <scope>",
                    "description": "<ordinal> instance of <scope> after target",
                },
                {
                    "spokenForm": f"{complex_modifiers['previous']} <number> <scope>s",
                    "description": "previous <number> instances of <scope>",
                },
                {
                    "spokenForm": f"<number> <scope>s {complex_modifiers['backward']}",
                    "description": "<number> instances of <scope> including target, going backwards",
                },
                {
                    "spokenForm": f"<number> <scope>s",
                    "description": "<number> instances of <scope> including target, going forwards",
                },
                {
                    "spokenForm": f"{complex_modifiers['next']} <number> <scope>s",
                    "description": "next <number> instances of <scope>",
                },
            ],
        },
        {
            "id": "ordinalScope",
            "type": "modifier",
            "variations": [
                {
                    "spokenForm": f"<ordinal> <scope>",
                    "description": "<ordinal> instance of <scope> in iteration scope",
                },
                {
                    "spokenForm": f"<ordinal> {complex_modifiers['last']} <scope>",
                    "description": "<ordinal>-to-last instance of <scope> in iteration scope",
                },
                {
                    "spokenForm": f"{complex_modifiers['first']} <number> <scope>s",
                    "description": "First <number> instances of <scope> in iteration scope",
                },
                {
                    "spokenForm": f"{complex_modifiers['last']} <number> <scope>s",
                    "description": "Last <number> instances of <scope> in iteration scope",
                },
            ],
        },
    ]
