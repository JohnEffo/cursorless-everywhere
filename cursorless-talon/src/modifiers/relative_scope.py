from typing import Any

from talon import Module

previous_next_modifiers = {"previous": "previous", "next": "next"}
backward_modifiers = {"backward": "backward"}

mod = Module()

mod.list("cursorless_previous_next_modifier", desc="Cursorless previous/next modifiers")
mod.list("cursorless_backward_modifier", desc="Cursorless backward modifiers")


@mod.capture(rule="{user.cursorless_previous_next_modifier}")
def cursorless_relative_direction(m) -> str:
    """Previous/next"""
    return "backward" if m[0] == "previous" else "forward"


@mod.capture(
    rule="[<user.ordinals_small>] <user.cursorless_relative_direction> <user.cursorless_scope_type>"
)
def cursorless_relative_scope_singular(m) -> dict[str, Any]:
    """Relative previous/next singular scope, eg `"next funk"` or `"third next funk"`."""
    return create_relative_scope_modifier(
        m.cursorless_scope_type,
        getattr(m, "ordinals_small", 1),
        1,
        m.cursorless_relative_direction,
    )


@mod.capture(
    rule="<user.cursorless_relative_direction> <number_small> <user.cursorless_scope_type_plural>"
)
def cursorless_relative_scope_plural(m) -> dict[str, Any]:
    """Relative previous/next plural scope. `next three funks`"""
    return create_relative_scope_modifier(
        m.cursorless_scope_type_plural,
        1,
        m.number_small,
        m.cursorless_relative_direction,
    )


@mod.capture(
    rule="<number_small> <user.cursorless_scope_type_plural> [{user.cursorless_backward_modifier}]"
)
def cursorless_relative_scope_count(m) -> dict[str, Any]:
    """Relative count scope. `three funks`"""
    return create_relative_scope_modifier(
        m.cursorless_scope_type_plural,
        0,
        m.number_small,
        getattr(m, "cursorless_backward_modifier", "forward"),
    )


@mod.capture(
    rule=(
        "<user.cursorless_relative_scope_singular> | "
        "<user.cursorless_relative_scope_plural> | "
        "<user.cursorless_relative_scope_count>"
    )
)
def cursorless_relative_scope(m) -> dict[str, Any]:
    """Previous/next scope"""
    return m[0]


def create_relative_scope_modifier(
    scope_type: dict, offset: int, length: int, direction: str
) -> dict[str, Any]:
    return {
        "type": "relativeScope",
        "scopeType": scope_type,
        "offset": offset,
        "length": length,
        "direction": direction,
    }
